"""LangGraph state machine for the ReAct loop.

Nodes:
  plan      — LLM writes the investigation plan once (entry node)
  decide    — LLM picks the next tool given the scratchpad
  call      — runs the chosen tool, accumulates evidence
  observe   — distils the tool result into a short string for the agent
  done      — LLM writes the final markdown briefing

Edges:
  __start__ -> plan -> decide -> {call | done}
  call -> observe -> decide
  done -> END

Termination is decided in ``decide`` (returns ``"stop"`` or runs out of
budget). The whole machine fits in ~120 lines; the heavy lifting is in
the tools and prompts."""
from __future__ import annotations

import json
import re
from concurrent.futures import ThreadPoolExecutor
from typing import Callable, Mapping

from langgraph.graph import END, StateGraph

from agent.llm import LLM
from agent.prompts import (
    DECIDER_SYSTEM, DECIDER_USER,
    PLANNER_SYSTEM, PLANNER_USER,
    REPORTER_SYSTEM, REPORTER_USER,
)
from agent.state import AgentState
from memory.evidence import Evidence
from memory.scratchpad import Scratchpad
from tools import all_tools
from tools.base import Tool, ToolResult


_DECIDER_RE = re.compile(r"\{[^{}]*\"tool\"\s*:\s*\"([a-z]+)\"[^{}]*\}", re.S)
_VALID_TOOLS = {"whois", "dns", "shodan", "github", "wayback", "stop"}


def _parse_decider(raw: str) -> tuple[str, str]:
    """Best-effort extraction of (tool, rationale) from the model's reply.
    If anything is malformed we return ('stop', '...') so the loop
    terminates rather than spinning."""
    raw = raw.strip()
    # Try strict JSON first.
    for candidate in (raw, raw.split("```")[1] if "```" in raw else raw):
        try:
            obj = json.loads(candidate)
            tool = (obj.get("tool") or "").strip().lower()
            if tool in _VALID_TOOLS:
                return tool, str(obj.get("rationale", ""))[:200]
        except (ValueError, IndexError, AttributeError):
            continue
    # Loose regex fallback.
    m = _DECIDER_RE.search(raw)
    if m:
        tool = m.group(1).lower()
        if tool in _VALID_TOOLS:
            return tool, raw[:200]
    return "stop", "decider returned unparseable response"


def _evidence_block(rows: list[dict]) -> str:
    """Render a compact citation-ready block for the reporter prompt."""
    lines = []
    for r in rows[:80]:  # hard cap so the prompt stays small
        lines.append(
            f"- [{r['tool']}] {r['kind']} = {r['value']}  "
            f"(source: {r.get('source', '')})"
        )
    return "\n".join(lines) if lines else "(no evidence rows)"


# ----------------------------------------------------------------------
# Public factory
# ----------------------------------------------------------------------

def build_graph(
    *,
    llm: LLM,
    tools: list[Tool] | None = None,
    on_phase: Callable[[AgentState, str], None] | None = None,
):
    """Wire the LangGraph StateGraph and return the compiled runnable.

    ``on_phase`` is an optional dashboard hook called as
    ``on_phase(state, phase_label)`` at the start of each node so the
    TUI can mirror the agent's state in real time.
    """
    tools = tools or all_tools()
    tool_by_name: Mapping[str, Tool] = {t.name: t for t in tools}
    scratchpads: dict[str, Scratchpad] = {}
    # We run blocking tools through a thread pool — keeps the LangGraph
    # event loop healthy for any future async additions.
    pool = ThreadPoolExecutor(max_workers=1, thread_name_prefix="osint-tool")

    def _scratchpad_for(state: AgentState) -> Scratchpad:
        sp = scratchpads.get(state["target"])
        if sp is None:
            sp = Scratchpad(target=state["target"])
            for row in state.get("evidence", []) or []:
                sp.add_evidence([Evidence(
                    tool=row["tool"], target=row["target"], kind=row["kind"],
                    value=row["value"], source=row["source"],
                    detail=row.get("detail", ""),
                    confidence=row.get("confidence", 0.95),
                )])
            for t in state.get("tools_called", []) or []:
                sp.mark_tool_called(t)
            scratchpads[state["target"]] = sp
        sp.plan = state.get("plan", "")
        return sp

    # ---------------------------------------------- nodes ------------
    def node_plan(state: AgentState) -> dict:
        if on_phase:
            on_phase(state, "plan")
        resp = llm.chat(
            system=PLANNER_SYSTEM,
            user=PLANNER_USER.format(target=state["target"]),
            max_tokens=180,
        )
        sp = _scratchpad_for(state)
        sp.set_plan(resp.text)
        sp.append_trace(f"plan: {resp.text}")
        return {
            "plan": resp.text,
            "phase": "plan",
            "iteration": 0,
            "tools_called": [],
            "evidence": [],
            "trace": [f"plan: {resp.text}"],
            "elapsed_ms_per_tool": {},
            "last_observation": "",
        }

    def node_decide(state: AgentState) -> dict:
        if on_phase:
            on_phase(state, "decide")
        sp = _scratchpad_for(state)
        # Stop early if budget is exhausted.
        if state.get("iteration", 0) >= state.get("budget", 12):
            return {
                "phase": "done",
                "chosen_tool": "stop",
                "finish_reason": "budget_exhausted",
            }
        resp = llm.chat(
            system=DECIDER_SYSTEM,
            user=DECIDER_USER.format(scratchpad=sp.summary_for_prompt()),
            max_tokens=120,
        )
        tool, rationale = _parse_decider(resp.text)
        sp.append_trace(f"decide -> {tool}: {rationale[:100]}")
        return {
            "phase": "decide",
            "chosen_tool": tool,
            "trace": list(state.get("trace", [])) + [
                f"decide -> {tool}: {rationale[:100]}"
            ],
        }

    def node_call(state: AgentState) -> dict:
        if on_phase:
            on_phase(state, "call")
        chosen = state.get("chosen_tool") or ""
        sp = _scratchpad_for(state)
        if chosen not in tool_by_name:
            sp.append_trace(f"call: unknown tool {chosen!r}; treating as stop")
            return {
                "phase": "call",
                "chosen_tool": "stop",
                "iteration": state.get("iteration", 0) + 1,
            }
        tool = tool_by_name[chosen]
        future = pool.submit(tool.run, state["target"])
        result: ToolResult = future.result(timeout=60.0)
        sp.mark_tool_called(chosen)
        added = sp.add_evidence(result.findings)
        evidence_dump = [e.to_dict() for e in sp.evidence]
        elapsed = dict(state.get("elapsed_ms_per_tool", {}))
        elapsed[chosen] = result.elapsed_ms
        observation = (
            f"{chosen}: {len(result.findings)} findings "
            f"({added} new), elapsed {result.elapsed_ms} ms"
            + (f", error: {result.error}" if result.error else "")
        )
        sp.append_trace(f"observe: {observation}")
        return {
            "phase": "observe",
            "iteration": state.get("iteration", 0) + 1,
            "tools_called": list(sp.tools_called),
            "evidence": evidence_dump,
            "last_observation": observation,
            "trace": list(state.get("trace", [])) + [f"observe: {observation}"],
            "elapsed_ms_per_tool": elapsed,
        }

    def node_done(state: AgentState) -> dict:
        if on_phase:
            on_phase(state, "done")
        sp = _scratchpad_for(state)
        rows = state.get("evidence", []) or []
        resp = llm.chat(
            system=REPORTER_SYSTEM,
            user=REPORTER_USER.format(
                target=state["target"],
                tools_called=", ".join(sorted(state.get("tools_called", []))) or "none",
                n=len(rows),
                evidence_block=_evidence_block(rows),
            ),
            max_tokens=600,
        )
        finish = state.get("finish_reason") or (
            "covered_all_tools" if sp.coverage >= 5 else "agent_stopped"
        )
        return {
            "phase": "done",
            "final_report": resp.text,
            "finish_reason": finish,
        }

    # ---------------------------------------------- routing ----------
    def route_after_decide(state: AgentState) -> str:
        return "done" if state.get("chosen_tool") == "stop" else "call"

    def route_after_call(state: AgentState) -> str:
        # If call replaced chosen_tool with "stop" (unknown tool), exit.
        return "done" if state.get("chosen_tool") == "stop" else "decide"

    # ---------------------------------------------- graph ------------
    g = StateGraph(AgentState)
    g.add_node("plan", node_plan)
    g.add_node("decide", node_decide)
    g.add_node("call", node_call)
    g.add_node("done", node_done)
    g.set_entry_point("plan")
    g.add_edge("plan", "decide")
    g.add_conditional_edges("decide", route_after_decide,
                             {"call": "call", "done": "done"})
    g.add_conditional_edges("call", route_after_call,
                             {"decide": "decide", "done": "done"})
    g.add_edge("done", END)
    return g.compile()

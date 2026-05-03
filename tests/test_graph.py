"""End-to-end graph test with a stubbed LLM.

We feed the agent a scripted reply sequence so the test is fully
deterministic — no model required."""
from __future__ import annotations

from typing import Iterator

from agent.graph import build_graph, _parse_decider
from agent.llm import LLMResponse


class ScriptedLLM:
    """Drop-in replacement for the LLM that returns prepared responses
    in order. Used to exercise the graph without a real model."""

    def __init__(self, replies):
        self._replies: Iterator[str] = iter(replies)
        self.model = "scripted"
        self.calls: list[tuple[str, str]] = []

    def chat(self, *, system, user, max_tokens=600, temperature=0.0):
        self.calls.append((system[:30], user[:30]))
        return LLMResponse(text=next(self._replies), latency_ms=1)

    def close(self):  # pragma: no cover - parity only
        pass


class FakeTool:
    def __init__(self, name: str, findings_n: int = 1):
        self.name = name
        self._n = findings_n
        self.description = f"fake {name}"

    def run(self, target, *, timeout_s: float = 15.0):
        from memory.evidence import Evidence
        from tools.base import ToolResult
        result = ToolResult(tool=self.name, target=target, elapsed_ms=5)
        for i in range(self._n):
            result.findings.append(Evidence(
                tool=self.name, target=target,
                kind=f"{self.name}.fact",
                value=f"v{i}",
                source=f"{self.name}://{target}",
            ))
        return result


def test_decider_parsing_handles_strict_json():
    tool, rationale = _parse_decider('{"tool": "whois", "rationale": "first"}')
    assert tool == "whois"
    assert rationale.startswith("first")


def test_decider_parsing_falls_back_to_stop_on_garbage():
    tool, _ = _parse_decider("hello, I would like to look at registrar info")
    assert tool == "stop"


def test_full_loop_terminates_after_covering_tools():
    replies = [
        "plan: call all five",
        '{"tool":"whois","rationale":"start cheap"}',
        '{"tool":"dns","rationale":"confirm hosts"}',
        '{"tool":"shodan","rationale":"open ports"}',
        '{"tool":"github","rationale":"exposed configs"}',
        '{"tool":"wayback","rationale":"history"}',
        '{"tool":"stop","rationale":"covered all five"}',
        "## Briefing\nAll tools succeeded.",
    ]
    llm = ScriptedLLM(replies)
    fake_tools = [FakeTool(n, findings_n=2) for n in
                   ("whois", "dns", "shodan", "github", "wayback")]
    g = build_graph(llm=llm, tools=fake_tools)
    final = g.invoke({"target": "x.example", "budget": 8,
                       "iteration": 0, "tools_called": [], "evidence": [],
                       "trace": [], "elapsed_ms_per_tool": {}},
                      {"recursion_limit": 64})
    assert sorted(final["tools_called"]) == [
        "dns", "github", "shodan", "wayback", "whois"]
    assert len(final["evidence"]) == 10  # 5 tools × 2 findings each
    assert final["finish_reason"] in {"covered_all_tools", "agent_stopped"}
    assert "All tools succeeded" in final["final_report"]


def test_agent_stops_when_decider_returns_stop_immediately():
    replies = [
        "plan: skip everything",
        '{"tool":"stop","rationale":"early exit for test"}',
        "briefing: nothing found",
    ]
    llm = ScriptedLLM(replies)
    fake_tools = [FakeTool(n) for n in ("whois", "dns", "shodan",
                                          "github", "wayback")]
    g = build_graph(llm=llm, tools=fake_tools)
    final = g.invoke({"target": "x.example", "budget": 8,
                       "iteration": 0, "tools_called": [], "evidence": [],
                       "trace": [], "elapsed_ms_per_tool": {}})
    assert final["tools_called"] == []
    assert final["evidence"] == []


def test_budget_exhaustion_terminates_cleanly():
    """If the LLM keeps choosing tools, budget bounds the loop."""
    replies = [
        "plan",
        *[
            '{"tool":"whois","rationale":"loop"}'
            for _ in range(20)
        ],
        "briefing",
    ]
    llm = ScriptedLLM(replies)
    fake_tools = [FakeTool("whois")]
    g = build_graph(llm=llm, tools=fake_tools)
    final = g.invoke({"target": "x.example", "budget": 3,
                       "iteration": 0, "tools_called": [], "evidence": [],
                       "trace": [], "elapsed_ms_per_tool": {}})
    assert final["iteration"] == 3
    assert final["finish_reason"] == "budget_exhausted"

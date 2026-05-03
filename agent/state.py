"""LangGraph state schema.

A TypedDict — LangGraph treats this as a *state schema*, merging values
returned by each node into the running state. We keep the schema flat
on purpose: nested dataclasses cause merge ambiguity in StateGraph and
nothing here needs the structure."""
from __future__ import annotations

from typing import Any, Literal, TypedDict


Phase = Literal["plan", "call", "observe", "decide", "done"]


class AgentState(TypedDict, total=False):
    # ----- run context (set once at start) -----
    target: str
    budget: int            # max iterations
    iteration: int         # current iteration count, 0-indexed

    # ----- agent loop -----
    phase: Phase
    plan: str
    chosen_tool: str | None
    last_observation: str  # short prose summary fed back into the next prompt

    # ----- accumulators -----
    tools_called: list[str]
    evidence: list[dict[str, Any]]    # serialised Evidence rows
    trace: list[str]                   # human-readable thought log
    elapsed_ms_per_tool: dict[str, int]

    # ----- terminal -----
    final_report: str      # markdown briefing, set in the "done" node
    finish_reason: str     # "covered_all_tools" | "budget_exhausted" | "agent_stopped"

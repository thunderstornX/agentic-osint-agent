"""Typer CLI.

    osint investigate --target nist.gov
    osint tools                # list the 5 tools and what each one does
    osint version

Provider defaults to ``openrouter``; pass ``--provider nvidia`` for NIM.
The CLI tolerates ``operator_authority`` from either ``--authority`` or
the ``OSINT_OPERATOR_AUTHORITY`` env var. We refuse to run without one
because the structured report has a mandatory field for it.
"""
from __future__ import annotations

import os
import sys
import time
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.table import Table

from agent.graph import build_graph
from agent.llm import LLM, LLMError
from agent.tui.banner import render_banner
from agent.tui.dashboard import Dashboard, DashboardState
from agent.tui.report import render_briefing
from agent.tui.theme import THEME
from output.formatter import build_report, write_json_report
from output.markdown import write_markdown_briefing
from tools import all_tools


app = typer.Typer(
    add_completion=False,
    help="Agentic OSINT investigator. Five public-source tools, one disciplined ReAct loop.",
)
console = Console(theme=THEME)


@app.callback(invoke_without_command=True)
def _root(ctx: typer.Context) -> None:
    if ctx.invoked_subcommand is None:
        render_banner(target_console=console)
        console.print()
        console.print("[osint.muted]Run [/]"
                      "[osint.handle]osint --help[/]"
                      "[osint.muted] for commands.[/]")


@app.command("tools")
def cmd_tools() -> None:
    """List the available OSINT tools."""
    render_banner(target_console=console)
    t = Table(title="osint :: tools",
              border_style="osint.border", show_lines=False, padding=(0, 1))
    t.add_column("name", style="osint.muted")
    t.add_column("description")
    for tool in all_tools():
        t.add_row(f"[osint.tool.{tool.name}]{tool.name}[/]", tool.description)
    console.print(t)


@app.command("version")
def cmd_version() -> None:
    console.print("agentic-osint-agent  [osint.handle]v1.0.0[/]")


@app.command("investigate")
def cmd_investigate(
    target: str = typer.Option(..., "--target", "-t",
                               help="Domain to investigate, e.g. nist.gov"),
    provider: str = typer.Option("openrouter", "--provider",
                                  help="openrouter | nvidia"),
    model: Optional[str] = typer.Option(None, "--model",
                                         help="Override the default free-tier model"),
    budget: int = typer.Option(12, "--budget",
                                help="Max ReAct iterations (1-24)",
                                min=1, max=24),
    output_dir: Path = typer.Option(Path("results"), "--output-dir",
                                     help="Directory for JSON+MD outputs"),
    authority: Optional[str] = typer.Option(None, "--authority",
                                             help="Operator authority statement (required)"),
    no_dashboard: bool = typer.Option(False, "--no-dashboard",
                                       help="Disable the live dashboard (CI mode)"),
) -> None:
    """Run the ReAct investigation loop against a single target."""

    auth = authority or os.getenv("OSINT_OPERATOR_AUTHORITY") or ""
    if not auth.strip():
        console.print(
            "[osint.error]error:[/] no operator authority supplied — "
            "pass [osint.handle]--authority \"<reason>\"[/] or set "
            "[osint.handle]OSINT_OPERATOR_AUTHORITY[/]."
        )
        console.print(
            "[osint.muted]This field documents *why* you are allowed to "
            "investigate this target. It is required.[/]"
        )
        raise typer.Exit(code=2)

    render_banner(target_console=console)
    console.print(
        f"[osint.muted]target [/][osint.heading]{target}[/]  "
        f"[osint.muted]provider [/][osint.tagline]{provider}[/]  "
        f"[osint.muted]budget [/][osint.handle]{budget}[/]"
    )

    try:
        llm = LLM(provider=provider, model=model)  # type: ignore[arg-type]
    except LLMError as exc:
        console.print(f"[osint.error]error:[/] {exc}")
        raise typer.Exit(code=2)

    state = DashboardState(target=target, provider=provider,
                            model=llm.model, budget=budget)

    dash: Dashboard | None = None
    if not no_dashboard:
        dash = Dashboard(state, console=console)

    def on_phase(agent_state, phase: str) -> None:
        state.iteration = agent_state.get("iteration", 0)
        state.current_phase = phase
        if phase == "call":
            state.current_tool = agent_state.get("chosen_tool")
            tool = state.current_tool or "?"
            state.note(f"  [osint.call]→ call[/]  {tool}")
        elif phase == "decide":
            state.current_tool = None
            state.note("  [osint.decide]· decide[/]")
        elif phase == "plan":
            state.note("  [osint.plan]· plan[/]")
        elif phase == "done":
            state.note("  [osint.done]✓ done[/]")
        # update tool counters from latest evidence
        ev = agent_state.get("evidence", []) or []
        per_tool: dict[str, int] = {}
        for e in ev:
            per_tool[e["tool"]] = per_tool.get(e["tool"], 0) + 1
        for tool_name, count in per_tool.items():
            state.tool_findings[tool_name] = count
        for tool_name in agent_state.get("tools_called", []) or []:
            state.tool_calls[tool_name] = max(1, state.tool_calls.get(tool_name, 0))
        if dash is not None:
            try:
                dash.render_into(_live)  # noqa: F821 — assigned just below
            except Exception:  # pragma: no cover - never crash the run
                pass

    started = time.monotonic()
    initial: dict = {
        "target": target,
        "budget": budget,
        "iteration": 0,
        "tools_called": [],
        "evidence": [],
        "trace": [],
        "elapsed_ms_per_tool": {},
    }
    graph = build_graph(llm=llm, on_phase=on_phase)

    if dash is not None:
        with dash.live() as _live:  # noqa: F841 — closure name above
            try:
                final_state = graph.invoke(initial, {"recursion_limit": budget * 4 + 8})
            except Exception as exc:  # pragma: no cover
                console.print(f"[osint.error]agent error:[/] {exc}")
                raise typer.Exit(code=1)
    else:
        # CI / headless mode: still run the loop without the live UI.
        _live = None  # noqa: F841
        final_state = graph.invoke(initial, {"recursion_limit": budget * 4 + 8})

    elapsed = time.monotonic() - started
    llm.close()

    report = build_report(
        target=target,
        provider=provider,
        model=llm.model,
        budget=budget,
        iterations=final_state.get("iteration", 0),
        elapsed_s=elapsed,
        operator_authority=auth.strip(),
        evidence=final_state.get("evidence", []),
        trace=final_state.get("trace", []),
        tools_called=final_state.get("tools_called", []),
        elapsed_ms_per_tool=final_state.get("elapsed_ms_per_tool", {}),
        final_report=final_state.get("final_report", ""),
        finish_reason=final_state.get("finish_reason", "agent_stopped"),
    )
    output_dir = Path(output_dir)
    safe = target.replace("/", "_").replace(":", "_")
    json_path = output_dir / f"{safe}.json"
    md_path = output_dir / f"{safe}.md"
    write_json_report(json_path, report)
    write_markdown_briefing(md_path, report)

    console.print()
    # render the post-run briefing
    per_tool: dict[str, dict] = {}
    for ev in report["evidence"]:
        bucket = per_tool.setdefault(ev["tool"], {"calls": 1, "findings": 0,
                                                    "first_source": ev.get("source", "")})
        bucket["findings"] += 1
    for tool in report["summary"]["tools_called"]:
        per_tool.setdefault(tool, {"calls": 1, "findings": 0, "first_source": ""})
    render_briefing(
        target=target,
        provider=provider,
        model=llm.model,
        elapsed_s=elapsed,
        iterations=report["run"]["iterations"],
        coverage=report["summary"]["coverage"],
        findings=report["summary"]["evidence_count"],
        per_tool=per_tool,
        console=console,
    )
    console.print()
    console.print(f"[osint.muted]wrote[/] [osint.handle]{json_path}[/]")
    console.print(f"[osint.muted]wrote[/] [osint.handle]{md_path}[/]")


if __name__ == "__main__":  # pragma: no cover
    app()

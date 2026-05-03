"""Post-run briefing — the *quiet* sibling of the live dashboard.

Renders a compact summary panel + per-tool evidence table, suitable for
paper figures and end-of-run terminal output. Keeps no async state."""
from __future__ import annotations

from typing import Mapping, Sequence

from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from agent.tui.theme import THEME


_TOOL_ORDER = ("whois", "dns", "shodan", "github", "wayback")
_TOOL_LABELS = {
    "whois":   "WHOIS",
    "dns":     "DNS",
    "shodan":  "Shodan IDB",
    "github":  "GitHub Dork",
    "wayback": "Wayback CDX",
}


def _verdict(coverage: int, findings: int) -> Text:
    """Single-line read on how the run went.

    The thresholds are deliberate: 5/5 tool categories means the agent
    actually *exercised* its plan; <5 means the agent gave up early or
    one tool errored. Findings count is a loose signal — some clean
    targets simply have no exposed config files. We say so."""
    if coverage == 5 and findings >= 5:
        return Text("  thorough sweep — broad coverage, plenty of evidence",
                    style="osint.found")
    if coverage == 5:
        return Text(
            "  full coverage — every tool exercised, evidence sparse "
            "(target may simply be tidy)",
            style="osint.tagline")
    if coverage >= 3:
        return Text("  partial coverage — agent stopped before exhausting "
                    "the toolset", style="osint.empty")
    return Text("  shallow run — investigate logs before trusting the "
                "report", style="osint.error")


def render_briefing(
    *,
    target: str,
    provider: str,
    model: str,
    elapsed_s: float,
    iterations: int,
    coverage: int,
    findings: int,
    per_tool: Mapping[str, dict],
    console: Console | None = None,
) -> None:
    c = console or Console(theme=THEME)

    # ---- summary panel ------------------------------------------------
    summary = Text()
    summary.append("target   ", style="osint.muted")
    summary.append(target + "\n", style="osint.heading")
    summary.append("model    ", style="osint.muted")
    summary.append(f"{provider}/{model}\n", style="osint.tagline")
    summary.append("budget   ", style="osint.muted")
    summary.append(f"{iterations} iterations · {elapsed_s:.1f}s wall-clock\n",
                   style="osint.handle")
    summary.append("coverage ", style="osint.muted")
    summary.append(f"{coverage}/5 tool categories · {findings} evidence "
                   f"items\n", style="osint.handle")
    summary.append(_verdict(coverage, findings))

    panel = Panel(
        summary,
        title="[osint.heading]investigation briefing[/]",
        border_style="osint.border",
        padding=(0, 2),
    )

    # ---- per-tool table ----------------------------------------------
    t = Table(
        show_header=True,
        header_style="osint.heading",
        border_style="osint.border",
        padding=(0, 1),
    )
    t.add_column("tool", style="osint.muted")
    t.add_column("calls", justify="right")
    t.add_column("findings", justify="right")
    t.add_column("first source")
    for key in _TOOL_ORDER:
        info = per_tool.get(key, {"calls": 0, "findings": 0, "first_source": ""})
        label = f"[osint.tool.{key}]{_TOOL_LABELS[key]}[/]"
        calls = info.get("calls", 0)
        found = info.get("findings", 0)
        src = info.get("first_source", "") or ""
        f_style = ("osint.found" if found else
                   "osint.empty" if calls else "osint.muted")
        t.add_row(
            label,
            f"[osint.handle]{calls}[/]" if calls else f"[osint.muted]0[/]",
            f"[{f_style}]{found}[/]",
            f"[osint.muted]{src[:64]}[/]",
        )

    c.print(Group(panel, Text(""), t))

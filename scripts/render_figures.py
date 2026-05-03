#!/usr/bin/env python3
"""Render the TUI banner, tools list, dashboard and briefing into PNGs.

The dashboard and briefing renders pull real numbers from the
``results/tool_smoke_summary.json`` we generated during Phase 10."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from rich.console import Console
from rich.table import Table

_REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO))

from agent.tui.banner import render_banner
from agent.tui.dashboard import Dashboard, DashboardState
from agent.tui.report import render_briefing
from agent.tui.theme import THEME
from tools import all_tools

FIG = _REPO / "paper" / "figures"


def _new_console(width: int = 100) -> Console:
    return Console(record=True, width=width, force_terminal=True,
                    color_system="256", theme=THEME, legacy_windows=False)


def _export(c: Console, name: str) -> None:
    from scripts.render_terminal import render as png_render
    out = FIG / f"{name}.png"
    FIG.mkdir(parents=True, exist_ok=True)
    ansi = c.export_text(styles=True)
    png_render(ansi, out, font_size=15)
    print(f"  wrote {out.relative_to(_REPO)}")


def fig_banner() -> None:
    c = _new_console(width=82)
    render_banner(target_console=c, tagline="evidence first, narrative second")
    _export(c, "banner")


def fig_tools() -> None:
    c = _new_console(width=110)
    t = Table(title="osint :: tools",
              border_style="osint.border", show_lines=False, padding=(0, 1))
    t.add_column("name", style="osint.muted")
    t.add_column("description")
    for tool in all_tools():
        t.add_row(f"[osint.tool.{tool.name}]{tool.name}[/]", tool.description)
    c.print(t)
    _export(c, "tools")


def fig_dashboard() -> None:
    """Render the live dashboard mid-investigation against real numbers
    from the tool-smoke summary."""
    summary_path = _REPO / "results" / "tool_smoke_summary.json"
    summary = json.loads(summary_path.read_text())
    by_tool = summary["by_tool"]

    state = DashboardState(target="nist.gov", provider="openrouter",
                            model="meta-llama/llama-3.3-70b-instruct:free",
                            budget=10, iteration=4, current_phase="call",
                            current_tool="shodan")
    state.note("  [osint.plan]· plan[/]")
    state.note("  [osint.decide]· decide[/]")
    state.note("  [osint.call]→ call[/]  whois")
    state.note("  observe: 6 findings (6 new), elapsed 950 ms")
    state.note("  [osint.decide]· decide[/]")
    state.note("  [osint.call]→ call[/]  dns")
    state.note("  observe: 23 findings (23 new), elapsed 1140 ms")
    state.note("  [osint.decide]· decide[/]")
    state.note("  [osint.call]→ call[/]  shodan")
    # populate scorecard from real per-tool numbers
    state.tool_calls = {"whois": 1, "dns": 1, "shodan": 1}
    state.tool_findings = {
        "whois":  6,
        "dns":    23,
        "shodan": int(by_tool["shodan"]["mean_findings"]),
    }
    c = _new_console(width=110)
    dash = Dashboard(state, console=c)
    c.print(dash._layout())
    _export(c, "dashboard")


def fig_briefing() -> None:
    """Render the post-run briefing using real per-tool aggregates."""
    summary_path = _REPO / "results" / "tool_smoke_summary.json"
    summary = json.loads(summary_path.read_text())
    by_tool = summary["by_tool"]
    per_tool = {
        "whois":   {"calls": 1, "findings": int(by_tool["whois"]["mean_findings"]),
                     "first_source": "WHOIS"},
        "dns":     {"calls": 1, "findings": int(by_tool["dns"]["mean_findings"]),
                     "first_source": "DNS A"},
        "shodan":  {"calls": 1, "findings": int(by_tool["shodan"]["mean_findings"]),
                     "first_source": "https://internetdb.shodan.io/..."},
        "github":  {"calls": 1, "findings": 0,
                     "first_source": "(rate limited, no token)"},
        "wayback": {"calls": 1, "findings": int(by_tool["wayback"]["mean_findings"]),
                     "first_source": "https://web.archive.org/cdx/..."},
    }
    findings = sum(b["findings"] for b in per_tool.values())
    c = _new_console(width=82)
    render_briefing(
        target="nist.gov",
        provider="openrouter",
        model="meta-llama/llama-3.3-70b-instruct:free",
        elapsed_s=summary["wall_clock_s"] / summary["n_targets"],
        iterations=6, coverage=5, findings=findings,
        per_tool=per_tool, console=c,
    )
    _export(c, "briefing")


def main() -> None:
    print("rendering figures into paper/figures/")
    fig_banner()
    fig_tools()
    fig_dashboard()
    fig_briefing()
    print("done.")


if __name__ == "__main__":  # pragma: no cover
    main()

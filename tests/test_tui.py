"""TUI smoke tests."""
from __future__ import annotations

from io import StringIO

from rich.console import Console

from agent.tui.banner import BANNER, render_banner
from agent.tui.dashboard import Dashboard, DashboardState
from agent.tui.report import render_briefing
from agent.tui.theme import THEME


def _captured(width: int = 100) -> Console:
    return Console(file=StringIO(), width=width, theme=THEME,
                    force_terminal=True, color_system="256",
                    legacy_windows=False)


def test_banner_static_text_contains_signature():
    assert "ORCID" in BANNER
    assert "0009-0007-2787-943X" in BANNER
    # the chunky letterforms have spaces between letters
    assert "L A N G G R A P H" in BANNER
    assert "R E A C T" in BANNER


def test_render_banner_does_not_crash():
    c = _captured()
    render_banner(target_console=c)
    out = c.file.getvalue()
    assert "agentic-osint-agent" in out


def test_dashboard_records_phases_and_findings():
    state = DashboardState(target="x.example", provider="openrouter",
                            model="m", budget=4)
    state.note("hello world")
    state.record_call("whois", findings=2)
    state.record_call("dns", findings=3)
    assert state.tool_calls["whois"] == 1
    assert state.tool_findings["dns"] == 3


def test_dashboard_truncates_log_lines():
    state = DashboardState(target="x.example", provider="op", model="m")
    for i in range(40):
        state.note(f"line {i}")
    assert len(state.log_lines) == 14


def test_render_briefing_smoke():
    c = _captured()
    render_briefing(
        target="x.example", provider="openrouter", model="m",
        elapsed_s=12.0, iterations=4, coverage=5, findings=10,
        per_tool={
            "whois":   {"calls": 1, "findings": 3, "first_source": "WHOIS"},
            "dns":     {"calls": 1, "findings": 4, "first_source": "DNS A"},
            "shodan":  {"calls": 1, "findings": 2, "first_source": "https://internetdb..."},
            "github":  {"calls": 1, "findings": 0, "first_source": ""},
            "wayback": {"calls": 1, "findings": 1, "first_source": "https://web.archive..."},
        },
        console=c,
    )
    out = c.file.getvalue()
    assert "investigation briefing" in out
    assert "WHOIS" in out

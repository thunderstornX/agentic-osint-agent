"""Rich-powered TUI: detective-magnifier banner, live investigation
dashboard, and post-run briefing renderer.

Kept self-contained so the rest of the repo can be tested without spinning
up a Console.
"""
from agent.tui.banner import render_banner, BANNER
from agent.tui.theme import THEME
from agent.tui.dashboard import Dashboard, DashboardState
from agent.tui.report import render_briefing

__all__ = [
    "render_banner",
    "BANNER",
    "THEME",
    "Dashboard",
    "DashboardState",
    "render_briefing",
]

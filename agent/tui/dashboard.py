"""Live investigation dashboard.

Three panels in one Layout:
  - top: progress (iterations consumed / budget) + current target
  - middle-left: thought-action-observation log, scrolling
  - middle-right: tools-called scorecard with finding counts

The dashboard is *manually driven*: callers update the DashboardState and
then call ``render_into(live)``. We do not start the Live's auto-refresh
because the agent runs async and we don't want a background thread
fighting with asyncio.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable

from rich.console import Console, Group, RenderableType
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TextColumn,
    TimeElapsedColumn,
)
from rich.table import Table
from rich.text import Text

from agent.tui.theme import THEME


# Tool keys we render in the scorecard. Order is the canonical
# "investigation cycle" order; matches the one the agent prompt uses.
_TOOL_ORDER = ("whois", "dns", "shodan", "github", "wayback")
_TOOL_LABELS = {
    "whois":   "WHOIS",
    "dns":     "DNS",
    "shodan":  "Shodan IDB",
    "github":  "GitHub Dork",
    "wayback": "Wayback CDX",
}


@dataclass
class DashboardState:
    """All the numbers the dashboard needs.

    ``log_lines`` keeps the most recent ~14 entries — anything older is
    dropped so the panel stays tidy on smaller terminals.
    """
    target: str
    provider: str
    model: str
    budget: int = 12
    iteration: int = 0
    current_phase: str = "idle"
    current_tool: str | None = None
    log_lines: list[Text] = field(default_factory=list)
    tool_calls: dict[str, int] = field(default_factory=dict)
    tool_findings: dict[str, int] = field(default_factory=dict)

    def note(self, line: Text | str) -> None:
        if isinstance(line, str):
            # Parse Rich markup tags so the dashboard renders coloured
            # phase badges instead of literal "[osint.plan]" strings.
            line = Text.from_markup(line)
        self.log_lines.append(line)
        if len(self.log_lines) > 14:
            self.log_lines = self.log_lines[-14:]

    def record_call(self, tool: str, *, findings: int) -> None:
        self.tool_calls[tool] = self.tool_calls.get(tool, 0) + 1
        self.tool_findings[tool] = self.tool_findings.get(tool, 0) + findings


class Dashboard:
    """Wraps a DashboardState into a Live-renderable Layout."""

    def __init__(self, state: DashboardState, *, console: Console | None = None):
        self.state = state
        self.console = console or Console(theme=THEME)
        self._progress = Progress(
            SpinnerColumn(style="osint.sweep"),
            TextColumn("[osint.heading]{task.description}[/]"),
            BarColumn(complete_style="osint.lens", finished_style="osint.done"),
            TextColumn("[osint.muted]iter {task.completed:>2}/{task.total} ·[/]"),
            TimeElapsedColumn(),
            console=self.console,
            transient=False,
        )
        self._task_id = self._progress.add_task(
            description=f"investigating  {state.target}",
            total=state.budget,
        )

    # -------------------------------------------------- public lifecycle --
    def live(self) -> Live:
        return Live(
            self._layout(),
            console=self.console,
            refresh_per_second=8,
            auto_refresh=False,
        )

    def render_into(self, live: Live) -> None:
        """Refresh both progress + layout against current state."""
        self._progress.update(self._task_id, completed=self.state.iteration)
        live.update(self._layout(), refresh=True)

    # ---------------------------------------------------------- panels --
    def _phase_badge(self) -> Text:
        phase = self.state.current_phase
        style = {
            "plan":    "osint.plan",
            "call":    "osint.call",
            "observe": "osint.observe",
            "decide":  "osint.decide",
            "done":    "osint.done",
        }.get(phase, "osint.muted")
        return Text(f"  {phase:<8}", style=style)

    def _activity(self) -> Panel:
        head = Text()
        head.append("target  ", style="osint.muted")
        head.append(self.state.target + "\n", style="osint.heading")
        head.append("model   ", style="osint.muted")
        head.append(f"{self.state.provider}/{self.state.model}\n",
                    style="osint.tagline")
        head.append("phase   ", style="osint.muted")
        head.append(self.state.current_phase, style="osint.heading")
        if self.state.current_tool:
            head.append("  →  ", style="osint.muted")
            head.append(self.state.current_tool, style="osint.handle")

        body = Group(*self.state.log_lines) if self.state.log_lines else Text(
            "  (waiting on first reasoning step)", style="osint.muted")

        return Panel(
            Group(head, Text(""), body),
            title="[osint.heading]activity[/]",
            border_style="osint.border",
            padding=(0, 1),
        )

    def _scorecard(self) -> Panel:
        t = Table(
            show_header=True,
            header_style="osint.heading",
            border_style="osint.border",
            padding=(0, 1),
        )
        t.add_column("tool",     style="osint.muted")
        t.add_column("calls",   justify="right")
        t.add_column("findings", justify="right")
        for key in _TOOL_ORDER:
            calls = self.state.tool_calls.get(key, 0)
            found = self.state.tool_findings.get(key, 0)
            label_style = f"osint.tool.{key}"
            calls_style = "osint.handle" if calls else "osint.muted"
            f_style = ("osint.found" if found else
                       "osint.empty" if calls else "osint.muted")
            t.add_row(
                f"[{label_style}]{_TOOL_LABELS[key]}[/]",
                f"[{calls_style}]{calls}[/]",
                f"[{f_style}]{found}[/]",
            )
        return Panel(t, title="[osint.heading]tool scorecard[/]",
                     border_style="osint.border", padding=(0, 1))

    def _layout(self) -> RenderableType:
        layout = Layout()
        layout.split_column(
            Layout(self._progress.get_renderable(), name="top", size=3),
            Layout(name="body"),
        )
        layout["body"].split_row(
            Layout(self._activity(), ratio=2),
            Layout(self._scorecard(), ratio=1),
        )
        return layout

"""The detective-magnifier banner that prints on every CLI invocation.

The figure on the right is a stylised magnifying glass mid-sweep over a
target. The agent is the lens; the public sources are what falls under
it. The banner is hand-laid into a strict ~76-column budget because Rich
will silently wrap a Panel beyond ~78 cols on most terminals and break
the artwork — learnt that the hard way on the spider banner in the
sibling red-team toolkit.
"""
from __future__ import annotations

import random
from rich.align import Align
from rich.console import Console, Group
from rich.panel import Panel
from rich.text import Text

from agent.tui.theme import THEME


_TAGLINES = [
    "follow the threads, not the targets",
    "five public lenses, one disciplined loop",
    "plan · call · observe · decide",
    "the agent is the lens, not the target",
    "every finding ships with a citation",
    "passive recon, deliberate cadence",
    "evidence first, narrative second",
]


# 76-col content budget. Each section is hand-aligned. Do not autoformat.
BANNER = r"""
   ___  ____ ___ _   _ _____                  . . . . . .
  / _ \/ ___|_ _| \ | |_   _|                ·             ·
 | | | \___ \| ||  \| | | |                 ·    .--.       ·
 | |_| |___) | || |\  | | |                 ·   /    \      ·
  \___/|____/___|_| \_| |_|                  · |  ◯   |    ·
                                              ·  \    /    ·
       a g e n t i c   o s i n t                  '--'\\
                                                       \\
            a g e n t                                   \\__
                                                          \__

         L A N G G R A P H  ·  R E A C T  ·  5   T O O L S
                  plan  ·  call  ·  observe  ·  decide

         ~ AMB · ORCID 0009-0007-2787-943X · v1.0 · 2026 ~
"""


def _colourise(raw: str) -> Text:
    """Apply theme styles per character. Cheap, readable, no regex magic."""
    out = Text()
    for line in raw.splitlines():
        styled = Text()
        for ch in line:
            if ch in "_/\\|()":
                styled.append(ch, style="osint.title")
            elif ch in "◯":
                styled.append(ch, style="osint.lens")
            elif ch in ".·":
                styled.append(ch, style="osint.sweep")
            elif ch == "~":
                styled.append(ch, style="osint.muted")
            elif ch == "'":
                styled.append(ch, style="osint.handle")
            elif ch == "-":
                styled.append(ch, style="osint.handle")
            else:
                styled.append(ch, style="osint.tagline")
        out.append(styled)
        out.append("\n")
    return out


def render_banner(*, target_console: Console | None = None,
                  tagline: str | None = None) -> None:
    """Print the banner. Caller-supplied console wins so tests can capture
    it; otherwise we make a fresh themed Console."""
    c = target_console or Console(theme=THEME)
    body = _colourise(BANNER.strip("\n"))
    chosen = tagline or random.choice(_TAGLINES)  # nosec B311 -- cosmetic only
    sub = Text("\n  " + chosen + "\n", style="osint.tagline", justify="center")
    panel = Panel(
        Group(body, sub),
        border_style="osint.border",
        padding=(0, 2),
        title="[osint.title]agentic-osint-agent[/]",
        subtitle="[osint.muted]passive recon · public sources only[/]",
    )
    c.print(Align.center(panel))


def render_compact_banner(target_console: Console | None = None) -> None:
    """One-liner for narrow terminals or downstream embedding."""
    c = target_console or Console(theme=THEME)
    c.print(
        "[osint.title]osint[/]  "
        "[osint.muted]·[/]  "
        "[osint.tagline]LangGraph ReAct investigator[/]  "
        "[osint.muted]·[/]  "
        "[osint.handle]v1.0[/]"
    )

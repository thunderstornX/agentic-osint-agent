"""Rich theme used everywhere we print.

Sticking to ANSI-16 so the colours behave inside tmux, screen, and SSH
sessions on whatever terminal you happen to land in. Old lab habit, good
lab habit.
"""
from __future__ import annotations

from rich.theme import Theme

THEME = Theme(
    {
        # --- structure ---
        "osint.title":   "bold bright_cyan",
        "osint.tagline": "italic bright_white",
        "osint.muted":   "grey50",
        "osint.border":  "cyan",
        "osint.heading": "bold bright_white",
        "osint.dim":     "grey50",

        # --- the magnifying glass + sonar motif ---
        "osint.lens":    "bold bright_yellow",
        "osint.handle":  "yellow",
        "osint.sweep":   "bright_blue",
        "osint.thread":  "magenta",

        # --- agent loop states ---
        "osint.plan":    "bold bright_blue",
        "osint.call":    "bold bright_yellow",
        "osint.observe": "bright_white",
        "osint.decide":  "bold bright_magenta",
        "osint.done":    "bold bright_green",

        # --- evidence outcomes ---
        "osint.found":     "bold bright_green",
        "osint.empty":     "yellow",
        "osint.error":     "bold bright_red",
        "osint.skipped":   "grey50",

        # --- per-tool badges (one colour per tool, easier to scan) ---
        "osint.tool.whois":   "bright_cyan",
        "osint.tool.dns":     "bright_blue",
        "osint.tool.shodan":  "bright_red",
        "osint.tool.github":  "bright_magenta",
        "osint.tool.wayback": "bright_yellow",
    }
)

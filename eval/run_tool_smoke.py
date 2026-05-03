#!/usr/bin/env python3
"""Run all five tools against the 20 evaluation targets and write a CSV.

This is the *tool-only* eval — no LLM in the loop. Useful as a real,
reproducible baseline that measures:

  - tool success rate (did we get a non-error response?)
  - tool wall-clock latency
  - findings count per tool per target
  - per-target overall coverage

The agent eval (with the LLM in the loop) is in `run_eval.py`.

Outputs:
  results/tool_smoke.csv       — one row per (target, tool)
  results/tool_smoke_summary.json — aggregates
"""
from __future__ import annotations

import csv
import json
import sys
import time
from pathlib import Path

# Make the repo importable when run from anywhere.
_REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO))

from rich.console import Console
from rich.progress import (
    BarColumn, Progress, SpinnerColumn, TextColumn, TimeElapsedColumn,
)

from agent.tui.theme import THEME
from tools import all_tools


def main() -> None:
    console = Console(theme=THEME)
    console.rule("[osint.title]osint :: tool smoke eval[/]")

    targets_path = _REPO / "eval" / "test_targets.json"
    targets = json.loads(targets_path.read_text())["targets"]
    out_csv = _REPO / "results" / "tool_smoke.csv"
    out_summary = _REPO / "results" / "tool_smoke_summary.json"
    out_csv.parent.mkdir(parents=True, exist_ok=True)

    tools = all_tools()

    rows: list[dict] = []
    started = time.monotonic()
    with Progress(
        SpinnerColumn(style="osint.sweep"),
        TextColumn("[osint.heading]{task.description}[/]"),
        BarColumn(complete_style="osint.lens", finished_style="osint.done"),
        TextColumn("[osint.muted]{task.completed:>2}/{task.total}[/]"),
        TimeElapsedColumn(),
        console=console,
    ) as progress:
        task = progress.add_task(description="probing 20 targets",
                                  total=len(targets) * len(tools))
        for entry in targets:
            target = entry["target"]
            cat = entry["category"]
            for tool in tools:
                t0 = time.monotonic()
                res = tool.run(target, timeout_s=30.0)
                elapsed = time.monotonic() - t0
                rows.append({
                    "target": target,
                    "category": cat,
                    "tool": tool.name,
                    "ok": res.ok,
                    "error": res.error or "",
                    "findings": len(res.findings),
                    "elapsed_s": round(elapsed, 2),
                })
                progress.update(task, advance=1,
                                description=f"{target} :: {tool.name}")

    elapsed_total = time.monotonic() - started

    # ---- write CSV ---------------------------------------------------
    fieldnames = ["target", "category", "tool", "ok", "error",
                  "findings", "elapsed_s"]
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow(r)

    # ---- summary -----------------------------------------------------
    by_tool: dict[str, dict] = {}
    for r in rows:
        b = by_tool.setdefault(r["tool"], {
            "calls": 0, "ok": 0, "findings": 0, "latency_s_total": 0.0,
        })
        b["calls"] += 1
        b["ok"] += int(r["ok"])
        b["findings"] += r["findings"]
        b["latency_s_total"] += r["elapsed_s"]
    for k, v in by_tool.items():
        v["success_rate"] = round(v["ok"] / max(v["calls"], 1), 3)
        v["mean_latency_s"] = round(v["latency_s_total"] / max(v["calls"], 1), 2)
        v["mean_findings"] = round(v["findings"] / max(v["calls"], 1), 2)
        del v["latency_s_total"]

    by_target: dict[str, dict] = {}
    for r in rows:
        b = by_target.setdefault(r["target"], {
            "category": r["category"], "tools_ok": 0,
            "tools_called": 0, "findings": 0,
        })
        b["tools_called"] += 1
        b["tools_ok"] += int(r["ok"])
        b["findings"] += r["findings"]

    summary = {
        "n_targets": len(targets),
        "n_tools": len(tools),
        "total_runs": len(rows),
        "wall_clock_s": round(elapsed_total, 1),
        "by_tool": by_tool,
        "by_target": by_target,
    }
    out_summary.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    console.rule("[osint.done]done[/]")
    console.print(f"  wrote [osint.handle]{out_csv.relative_to(_REPO)}[/]")
    console.print(f"  wrote [osint.handle]{out_summary.relative_to(_REPO)}[/]")
    console.print(f"  wall-clock: [osint.handle]{elapsed_total:.1f}s[/]")
    console.print(f"  successful runs: [osint.found]"
                   f"{sum(1 for r in rows if r['ok'])}/{len(rows)}[/]")


if __name__ == "__main__":
    main()

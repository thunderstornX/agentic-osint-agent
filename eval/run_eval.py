#!/usr/bin/env python3
"""Run the full agent against the 20 evaluation targets.

Requires a provider key (OpenRouter or NVIDIA NIM). Each target gets a
fresh agent run with the configured budget; results are written as
JSON+MD per target plus a summary CSV.

The metrics we capture per target:

  iterations       — how many ReAct steps the agent consumed
  coverage         — how many of the 5 tool categories were called
  evidence_count   — total evidence rows accumulated
  hallucination    — fraction of claims in final_report that do NOT cite
                      a known tool tag (whois|dns|shodan|github|wayback)
  elapsed_s        — wall-clock for the whole investigation
  finish_reason    — covered_all_tools | budget_exhausted | agent_stopped

These are the same metrics quoted in the paper.
"""
from __future__ import annotations

import csv
import json
import os
import re
import sys
import time
from pathlib import Path

_REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO))

import typer
from rich.console import Console

from agent.graph import build_graph
from agent.llm import LLM, LLMError
from agent.tui.theme import THEME
from output.formatter import build_report, write_json_report
from output.markdown import write_markdown_briefing


app = typer.Typer(add_completion=False)
console = Console(theme=THEME)


_TOOL_TAGS = ("whois", "dns", "shodan", "github", "wayback")
_TAG_REGEXES = [re.compile(rf"\b{t}\b", re.I) for t in _TOOL_TAGS]


def _hallucination_rate(final_report: str) -> float:
    """Loose proxy: fraction of sentences in the briefing that DON'T
    mention one of the five tools by name. Real hallucination detection
    needs a human-in-the-loop review; this is an automated signal."""
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", final_report)
                  if s.strip()]
    if not sentences:
        return 0.0
    grounded = 0
    for s in sentences:
        if any(rx.search(s) for rx in _TAG_REGEXES):
            grounded += 1
    return round(1.0 - grounded / len(sentences), 3)


@app.command()
def run(
    provider: str = typer.Option("openrouter", "--provider"),
    model: str = typer.Option(None, "--model"),
    budget: int = typer.Option(10, "--budget"),
    output_dir: Path = typer.Option(_REPO / "results" / "eval",
                                      "--output-dir"),
    limit: int = typer.Option(0, "--limit",
                                help="Stop after N targets (0 = all)"),
    authority: str = typer.Option(
        "Public-interest research; targets are .gov, .edu, large NGOs, "
        "or RFC-reserved domains; passive sources only.",
        "--authority"),
) -> None:
    targets_path = _REPO / "eval" / "test_targets.json"
    targets = json.loads(targets_path.read_text())["targets"]
    if limit and limit > 0:
        targets = targets[:limit]

    output_dir.mkdir(parents=True, exist_ok=True)
    csv_path = _REPO / "results" / "eval_results.csv"

    try:
        llm = LLM(provider=provider, model=model)
    except LLMError as exc:
        console.print(f"[osint.error]error:[/] {exc}")
        raise typer.Exit(2)

    graph = build_graph(llm=llm)

    fieldnames = [
        "target", "category", "iterations", "coverage", "evidence_count",
        "hallucination_rate", "finish_reason", "elapsed_s",
    ]
    rows: list[dict] = []
    started_all = time.monotonic()
    for entry in targets:
        target = entry["target"]
        cat = entry["category"]
        console.rule(f"[osint.title]{target}[/]")
        t0 = time.monotonic()
        try:
            final = graph.invoke(
                {"target": target, "budget": budget,
                 "iteration": 0, "tools_called": [], "evidence": [],
                 "trace": [], "elapsed_ms_per_tool": {}},
                {"recursion_limit": budget * 4 + 8},
            )
        except Exception as exc:  # pragma: no cover - resilient eval
            console.print(f"  [osint.error]agent error:[/] {exc}")
            continue
        elapsed = time.monotonic() - t0

        report = build_report(
            target=target, provider=provider, model=llm.model,
            budget=budget,
            iterations=final.get("iteration", 0),
            elapsed_s=elapsed, operator_authority=authority,
            evidence=final.get("evidence", []),
            trace=final.get("trace", []),
            tools_called=final.get("tools_called", []),
            elapsed_ms_per_tool=final.get("elapsed_ms_per_tool", {}),
            final_report=final.get("final_report", ""),
            finish_reason=final.get("finish_reason", "agent_stopped"),
        )
        safe = target.replace("/", "_")
        write_json_report(output_dir / f"{safe}.json", report)
        write_markdown_briefing(output_dir / f"{safe}.md", report)

        row = {
            "target": target, "category": cat,
            "iterations": report["run"]["iterations"],
            "coverage": report["summary"]["coverage"],
            "evidence_count": report["summary"]["evidence_count"],
            "hallucination_rate": _hallucination_rate(
                report["final_report"]),
            "finish_reason": report["summary"]["finish_reason"],
            "elapsed_s": round(elapsed, 1),
        }
        rows.append(row)
        console.print(
            f"  [osint.found]{row['evidence_count']} findings[/]  "
            f"coverage [osint.handle]{row['coverage']}/5[/]  "
            f"halluc [osint.empty]{row['hallucination_rate']}[/]  "
            f"{row['elapsed_s']}s")

    llm.close()
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow(r)
    console.rule("[osint.done]eval done[/]")
    console.print(f"wrote [osint.handle]{csv_path.relative_to(_REPO)}[/]")
    console.print(f"per-target reports in "
                   f"[osint.handle]{output_dir.relative_to(_REPO)}/[/]")
    console.print(
        f"total wall-clock: [osint.handle]"
        f"{time.monotonic() - started_all:.1f}s[/]"
    )


if __name__ == "__main__":  # pragma: no cover
    app()

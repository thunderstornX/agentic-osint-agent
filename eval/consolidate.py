#!/usr/bin/env python3
"""Consolidate per-target eval JSONs into a single CSV + summary.

Reads ``results/eval/*.json``, computes the same per-target metrics
``run_eval.py`` reports inline, and writes:

  results/eval_results.csv         — one row per target
  results/eval_summary.json        — aggregate numbers for the paper

Run after one or more passes of ``python -m eval.run_eval``. Idempotent.
"""
from __future__ import annotations

import csv
import json
import re
import statistics
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[1]


_TOOL_TAGS = ("whois", "dns", "shodan", "github", "wayback")
_TAG_REGEXES = [re.compile(rf"\b{t}\b", re.I) for t in _TOOL_TAGS]


def hallucination_rate(final_report: str) -> float:
    """Fraction of sentences in the briefing that mention NO tool tag.

    Same metric used inline by ``run_eval.py`` so the two paths stay in
    lockstep — re-running consolidate after the eval gives the same
    numbers."""
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", final_report)
                  if s.strip()]
    if not sentences:
        return 0.0
    grounded = sum(1 for s in sentences
                    if any(rx.search(s) for rx in _TAG_REGEXES))
    return round(1.0 - grounded / len(sentences), 3)


def main() -> None:
    eval_dir = _REPO / "results" / "eval"
    out_csv = _REPO / "results" / "eval_results.csv"
    out_summary = _REPO / "results" / "eval_summary.json"
    targets_path = _REPO / "eval" / "test_targets.json"

    if not eval_dir.exists():
        print(f"no eval dir at {eval_dir}", file=sys.stderr)
        sys.exit(1)

    targets = {t["target"]: t["category"]
               for t in json.loads(targets_path.read_text())["targets"]}

    rows: list[dict] = []
    for json_path in sorted(eval_dir.glob("*.json")):
        try:
            d = json.loads(json_path.read_text(encoding="utf-8"))
        except (ValueError, OSError) as exc:
            print(f"  skip {json_path.name}: {exc}", file=sys.stderr)
            continue
        target = d["run"]["target"]
        rows.append({
            "target": target,
            "category": targets.get(target, ""),
            "provider": d["run"].get("provider", ""),
            "model": d["run"].get("model", ""),
            "iterations": d["run"]["iterations"],
            "coverage": d["summary"]["coverage"],
            "evidence_count": d["summary"]["evidence_count"],
            "hallucination_rate": hallucination_rate(d.get("final_report", "")),
            "finish_reason": d["summary"]["finish_reason"],
            "elapsed_s": d["run"]["elapsed_s"],
        })

    fieldnames = ["target", "category", "provider", "model", "iterations",
                  "coverage", "evidence_count", "hallucination_rate",
                  "finish_reason", "elapsed_s"]
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow(r)

    if not rows:
        print("no per-target reports found")
        return

    cov_full = sum(1 for r in rows if r["coverage"] == 5)
    summary = {
        "n_targets": len(rows),
        "n_full_coverage": cov_full,
        "full_coverage_rate": round(cov_full / len(rows), 3),
        "evidence_per_target": {
            "mean":   round(statistics.mean(r["evidence_count"] for r in rows), 1),
            "median": statistics.median(r["evidence_count"] for r in rows),
            "min":    min(r["evidence_count"] for r in rows),
            "max":    max(r["evidence_count"] for r in rows),
        },
        "iterations_per_target": {
            "mean":   round(statistics.mean(r["iterations"] for r in rows), 2),
            "median": statistics.median(r["iterations"] for r in rows),
        },
        "hallucination_rate": {
            "mean":   round(statistics.mean(r["hallucination_rate"] for r in rows), 3),
            "median": statistics.median(r["hallucination_rate"] for r in rows),
            "max":    max(r["hallucination_rate"] for r in rows),
        },
        "elapsed_s_per_target": {
            "mean":   round(statistics.mean(r["elapsed_s"] for r in rows), 1),
            "median": statistics.median(r["elapsed_s"] for r in rows),
            "total":  round(sum(r["elapsed_s"] for r in rows), 1),
        },
        "finish_reason": {},
        "providers_used": sorted({r["provider"] for r in rows if r["provider"]}),
    }
    for r in rows:
        summary["finish_reason"][r["finish_reason"]] = (
            summary["finish_reason"].get(r["finish_reason"], 0) + 1
        )

    out_summary.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"wrote {out_csv.relative_to(_REPO)}")
    print(f"wrote {out_summary.relative_to(_REPO)}")
    print(f"  {len(rows)} targets — full-coverage {cov_full}/{len(rows)} "
          f"({summary['full_coverage_rate']*100:.1f}%)")
    print(f"  mean evidence/target {summary['evidence_per_target']['mean']}")
    print(f"  mean halluc {summary['hallucination_rate']['mean']}")
    print(f"  mean elapsed_s {summary['elapsed_s_per_target']['mean']}")


if __name__ == "__main__":  # pragma: no cover
    main()

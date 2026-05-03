"""Structured JSON intelligence report.

The report is the durable artefact of an investigation. Schema
versioned (currently 1) so downstream parsers can detect breaks.

Top-level keys:

    schema_version
    generated_at        — ISO-8601 UTC
    operator_authority  — REQUIRED, set from CLI; the agent will not
                          run without it. Captures *why* the run was
                          allowed.
    run                 — provider, model, target, budget, elapsed
    summary             — coverage, evidence count, finish reason
    evidence            — every Evidence row, one object per item
    trace               — chronological thought-action-observation log
    final_report        — markdown briefing the agent wrote
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


SCHEMA_VERSION = 1


def build_report(
    *,
    target: str,
    provider: str,
    model: str,
    budget: int,
    iterations: int,
    elapsed_s: float,
    operator_authority: str,
    evidence: list[dict],
    trace: list[str],
    tools_called: list[str],
    elapsed_ms_per_tool: Mapping[str, int],
    final_report: str,
    finish_reason: str,
) -> dict[str, Any]:
    coverage = len({t for t in tools_called if t in {
        "whois", "dns", "shodan", "github", "wayback"}})
    return {
        "schema_version": SCHEMA_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "operator_authority": operator_authority,
        "run": {
            "target": target,
            "provider": provider,
            "model": model,
            "budget": budget,
            "iterations": iterations,
            "elapsed_s": round(elapsed_s, 2),
        },
        "summary": {
            "coverage": coverage,
            "tools_called": sorted(tools_called),
            "evidence_count": len(evidence),
            "finish_reason": finish_reason,
            "elapsed_ms_per_tool": dict(elapsed_ms_per_tool),
        },
        "evidence": evidence,
        "trace": trace,
        "final_report": final_report,
    }


def write_json_report(path: str | Path, report: dict[str, Any]) -> Path:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(report, indent=2, sort_keys=False), encoding="utf-8")
    return p

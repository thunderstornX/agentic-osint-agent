"""Human-readable Markdown briefing.

Sister to the JSON report. The agent's narrative final_report is the
hero section; we frame it with a stable header (target, provider,
coverage) and a per-tool evidence table so the briefing remains useful
even if the LLM's prose is sparse.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any


_TOOL_LABELS = {
    "whois":   "WHOIS",
    "dns":     "DNS",
    "shodan":  "Shodan IDB",
    "github":  "GitHub Dork",
    "wayback": "Wayback CDX",
}


def _escape(s: str) -> str:
    return s.replace("|", "\\|").replace("\n", " ")


def render_markdown(report: dict[str, Any]) -> str:
    run = report["run"]
    summary = report["summary"]
    out: list[str] = []
    out.append(f"# OSINT briefing — `{run['target']}`")
    out.append("")
    out.append(f"- **Generated:** {report['generated_at']}")
    out.append(f"- **Provider / model:** `{run['provider']}` / `{run['model']}`")
    out.append(f"- **Iterations:** {run['iterations']} of {run['budget']} budget")
    out.append(f"- **Wall-clock:** {run['elapsed_s']} s")
    out.append(f"- **Tool coverage:** {summary['coverage']}/5  "
               f"({', '.join(summary['tools_called']) or '—'})")
    out.append(f"- **Finish reason:** `{summary['finish_reason']}`")
    out.append(f"- **Operator authority:** {report['operator_authority']}")
    out.append("")
    out.append("## Briefing")
    out.append("")
    out.append(report["final_report"].strip() or "_(empty)_")
    out.append("")

    out.append("## Evidence by tool")
    out.append("")
    out.append("| Tool | Calls | Findings |")
    out.append("|---|---:|---:|")
    counts: dict[str, dict[str, int]] = {k: {"calls": 0, "findings": 0}
                                         for k in _TOOL_LABELS}
    for ev in report.get("evidence", []):
        bucket = counts.setdefault(ev["tool"], {"calls": 0, "findings": 0})
        bucket["findings"] += 1
    for tool in summary.get("tools_called", []):
        if tool in counts:
            counts[tool]["calls"] = max(1, counts[tool]["calls"])
    for key, label in _TOOL_LABELS.items():
        c = counts.get(key, {"calls": 0, "findings": 0})
        out.append(f"| {label} | {c['calls']} | {c['findings']} |")
    out.append("")

    out.append("## Evidence rows")
    out.append("")
    out.append("| # | Tool | Kind | Value | Source |")
    out.append("|---:|---|---|---|---|")
    for i, ev in enumerate(report.get("evidence", []), 1):
        out.append(
            f"| {i} | {ev['tool']} | {ev['kind']} | "
            f"`{_escape(str(ev['value']))[:80]}` | "
            f"{_escape(str(ev.get('source', '')))[:80]} |"
        )
    out.append("")

    out.append("## Trace")
    out.append("")
    for line in report.get("trace", []):
        out.append(f"- {_escape(line)}")
    out.append("")
    return "\n".join(out)


def write_markdown_briefing(path: str | Path, report: dict[str, Any]) -> Path:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(render_markdown(report), encoding="utf-8")
    return p

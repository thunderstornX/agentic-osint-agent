"""Report writers."""
from __future__ import annotations

import json
from pathlib import Path

from output.formatter import build_report, write_json_report
from output.markdown import render_markdown


def _sample_report():
    return build_report(
        target="x.example",
        provider="openrouter",
        model="meta/llama-3.3-70b-instruct:free",
        budget=8,
        iterations=4,
        elapsed_s=12.34,
        operator_authority="Authorised: bug-bounty programme XYZ-2026",
        evidence=[
            {"tool": "whois", "target": "x.example", "kind": "registrar",
             "value": "ACME Registrar", "source": "WHOIS",
             "detail": "registrar of record", "confidence": 0.95,
             "fingerprint": "abc"},
            {"tool": "dns", "target": "x.example", "kind": "dns.a",
             "value": "203.0.113.5", "source": "DNS A",
             "detail": "A record", "confidence": 0.95, "fingerprint": "def"},
        ],
        trace=["plan: cover all five", "decide -> whois", "observe: 1 finding"],
        tools_called=["whois", "dns"],
        elapsed_ms_per_tool={"whois": 800, "dns": 200},
        final_report="## Target\nx.example is a placeholder. (WHOIS, DNS)",
        finish_reason="agent_stopped",
    )


def test_json_report_is_valid_and_has_schema_version(tmp_path: Path):
    rep = _sample_report()
    out = write_json_report(tmp_path / "x.json", rep)
    parsed = json.loads(out.read_text())
    assert parsed["schema_version"] == 1
    assert parsed["operator_authority"].startswith("Authorised")
    assert parsed["summary"]["coverage"] == 2


def test_markdown_includes_briefing_and_evidence_table():
    md = render_markdown(_sample_report())
    assert "x.example" in md
    assert "## Briefing" in md
    assert "## Evidence by tool" in md
    assert "WHOIS" in md
    assert "Wayback CDX" in md
    # pipe-escape for any | inside fields
    assert "|" in md


def test_markdown_handles_pipe_escape():
    rep = _sample_report()
    rep["evidence"].append({
        "tool": "dns", "target": "x.example",
        "kind": "dns.txt", "value": "v=spf1 a | all",
        "source": "DNS TXT", "detail": "", "confidence": 0.95,
        "fingerprint": "ghi",
    })
    md = render_markdown(rep)
    assert "\\|" in md  # escaped pipe in the table cell

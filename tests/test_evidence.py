"""Evidence + Scratchpad invariants."""
from __future__ import annotations

from memory.evidence import Evidence
from memory.scratchpad import Scratchpad


def test_evidence_default_confidence_is_high_for_primary_sources():
    e = Evidence(tool="whois", target="x.com", kind="registrar",
                  value="ACME", source="WHOIS")
    assert e.confidence == 0.95


def test_github_evidence_gets_lower_default_confidence():
    e = Evidence(tool="github", target="x.com", kind="github_hit",
                  value="acme/repo:cfg", source="https://github.com/...")
    assert e.confidence == 0.65


def test_explicit_confidence_is_respected_for_github_too():
    e = Evidence(tool="github", target="x.com", kind="github_hit",
                  value="acme/repo:cfg", source="x", confidence=0.9)
    assert e.confidence == 0.9


def test_evidence_fingerprint_is_stable_and_dedups():
    a = Evidence(tool="dns", target="x.com", kind="dns.a", value="1.2.3.4",
                  source="DNS A")
    b = Evidence(tool="dns", target="x.com", kind="dns.a", value="1.2.3.4",
                  source="DNS A")
    assert a.fingerprint == b.fingerprint


def test_scratchpad_dedups_evidence():
    sp = Scratchpad(target="x.com")
    rows = [
        Evidence(tool="dns", target="x.com", kind="dns.a", value="1.2.3.4",
                  source="DNS A"),
        Evidence(tool="dns", target="x.com", kind="dns.a", value="1.2.3.4",
                  source="DNS A"),
    ]
    added = sp.add_evidence(rows)
    assert added == 1
    assert len(sp.evidence) == 1


def test_scratchpad_summary_for_prompt_is_compact():
    sp = Scratchpad(target="x.com")
    sp.set_plan("call whois then dns")
    sp.mark_tool_called("whois")
    sp.add_evidence([Evidence(tool="whois", target="x.com",
                              kind="registrar", value="ACME", source="WHOIS")])
    txt = sp.summary_for_prompt()
    assert "x.com" in txt
    assert "whois" in txt
    assert "ACME" in txt
    # The summary fits comfortably in a system prompt.
    assert len(txt) < 2048

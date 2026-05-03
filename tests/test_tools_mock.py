"""Mocked-HTTP tests for the network-dependent tools.

WHOIS and DNS aren't here because:
  - python-whois performs a real socket connection per query and isn't
    convincingly mockable without monkeypatching the library internals
  - dnspython is similar; the system resolver is the right thing to
    test against in CI on a real machine

Both tools are exercised by the eval harness in Phase 10 against real
public targets, which is the more honest test anyway."""
from __future__ import annotations

import httpx
import respx

from tools.shodan_tool import ShodanTool
from tools.github_dork_tool import GitHubDorkTool
from tools.wayback_tool import WaybackTool


# --- Shodan -----------------------------------------------------------

def test_shodan_handles_404_as_clean_no_data(monkeypatch):
    """InternetDB returns 404 when an IP has no public footprint. That is
    not an error; it is *evidence* of a clean target."""
    tool = ShodanTool(http_client=None)
    monkeypatch.setattr(tool, "_resolve_first_a",
                        lambda domain, timeout_s: "203.0.113.1")
    with respx.mock(assert_all_called=True) as m:
        m.get("https://internetdb.shodan.io/203.0.113.1").mock(
            return_value=httpx.Response(404))
        with httpx.Client() as client:
            tool._client = client
            res = tool.run("clean.example", timeout_s=5)
    assert res.ok
    assert any(e.kind == "shodan.no_data" for e in res.findings)


def test_shodan_parses_full_record(monkeypatch):
    tool = ShodanTool(http_client=None)
    monkeypatch.setattr(tool, "_resolve_first_a",
                        lambda domain, timeout_s: "8.8.8.8")
    payload = {
        "ip": "8.8.8.8",
        "ports": [53, 443],
        "hostnames": ["dns.google"],
        "cpes": ["cpe:/a:google:dns:1.0"],
        "vulns": [],
    }
    with respx.mock(assert_all_called=True) as m:
        m.get("https://internetdb.shodan.io/8.8.8.8").mock(
            return_value=httpx.Response(200, json=payload))
        with httpx.Client() as client:
            tool._client = client
            res = tool.run("dns.google", timeout_s=5)
    assert res.ok
    kinds = sorted({e.kind for e in res.findings})
    assert "open_port" in kinds
    assert "hostname" in kinds
    assert "cpe" in kinds


def test_shodan_no_a_record_is_graceful_error(monkeypatch):
    tool = ShodanTool(http_client=None)
    monkeypatch.setattr(tool, "_resolve_first_a",
                        lambda domain, timeout_s: None)
    res = tool.run("nx.example", timeout_s=5)
    assert not res.ok
    assert "no A record" in (res.error or "")


# --- GitHub dork ------------------------------------------------------

def test_github_parses_results_and_assigns_low_confidence():
    """A successful dork yields github_hit findings with confidence 0.65."""
    tool = GitHubDorkTool(http_client=None, sleep_s=0)
    payload = {
        "total_count": 1,
        "items": [
            {
                "repository": {"full_name": "acme/leak"},
                "path": "config.yml",
                "html_url": "https://github.com/acme/leak/blob/main/config.yml",
            }
        ],
    }
    with respx.mock(assert_all_called=False) as m:
        m.get("https://api.github.com/search/code").mock(
            return_value=httpx.Response(200, json=payload))
        with httpx.Client() as client:
            tool._client = client
            res = tool.run("acme.com", timeout_s=5)
    assert res.findings
    assert all(e.confidence == 0.65 for e in res.findings)
    assert all(e.kind == "github_hit" for e in res.findings)


def test_github_rate_limit_is_recorded_not_thrown():
    tool = GitHubDorkTool(http_client=None, sleep_s=0)
    with respx.mock(assert_all_called=False) as m:
        m.get("https://api.github.com/search/code").mock(
            return_value=httpx.Response(403, json={"message": "rate limit"}))
        with httpx.Client() as client:
            tool._client = client
            res = tool.run("acme.com", timeout_s=5)
    # rate limited — no findings, but the run should not raise; the
    # error message must not include any of GitHub's response body.
    assert "rate" in (res.error or "").lower()


# --- Wayback ----------------------------------------------------------

def test_wayback_extracts_first_last_and_count():
    tool = WaybackTool(http_client=None)
    rows = [
        ["timestamp", "original", "statuscode", "mimetype"],
        ["19990101000000", "http://example.com", "200", "text/html"],
        ["20140112120000", "http://example.com", "200", "text/html"],
        ["20240501080000", "http://example.com", "200", "text/html"],
    ]
    with respx.mock(assert_all_called=True) as m:
        m.get("http://web.archive.org/cdx/search/cdx").mock(
            return_value=httpx.Response(200, json=rows))
        with httpx.Client() as client:
            tool._client = client
            res = tool.run("example.com", timeout_s=5)
    assert res.ok
    kinds = {e.kind for e in res.findings}
    assert "wayback.first_snapshot" in kinds
    assert "wayback.last_snapshot" in kinds
    assert "wayback.snapshot_count" in kinds


def test_wayback_empty_response_is_no_snapshots():
    tool = WaybackTool(http_client=None)
    with respx.mock(assert_all_called=True) as m:
        m.get("http://web.archive.org/cdx/search/cdx").mock(
            return_value=httpx.Response(200, json=[["timestamp"]]))
        with httpx.Client() as client:
            tool._client = client
            res = tool.run("brand-new.example", timeout_s=5)
    assert res.ok
    assert any(e.kind == "wayback.no_snapshots" for e in res.findings)

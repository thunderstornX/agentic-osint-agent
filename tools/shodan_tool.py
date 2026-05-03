"""Shodan InternetDB free endpoint.

InternetDB is the public, no-auth surface of Shodan: GET ``/{ip}``
returns a tiny JSON document with open ports, hostnames, vulns, CPEs.
No API key, no rate limit listed beyond polite use.

We resolve the *target domain* to its A records first (one DNS call),
then query the IP. If the domain has no A record, the run is a graceful
no-op rather than an error."""
from __future__ import annotations

import time

import dns.exception
import dns.resolver
import httpx

from memory.evidence import Evidence
from tools.base import Tool, ToolResult, _normalise_target


_BASE_URL = "https://internetdb.shodan.io"


class ShodanTool(Tool):
    name = "shodan"
    description = (
        "Query Shodan's free InternetDB endpoint for the target's IP "
        "address: returns open ports, hostnames seen on the IP, known "
        "vulnerabilities, and CPE strings. No API key needed; safe to "
        "call without authentication."
    )

    def __init__(self, *, base_url: str = _BASE_URL, http_client: httpx.Client | None = None):
        self._base = base_url.rstrip("/")
        self._client = http_client  # injected for tests

    def _resolve_first_a(self, domain: str, timeout_s: float) -> str | None:
        resolver = dns.resolver.Resolver()
        resolver.lifetime = timeout_s
        resolver.timeout = max(2.0, timeout_s / 2)
        try:
            answers = resolver.resolve(domain, "A")
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer,
                dns.resolver.NoNameservers, dns.exception.Timeout):
            return None
        for r in answers:
            return r.to_text().strip()
        return None

    def run(self, target: str, *, timeout_s: float = 15.0) -> ToolResult:
        domain = _normalise_target(target)
        started = time.monotonic()
        result = ToolResult(tool=self.name, target=domain)

        ip = self._resolve_first_a(domain, timeout_s=timeout_s)
        if not ip:
            result.error = "no A record to look up on InternetDB"
            result.elapsed_ms = int((time.monotonic() - started) * 1000)
            return result

        url = f"{self._base}/{ip}"
        client = self._client or httpx.Client(timeout=timeout_s)
        try:
            response = client.get(url, headers={"Accept": "application/json"})
        except httpx.HTTPError as exc:
            result.error = f"InternetDB request failed: {exc.__class__.__name__}"
            result.elapsed_ms = int((time.monotonic() - started) * 1000)
            return result
        finally:
            if self._client is None:
                client.close()

        if response.status_code == 404:
            # The endpoint legitimately returns 404 when an IP has no
            # public footprint. That's not an error — it's a clean lookup.
            result.raw = {"ip": ip, "status": "no_public_footprint"}
            result.findings.append(Evidence(
                tool=self.name, target=domain,
                kind="shodan.no_data",
                value=ip,
                source=url,
                detail=f"InternetDB returned no public records for {ip}",
            ))
            result.elapsed_ms = int((time.monotonic() - started) * 1000)
            return result

        if response.status_code >= 400:
            result.error = f"InternetDB returned HTTP {response.status_code}"
            result.elapsed_ms = int((time.monotonic() - started) * 1000)
            return result

        try:
            data = response.json()
        except ValueError:
            result.error = "InternetDB response was not JSON"
            result.elapsed_ms = int((time.monotonic() - started) * 1000)
            return result

        result.raw = data

        for port in data.get("ports", []) or []:
            result.findings.append(Evidence(
                tool=self.name, target=domain,
                kind="open_port",
                value=str(port),
                source=url,
                detail=f"open TCP port on {ip}",
            ))

        for hostname in data.get("hostnames", []) or []:
            result.findings.append(Evidence(
                tool=self.name, target=domain,
                kind="hostname",
                value=str(hostname),
                source=url,
                detail=f"hostname seen on {ip}",
            ))

        for cpe in data.get("cpes", []) or []:
            result.findings.append(Evidence(
                tool=self.name, target=domain,
                kind="cpe",
                value=str(cpe),
                source=url,
                detail=f"CPE software identifier on {ip}",
            ))

        for vuln in data.get("vulns", []) or []:
            result.findings.append(Evidence(
                tool=self.name, target=domain,
                kind="vuln",
                value=str(vuln),
                source=url,
                detail=f"published vulnerability associated with {ip}",
            ))

        result.elapsed_ms = int((time.monotonic() - started) * 1000)
        return result

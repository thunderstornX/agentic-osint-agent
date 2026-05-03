"""DNS lookup via dnspython.

Looks up A, AAAA, MX, NS, TXT, CNAME for a domain. Each record
becomes an Evidence row. We keep the resolver default (system DNS)
because most workstations already have a sensible recursive."""
from __future__ import annotations

import time

import dns.exception
import dns.resolver

from memory.evidence import Evidence
from tools.base import Tool, ToolResult, _normalise_target


_RECORD_TYPES = ("A", "AAAA", "MX", "NS", "TXT", "CNAME")


class DnsTool(Tool):
    name = "dns"
    description = (
        "Resolve A / AAAA / MX / NS / TXT / CNAME records for a domain. "
        "Useful for confirming hosts seen elsewhere and for spotting "
        "SPF / DKIM / verification tokens in TXT records."
    )

    def run(self, target: str, *, timeout_s: float = 15.0) -> ToolResult:
        domain = _normalise_target(target)
        started = time.monotonic()
        result = ToolResult(tool=self.name, target=domain)
        raw: dict[str, list[str]] = {}

        resolver = dns.resolver.Resolver()
        resolver.lifetime = timeout_s
        resolver.timeout = max(2.0, timeout_s / len(_RECORD_TYPES))

        any_success = False
        for rtype in _RECORD_TYPES:
            try:
                answers = resolver.resolve(domain, rtype, raise_on_no_answer=False)
            except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer,
                    dns.resolver.NoNameservers, dns.exception.Timeout):
                raw[rtype] = []
                continue
            except Exception:  # pragma: no cover - rare resolver edge
                raw[rtype] = []
                continue

            any_success = True
            values = [r.to_text().strip('"') for r in answers]
            raw[rtype] = values
            for v in values:
                result.findings.append(Evidence(
                    tool=self.name, target=domain,
                    kind=f"dns.{rtype.lower()}",
                    value=v,
                    source=f"DNS {rtype}",
                    detail=f"{rtype} record",
                ))

        if not any_success and not result.findings:
            # No record types resolved at all — likely the domain doesn't
            # exist in public DNS. Surface as error rather than silent.
            result.error = "no DNS records resolved"

        result.raw = raw
        result.elapsed_ms = int((time.monotonic() - started) * 1000)
        return result

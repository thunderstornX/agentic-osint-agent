"""WHOIS lookup via the python-whois library.

We don't pretend WHOIS is uniform — registries return wildly different
shapes — so we extract a small, stable subset (registrar, creation,
expiration, name servers, registrant org if public) and turn each into a
discrete piece of Evidence."""
from __future__ import annotations

import time
from datetime import datetime
from typing import Any

import whois  # python-whois

from memory.evidence import Evidence
from tools.base import Tool, ToolResult, _normalise_target


def _stringify_date(value: Any) -> str | None:
    if value is None:
        return None
    if isinstance(value, list):
        # WHOIS often returns multiple historical dates; we keep the
        # earliest we can parse, tying it to the *original* registration.
        parsed = [v for v in value if isinstance(v, datetime)]
        if not parsed:
            return None
        return min(parsed).date().isoformat()
    if isinstance(value, datetime):
        return value.date().isoformat()
    return str(value)


def _stringify_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [str(v) for v in value if v]
    return [str(value)]


class WhoisTool(Tool):
    name = "whois"
    description = (
        "Look up registrar, creation/expiration dates, name servers, and "
        "(if public) registrant organisation for a domain. Cheap and "
        "fast; usually the first call in an investigation."
    )

    def run(self, target: str, *, timeout_s: float = 15.0) -> ToolResult:
        domain = _normalise_target(target)
        started = time.monotonic()
        result = ToolResult(tool=self.name, target=domain)

        try:
            record = whois.whois(domain)
        except Exception as exc:  # WHOIS lib is liberal about exception types
            result.error = f"whois lookup failed: {exc.__class__.__name__}"
            result.elapsed_ms = int((time.monotonic() - started) * 1000)
            return result

        if not record or not getattr(record, "domain_name", None):
            result.error = "no whois record returned"
            result.elapsed_ms = int((time.monotonic() - started) * 1000)
            return result

        # ----------- distil the record into structured findings -------
        registrar = getattr(record, "registrar", None)
        if registrar:
            result.findings.append(Evidence(
                tool=self.name, target=domain,
                kind="registrar",
                value=str(registrar),
                source="WHOIS",
                detail="domain registrar of record",
            ))

        created = _stringify_date(getattr(record, "creation_date", None))
        if created:
            result.findings.append(Evidence(
                tool=self.name, target=domain,
                kind="creation_date",
                value=created,
                source="WHOIS",
                detail="domain creation date",
            ))

        expires = _stringify_date(getattr(record, "expiration_date", None))
        if expires:
            result.findings.append(Evidence(
                tool=self.name, target=domain,
                kind="expiration_date",
                value=expires,
                source="WHOIS",
                detail="domain expiration date",
            ))

        nss = _stringify_list(getattr(record, "name_servers", None))
        # WHOIS frequently duplicates name servers in mixed case; dedupe
        # while preserving order so the agent sees a stable list.
        seen: set[str] = set()
        for ns in nss:
            key = ns.lower()
            if key in seen:
                continue
            seen.add(key)
            result.findings.append(Evidence(
                tool=self.name, target=domain,
                kind="name_server",
                value=ns.lower(),
                source="WHOIS",
                detail="authoritative name server",
            ))

        org = getattr(record, "org", None)
        if org and isinstance(org, str) and org.strip():
            result.findings.append(Evidence(
                tool=self.name, target=domain,
                kind="registrant_org",
                value=org.strip(),
                source="WHOIS",
                detail="public registrant organisation",
            ))

        result.raw = {
            "registrar": registrar,
            "creation_date": created,
            "expiration_date": expires,
            "name_servers": list(seen),
            "org": org,
        }
        result.elapsed_ms = int((time.monotonic() - started) * 1000)
        return result

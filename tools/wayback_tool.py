"""Wayback Machine CDX API.

The CDX endpoint at ``http://web.archive.org/cdx/search/cdx`` returns
chronological snapshot rows for a URL prefix. We capture the first
snapshot, the last snapshot, and an estimate of how many snapshots
exist — enough to spot domains that have been alive for decades and
domains that only just appeared in the index."""
from __future__ import annotations

import time
from datetime import datetime

import httpx

from memory.evidence import Evidence
from tools.base import Tool, ToolResult, _normalise_target


_BASE_URL = "http://web.archive.org/cdx/search/cdx"


def _format_wayback_date(stamp: str) -> str:
    """Wayback uses YYYYMMDDhhmmss. Render as ISO date for humans."""
    try:
        return datetime.strptime(stamp[:8], "%Y%m%d").date().isoformat()
    except (ValueError, IndexError):
        return stamp


class WaybackTool(Tool):
    name = "wayback"
    description = (
        "Query the Internet Archive's Wayback Machine CDX API for "
        "historical snapshots of the target domain. Surfaces first-"
        "ever and most-recent snapshot dates plus total snapshot count."
    )

    def __init__(self, *, base_url: str = _BASE_URL,
                 http_client: httpx.Client | None = None):
        self._base = base_url
        self._client = http_client

    def run(self, target: str, *, timeout_s: float = 15.0) -> ToolResult:
        domain = _normalise_target(target)
        started = time.monotonic()
        result = ToolResult(tool=self.name, target=domain)

        params = {
            "url": domain,
            "output": "json",
            "fl": "timestamp,original,statuscode,mimetype",
            "filter": "statuscode:200",
            "limit": 200,        # tight cap — full domain history takes >20s
            "collapse": "timestamp:8",  # one snapshot per day
        }
        owns_client = self._client is None
        client = self._client or httpx.Client(timeout=timeout_s)
        try:
            response = client.get(self._base, params=params)
        except httpx.HTTPError as exc:
            result.error = f"Wayback CDX request failed: {exc.__class__.__name__}"
            result.elapsed_ms = int((time.monotonic() - started) * 1000)
            if owns_client:
                client.close()
            return result

        if owns_client:
            client.close()

        if response.status_code >= 400:
            result.error = f"Wayback CDX returned HTTP {response.status_code}"
            result.elapsed_ms = int((time.monotonic() - started) * 1000)
            return result

        try:
            rows = response.json()
        except ValueError:
            result.error = "Wayback CDX response was not JSON"
            result.elapsed_ms = int((time.monotonic() - started) * 1000)
            return result

        # Header row + zero or more data rows.
        if not isinstance(rows, list) or len(rows) <= 1:
            result.findings.append(Evidence(
                tool=self.name, target=domain,
                kind="wayback.no_snapshots",
                value="0",
                source=self._base,
                detail="no Wayback snapshots returned",
            ))
            result.raw = {"rows": rows if isinstance(rows, list) else []}
            result.elapsed_ms = int((time.monotonic() - started) * 1000)
            return result

        data_rows = rows[1:]
        first = data_rows[0]
        last = data_rows[-1]
        first_date = _format_wayback_date(str(first[0]))
        last_date = _format_wayback_date(str(last[0]))
        first_url = (
            f"https://web.archive.org/web/{first[0]}/{first[1]}"
        )
        last_url = (
            f"https://web.archive.org/web/{last[0]}/{last[1]}"
        )

        result.findings.append(Evidence(
            tool=self.name, target=domain,
            kind="wayback.first_snapshot",
            value=first_date,
            source=first_url,
            detail="earliest archived snapshot for this domain",
        ))
        result.findings.append(Evidence(
            tool=self.name, target=domain,
            kind="wayback.last_snapshot",
            value=last_date,
            source=last_url,
            detail="most recent archived snapshot for this domain",
        ))
        result.findings.append(Evidence(
            tool=self.name, target=domain,
            kind="wayback.snapshot_count",
            value=str(len(data_rows)),
            source=self._base,
            detail="number of distinct daily snapshots returned (capped at 200)",
        ))

        result.raw = {
            "first": first_date,
            "last": last_date,
            "rows_returned": len(data_rows),
        }
        result.elapsed_ms = int((time.monotonic() - started) * 1000)
        return result

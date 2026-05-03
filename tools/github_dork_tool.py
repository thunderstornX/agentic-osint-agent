"""GitHub code-search dorks.

Three dorks are run per target — they are the well-known patterns for
spotting accidental commits of environment files, credentials, or
config that mention the target domain:

    "{target}" filename:.env
    "{target}" password
    "{target}" filename:config

The unauthenticated rate limit on GitHub search is currently 10 req/min;
when ``GITHUB_TOKEN`` is set the limit lifts to 30 req/min — but we still
sleep ~1s between dorks to be polite and to keep the agent's per-tool
latency in a sane place.
"""
from __future__ import annotations

import os
import time

import httpx

from memory.evidence import Evidence
from tools.base import Tool, ToolResult, _normalise_target


_BASE_URL = "https://api.github.com/search/code"
_PATTERNS = (
    'filename:.env',
    'password',
    'filename:config',
)
_BETWEEN_DORKS_S = 1.0
_MAX_RESULTS_PER_DORK = 5


class GitHubDorkTool(Tool):
    name = "github"
    description = (
        "Search public GitHub for accidental commits that mention the "
        "target domain in `.env`, `config`, or password contexts. Read-"
        "only; uses the public search API. Set GITHUB_TOKEN for higher "
        "rate limits."
    )

    def __init__(self, *, base_url: str = _BASE_URL,
                 http_client: httpx.Client | None = None,
                 token: str | None = None,
                 sleep_s: float = _BETWEEN_DORKS_S):
        self._base = base_url
        self._client = http_client
        self._token = token if token is not None else os.getenv("GITHUB_TOKEN")
        self._sleep_s = sleep_s

    def _headers(self) -> dict[str, str]:
        h = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if self._token:
            h["Authorization"] = f"Bearer {self._token}"
        return h

    def run(self, target: str, *, timeout_s: float = 15.0) -> ToolResult:
        domain = _normalise_target(target)
        started = time.monotonic()
        result = ToolResult(tool=self.name, target=domain)
        owns_client = self._client is None
        client = self._client or httpx.Client(timeout=timeout_s)
        per_dork: list[dict] = []

        try:
            for i, pattern in enumerate(_PATTERNS):
                if i > 0:
                    time.sleep(self._sleep_s)
                query = f'"{domain}" {pattern}'
                params = {"q": query, "per_page": _MAX_RESULTS_PER_DORK}
                try:
                    r = client.get(self._base, headers=self._headers(),
                                   params=params)
                except httpx.HTTPError as exc:
                    per_dork.append({
                        "pattern": pattern,
                        "error": exc.__class__.__name__,
                    })
                    continue

                if r.status_code == 403:
                    per_dork.append({
                        "pattern": pattern,
                        "error": "rate_limited",
                    })
                    # back off the rest of this run; the agent can try
                    # again in a later iteration with a token set
                    break
                if r.status_code >= 400:
                    per_dork.append({
                        "pattern": pattern,
                        "error": f"http_{r.status_code}",
                    })
                    continue

                try:
                    data = r.json()
                except ValueError:
                    per_dork.append({"pattern": pattern, "error": "not_json"})
                    continue

                items = data.get("items", []) or []
                per_dork.append({
                    "pattern": pattern,
                    "total_count": data.get("total_count"),
                    "shown": len(items),
                })
                for it in items[:_MAX_RESULTS_PER_DORK]:
                    repo = (it.get("repository") or {}).get("full_name", "?")
                    path = it.get("path", "?")
                    html_url = it.get("html_url", "")
                    result.findings.append(Evidence(
                        tool=self.name, target=domain,
                        kind="github_hit",
                        value=f"{repo}:{path}",
                        source=html_url or self._base,
                        detail=f'matched "{domain}" {pattern}',
                    ))
        finally:
            if owns_client:
                client.close()

        result.raw = {"queries": per_dork}
        if not result.findings and all("error" in d for d in per_dork):
            # All three dorks failed (typically: no token + rate limit)
            result.error = "all GitHub dorks errored — check rate limit"
        result.elapsed_ms = int((time.monotonic() - started) * 1000)
        return result

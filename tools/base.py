"""Tool contract.

Each tool is a stateless callable: ``tool.run(target) -> ToolResult``.
Errors are *carried inside the ToolResult* rather than thrown — the agent
needs to keep going when one source is offline. Real exceptions only
fly when the caller misuses the API."""
from __future__ import annotations

import abc
from dataclasses import dataclass, field
from typing import Any

from memory.evidence import Evidence


class ToolError(RuntimeError):
    """Raised only for caller errors (bad target, no network at all).
    Tool-level network/HTTP failures are reported via ToolResult.error."""


@dataclass
class ToolResult:
    """Uniform return type. ``findings`` is the *primary* data path; the
    raw response body is kept on ``raw`` for audit but is not what the
    agent reads back as evidence."""
    tool: str
    target: str
    findings: list[Evidence] = field(default_factory=list)
    raw: dict[str, Any] | list[Any] | None = None
    error: str | None = None
    elapsed_ms: int = 0

    @property
    def ok(self) -> bool:
        return self.error is None

    def to_dict(self) -> dict[str, Any]:
        return {
            "tool": self.tool,
            "target": self.target,
            "findings": [e.to_dict() for e in self.findings],
            "error": self.error,
            "elapsed_ms": self.elapsed_ms,
            # raw is intentionally omitted from the brief dict; full
            # provenance lives in the JSON report.
        }


class Tool(abc.ABC):
    """Sync interface — every concrete tool wraps its blocking calls
    with a thread executor when invoked from the async agent loop."""

    name: str            # e.g. "whois"
    description: str     # what the LLM sees in the prompt

    @abc.abstractmethod
    def run(self, target: str, *, timeout_s: float = 15.0) -> ToolResult:
        ...

    def __repr__(self) -> str:  # pragma: no cover - debugging aid
        return f"<Tool {self.name}>"


def _normalise_target(raw: str) -> str:
    """Strip protocol and path; keep just a hostname.

    The agent's prompt is loose about target format; we normalise once
    here so each tool's input parsing stays small."""
    t = raw.strip()
    if not t:
        raise ToolError("empty target")
    for prefix in ("https://", "http://", "//"):
        if t.startswith(prefix):
            t = t[len(prefix):]
    t = t.split("/", 1)[0].split("?", 1)[0].split("#", 1)[0]
    # strip trailing dot on FQDNs and any port suffix
    t = t.rstrip(".").split(":", 1)[0]
    if not t:
        raise ToolError("empty target after normalisation")
    return t.lower()

"""Evidence: a single, citable finding.

Every finding the agent produces flows through this dataclass. Two
non-negotiables:

  1. ``source`` — *where* this came from (a URL, a tool name, a record
     type). No source, no evidence; the agent must always be able to
     point back at the origin.
  2. ``confidence`` — a 0..1 self-assessed score. Tools default to 0.95
     for primary-source data (WHOIS, DNS, CDX rows) and 0.65 for
     pattern-based hits (GitHub dork results) where false-positive risk
     is real.
"""
from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any


@dataclass
class Evidence:
    tool: str
    target: str
    kind: str
    value: str
    source: str
    detail: str = ""
    confidence: float = field(default=0.95)

    def __post_init__(self) -> None:
        # Pattern-based tools (the GitHub dork in particular) carry more
        # noise than primary-source lookups. We adjust default confidence
        # only when the caller hasn't already overridden it.
        if self.tool == "github" and self.confidence == 0.95:
            self.confidence = 0.65

    @property
    def fingerprint(self) -> str:
        """Stable hash for dedup. Two evidence rows from the same tool
        with the same kind/value collapse."""
        h = hashlib.sha256(
            f"{self.tool}|{self.kind}|{self.value}".encode("utf-8"),
            usedforsecurity=False,
        )
        return h.hexdigest()[:12]

    def to_dict(self) -> dict[str, Any]:
        return {
            "tool": self.tool,
            "target": self.target,
            "kind": self.kind,
            "value": self.value,
            "source": self.source,
            "detail": self.detail,
            "confidence": round(self.confidence, 2),
            "fingerprint": self.fingerprint,
        }

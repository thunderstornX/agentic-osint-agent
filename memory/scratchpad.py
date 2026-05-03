"""Investigation scratchpad.

The scratchpad is the single thing the agent reads back to itself each
turn. It contains:

  - the running plan (LLM-written)
  - the set of tools called so far
  - all evidence gathered, deduped by fingerprint
  - a free-text trace of recent thought-action-observation triples

We aim to keep the *prompt-visible* portion under 2 KB so the agent
doesn't drown in its own history. ``recent_trace()`` returns just the
last few entries for that reason."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable

from memory.evidence import Evidence


@dataclass
class Scratchpad:
    target: str
    plan: str = ""
    tools_called: set[str] = field(default_factory=set)
    evidence: list[Evidence] = field(default_factory=list)
    trace: list[str] = field(default_factory=list)
    _seen_fingerprints: set[str] = field(default_factory=set, repr=False)

    # ----------------------------------------- evidence accumulation --
    def add_evidence(self, items: Iterable[Evidence]) -> int:
        """Add evidence; return how many were *new* (not duplicates)."""
        added = 0
        for e in items:
            fp = e.fingerprint
            if fp in self._seen_fingerprints:
                continue
            self._seen_fingerprints.add(fp)
            self.evidence.append(e)
            added += 1
        return added

    def evidence_for(self, tool: str) -> list[Evidence]:
        return [e for e in self.evidence if e.tool == tool]

    # ----------------------------------------- trace + plan --------------
    def append_trace(self, line: str) -> None:
        self.trace.append(line)

    def recent_trace(self, n: int = 6) -> list[str]:
        return self.trace[-n:]

    def set_plan(self, plan: str) -> None:
        self.plan = plan.strip()

    # ----------------------------------------- coverage helpers ----------
    @property
    def coverage(self) -> int:
        return len(self.tools_called)

    def mark_tool_called(self, tool: str) -> None:
        self.tools_called.add(tool)

    # ----------------------------------------- prompt-shaped view -------
    def summary_for_prompt(self) -> str:
        """The exact string injected into the next ReAct prompt."""
        lines = [f"target: {self.target}"]
        if self.plan:
            lines.append(f"plan: {self.plan}")
        lines.append(
            f"tools called so far ({len(self.tools_called)}/5): "
            + (", ".join(sorted(self.tools_called)) if self.tools_called else "none")
        )
        lines.append(f"evidence rows so far: {len(self.evidence)}")
        if self.evidence:
            lines.append("recent evidence:")
            for e in self.evidence[-8:]:
                lines.append(f"  [{e.tool}] {e.kind} = {e.value[:80]}")
        return "\n".join(lines)

"""Investigation scratchpad + evidence chain.

The agent's *only* memory of what it's found so far. Kept deliberately
small and explicit — the LLM sees the scratchpad each turn, so we want
it dense, citable, and free of internal-agent metadata.
"""
from memory.evidence import Evidence
from memory.scratchpad import Scratchpad

__all__ = ["Evidence", "Scratchpad"]

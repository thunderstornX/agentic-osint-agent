"""Shared fixtures.

Make sure the repo root is on the path so the modules import the same
way they would from the CLI entry point."""
from __future__ import annotations

import os
import sys
from pathlib import Path

import pytest

_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))


@pytest.fixture(autouse=True)
def _no_real_secrets(monkeypatch):
    """Belt-and-braces: never let a real key bleed into the test suite."""
    for key in ("OPENROUTER_API_KEY", "NVIDIA_API_KEY", "GITHUB_TOKEN"):
        monkeypatch.delenv(key, raising=False)
    yield

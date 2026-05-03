"""LLM adapter wire-format and key-handling tests."""
from __future__ import annotations

import io
import os

import httpx
import pytest
import respx
from rich.console import Console

from agent.llm import LLM, LLMError
from agent.tui.theme import THEME


def _ok_response(text: str) -> httpx.Response:
    return httpx.Response(200, json={
        "id": "x",
        "model": "fake",
        "choices": [{"message": {"role": "assistant", "content": text}}],
    })


def test_openrouter_happy_path():
    with respx.mock(assert_all_called=True) as m:
        m.post("https://openrouter.ai/api/v1/chat/completions").mock(
            return_value=_ok_response("hello"))
        with httpx.Client() as c:
            llm = LLM(provider="openrouter", api_key="sk-or-test", client=c)
            r = llm.chat(system="s", user="u", max_tokens=10)
    assert r.text == "hello"
    assert r.latency_ms >= 0


def test_nvidia_handles_content_parts_list():
    with respx.mock(assert_all_called=True) as m:
        m.post("https://integrate.api.nvidia.com/v1/chat/completions").mock(
            return_value=httpx.Response(200, json={
                "model": "nim",
                "choices": [{"message": {"content": [
                    {"type": "text", "text": "part-a "},
                    {"type": "text", "text": "part-b"},
                ]}}],
            }))
        with httpx.Client() as c:
            llm = LLM(provider="nvidia", api_key="nvapi-test", client=c)
            r = llm.chat(system="s", user="u")
    assert r.text == "part-a part-b"


def test_missing_key_raises():
    with pytest.raises(LLMError):
        LLM(provider="openrouter")


def test_http_error_does_not_echo_response_body():
    """The raw response body can include the request — including the
    system prompt — so the adapter must never include it in the error."""
    leaky = "leaked-system-prompt-here please do not echo"
    with respx.mock(assert_all_called=True) as m:
        m.post("https://openrouter.ai/api/v1/chat/completions").mock(
            return_value=httpx.Response(500, text=leaky))
        with httpx.Client() as c:
            llm = LLM(provider="openrouter", api_key="sk-or-test", client=c)
            with pytest.raises(LLMError) as excinfo:
                llm.chat(system="s", user="u")
    assert "leaked" not in str(excinfo.value)


def test_api_key_is_never_printed_anywhere(capsys):
    """Belt-and-braces: smoke for accidental key prints in error paths."""
    leaky_key = "sk-or-thisisthekey9999"
    with respx.mock(assert_all_called=False) as m:
        m.post("https://openrouter.ai/api/v1/chat/completions").mock(
            side_effect=httpx.ConnectError("boom"))
        with httpx.Client() as c:
            llm = LLM(provider="openrouter", api_key=leaky_key, client=c)
            with pytest.raises(LLMError):
                llm.chat(system="s", user="u")
    out = capsys.readouterr()
    assert leaky_key not in out.out
    assert leaky_key not in out.err

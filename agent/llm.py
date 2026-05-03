"""OpenAI-compatible LLM client.

Two providers, one wire format. Both speak ``/chat/completions`` so we
keep a single implementation and swap base-URL + key + model.

Why no LangChain ChatModel here: LangChain's chat-model wrappers add
two layers of message-object translation that we don't need for a
ReAct loop with three short calls. A 50-line httpx client is
predictable and easy to mock with respx.
"""
from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Literal

import httpx


Provider = Literal["openrouter", "nvidia"]


_PROVIDER_DEFAULTS: dict[str, dict[str, str]] = {
    "openrouter": {
        "base_url": "https://openrouter.ai/api/v1",
        "env_key":  "OPENROUTER_API_KEY",
        # OpenRouter's free-tier identifier suffix.
        "default_model": "meta-llama/llama-3.3-70b-instruct:free",
    },
    "nvidia": {
        "base_url": "https://integrate.api.nvidia.com/v1",
        "env_key":  "NVIDIA_API_KEY",
        # NVIDIA NIM free-tier model.
        "default_model": "meta/llama-3.3-70b-instruct",
    },
}


class LLMError(RuntimeError):
    """Generic adapter error. Never includes the raw response body to
    avoid accidentally logging secrets the model echoed back."""


@dataclass
class LLMResponse:
    text: str
    latency_ms: int
    model_reported: str | None = None


class LLM:
    """Thin OpenAI-compat client. Synchronous — the agent already
    serialises its three calls, so there's nothing to gain from async
    here."""

    def __init__(
        self,
        *,
        provider: Provider,
        model: str | None = None,
        api_key: str | None = None,
        base_url: str | None = None,
        timeout_s: float = 45.0,
        client: httpx.Client | None = None,
    ):
        if provider not in _PROVIDER_DEFAULTS:
            raise LLMError(f"unsupported provider: {provider}")
        defaults = _PROVIDER_DEFAULTS[provider]
        self.provider = provider
        self.base_url = (base_url or defaults["base_url"]).rstrip("/")
        self.model = model or defaults["default_model"]
        self._key = api_key if api_key is not None else os.getenv(defaults["env_key"])
        if not self._key:
            raise LLMError(
                f"{defaults['env_key']} is not set; export it or pass --api-key"
            )
        self._client = client or httpx.Client(timeout=timeout_s)
        self._owns_client = client is None

    def close(self) -> None:
        if self._owns_client:
            self._client.close()

    # ---------------------------------------------------- main call --
    def chat(
        self,
        *,
        system: str,
        user: str,
        max_tokens: int = 600,
        temperature: float = 0.0,
    ) -> LLMResponse:
        url = f"{self.base_url}/chat/completions"
        headers = {
            "Authorization": f"Bearer {self._key}",
            "Content-Type": "application/json",
        }
        if self.provider == "openrouter":
            # OpenRouter recommends these headers for routing & ranking.
            headers["HTTP-Referer"] = "https://github.com/thunderstornX/agentic-osint-agent"
            headers["X-Title"] = "agentic-osint-agent"
        body = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user",   "content": user},
            ],
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": False,
        }
        import time
        started = time.monotonic()
        try:
            r = self._client.post(url, headers=headers, json=body)
        except httpx.HTTPError as exc:
            raise LLMError(
                f"{self.provider} HTTP error: {exc.__class__.__name__}"
            ) from exc
        latency_ms = int((time.monotonic() - started) * 1000)

        if r.status_code >= 400:
            # Deliberately do NOT include r.text; some providers echo
            # the request body, including the system prompt + key in
            # mis-routed cases.
            raise LLMError(
                f"{self.provider} returned HTTP {r.status_code}"
            )

        try:
            data = r.json()
        except ValueError as exc:
            raise LLMError(f"{self.provider} response was not JSON") from exc

        choices = data.get("choices") or []
        if not choices:
            raise LLMError(f"{self.provider} response had no choices")

        msg = choices[0].get("message") or {}
        content = msg.get("content")
        # Some NIM endpoints return a list of content parts. Defensive
        # reassembly if so.
        if isinstance(content, list):
            content = "".join(
                p.get("text", "") for p in content
                if isinstance(p, dict) and p.get("type") in (None, "text")
            )
        if not isinstance(content, str) or not content.strip():
            raise LLMError(f"{self.provider} response had empty content")

        return LLMResponse(
            text=content.strip(),
            latency_ms=latency_ms,
            model_reported=data.get("model"),
        )

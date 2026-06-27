from __future__ import annotations

from typing import Any


class LLMGateway:
    """
    Central gateway for communicating with Large Language Models (LLMs).

    Currently this is a placeholder implementation.
    Future versions will support providers such as:
        - Gemini
        - OpenAI
        - Claude
        - Ollama
    """

    def __init__(
        self,
        provider: str = "mock",
    ) -> None:

        self.provider = provider

    async def generate(
        self,
        prompt: str,
        **kwargs: Any,
    ) -> str:
        """
        Generates a response for the given prompt.

        This placeholder implementation simply returns
        a mock response.
        """

        return (
            "Mock LLM Response\n\n"
            f"Prompt Received:\n{prompt}"
        )
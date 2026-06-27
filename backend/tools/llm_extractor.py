from __future__ import annotations

from typing import Any, Dict, Optional

from core.llm_gateway import LLMGateway


class LLMExtractor:
    """
    Uses the configured LLM to extract structured
    information from unstructured text.

    The extractor delegates all LLM communication
    to the LLMGateway.
    """

    def __init__(
        self,
        llm_gateway: Optional[LLMGateway] = None,
    ) -> None:

        self.llm_gateway = llm_gateway or LLMGateway()

    # ---------------------------------------------------------
    # Prompt Builder
    # ---------------------------------------------------------

    def build_prompt(
        self,
        text: str,
        instruction: str,
    ) -> str:
        """
        Builds the extraction prompt.
        """

        return f"""
You are an intelligent information extraction system.

Task:
{instruction}

Text:
{text}

Return only structured JSON.
"""

    # ---------------------------------------------------------
    # Extraction
    # ---------------------------------------------------------

    async def extract(
        self,
        text: str,
        instruction: str,
    ) -> Dict[str, Any]:
        """
        Extracts structured information using
        the configured LLM.
        """

        prompt = self.build_prompt(
            text=text,
            instruction=instruction,
        )

        response = await self.llm_gateway.generate(
            prompt=prompt,
        )

        return {
            "instruction": instruction,
            "response": response,
        }
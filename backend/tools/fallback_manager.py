from __future__ import annotations

import logging
from typing import Any, Dict, List

from .base.base_tool import BaseTool

logger = logging.getLogger(__name__)


class FallbackManager:
    """
    Executes tools using a fallback mechanism.

    If the primary tool fails, the manager
    automatically tries the next available tool.
    """

    def __init__(
        self,
        tools: List[BaseTool],
    ) -> None:

        if not tools:
            raise ValueError(
                "FallbackManager requires at least one tool."
            )

        self.tools = tools

    # ---------------------------------------------------------
    # Execute
    # ---------------------------------------------------------

    async def execute(
        self,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        """
        Executes tools sequentially until one succeeds.

        Raises
        ------
        RuntimeError
            If every tool fails.
        """

        errors = []

        for tool in self.tools:

            try:

                logger.info(
                    "Trying tool: %s",
                    tool.name,
                )

                result = await tool.execute(**kwargs)

                logger.info(
                    "Tool '%s' executed successfully.",
                    tool.name,
                )

                return {
                    "provider": tool.name,
                    "result": result,
                }

            except Exception as exc:

                logger.exception(
                    "Tool '%s' failed.",
                    tool.name,
                )

                errors.append(
                    {
                        "provider": tool.name,
                        "error": str(exc),
                    }
                )

        raise RuntimeError(
            {
                "message": "All fallback providers failed.",
                "errors": errors,
            }
        )
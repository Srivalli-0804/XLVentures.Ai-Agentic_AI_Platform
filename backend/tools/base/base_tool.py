from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseTool(ABC):
    """
    Base class for all external tools.

    Every tool (Google News, Hunter, Crunchbase,
    LinkedIn, etc.) must inherit from this class.
    """

    def __init__(
        self,
        name: str,
        description: str,
        version: str = "1.0.0",
    ) -> None:

        self.name = name
        self.description = description
        self.version = version

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    async def execute(
        self,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        """
        Executes the tool.

        Child classes should not override this method.
        Implement _execute() instead.
        """

        self.validate(**kwargs)

        return await self._execute(**kwargs)

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    def validate(
        self,
        **kwargs: Any,
    ) -> None:
        """
        Override if the tool requires custom validation.
        """

        return

    # ---------------------------------------------------------
    # Tool Implementation
    # ---------------------------------------------------------

    @abstractmethod
    async def _execute(
        self,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        """
        Tool-specific implementation.
        """
        raise NotImplementedError

    # ---------------------------------------------------------
    # Metadata
    # ---------------------------------------------------------

    def get_metadata(self) -> Dict[str, Any]:
        """
        Returns metadata describing the tool.
        """

        return {
            "name": self.name,
            "description": self.description,
            "version": self.version,
        }

    # ---------------------------------------------------------
    # String Representation
    # ---------------------------------------------------------

    def __repr__(self) -> str:

        return (
            f"{self.__class__.__name__}"
            f"(name='{self.name}', version='{self.version}')"
        )
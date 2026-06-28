"""
Base Tool

Every external provider inherits from this class.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseTool(ABC):
    """
    Base class for every external provider.

    Example:
        GoogleNewsProvider
        CrunchbaseProvider
        ProxycurlProvider
    """

    name: str = "base_tool"

    @abstractmethod
    def validate(self) -> None:
        """
        Validate configuration such as API keys.
        """
        ...

    @abstractmethod
    def execute(self, *args: Any, **kwargs: Any) -> Any:
        """
        Execute the provider request.
        """
        ...
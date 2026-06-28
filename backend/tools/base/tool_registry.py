"""
Tool Registry

Maintains all available external providers.
"""

from __future__ import annotations

from backend.tools.base.base_tool import BaseTool


class ToolRegistry:
    """
    Registry for external providers.
    """

    def __init__(self) -> None:
        self._tools: dict[str, BaseTool] = {}

    def register(
        self,
        tool: BaseTool,
    ) -> None:
        """
        Register a tool by its name.
        """

        if tool.name in self._tools:
            raise ValueError(
                f"Tool '{tool.name}' already registered."
            )

        self._tools[tool.name] = tool

    def unregister(
        self,
        name: str,
    ) -> None:
        """
        Remove a registered tool.
        """

        self._tools.pop(name, None)

    def get(
        self,
        name: str,
    ) -> BaseTool:
        """
        Retrieve a tool by name.
        """

        if name not in self._tools:
            raise KeyError(
                f"No tool registered with name '{name}'."
            )

        return self._tools[name]

    def exists(
        self,
        name: str,
    ) -> bool:
        """
        Check whether a tool exists.
        """

        return name in self._tools

    def list_tools(self) -> list[str]:
        """
        Return all registered tool names.
        """

        return sorted(self._tools.keys())

    def clear(self) -> None:
        """
        Remove every registered tool.
        """

        self._tools.clear()


tool_registry = ToolRegistry()
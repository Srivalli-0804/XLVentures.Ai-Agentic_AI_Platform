from __future__ import annotations

from typing import Dict, List, Optional

from .base_tool import BaseTool


class ToolRegistry:
    """
    Central registry for all external tools.

    Tools register themselves here and can later
    be retrieved by agents.
    """

    def __init__(self) -> None:
        self._tools: Dict[str, BaseTool] = {}

    # ---------------------------------------------------------
    # Registration
    # ---------------------------------------------------------

    def register(self, tool: BaseTool) -> None:
        """
        Register a tool.

        Raises:
            ValueError if a tool with the same
            name already exists.
        """

        if tool.name in self._tools:
            raise ValueError(
                f"Tool '{tool.name}' is already registered."
            )

        self._tools[tool.name] = tool

    # ---------------------------------------------------------
    # Unregister
    # ---------------------------------------------------------

    def unregister(self, tool_name: str) -> None:
        """
        Removes a tool from the registry.
        """

        self._tools.pop(tool_name, None)

    # ---------------------------------------------------------
    # Lookup
    # ---------------------------------------------------------

    def get_tool(
        self,
        tool_name: str,
    ) -> Optional[BaseTool]:
        """
        Returns a registered tool.

        Returns None if the tool does not exist.
        """

        return self._tools.get(tool_name)

    # ---------------------------------------------------------
    # Listing
    # ---------------------------------------------------------

    def get_all_tools(self) -> List[BaseTool]:
        """
        Returns all registered tools.
        """

        return list(self._tools.values())

    def get_registered_tool_names(self) -> List[str]:
        """
        Returns the names of all registered tools.
        """

        return sorted(self._tools.keys())

    # ---------------------------------------------------------
    # Utility
    # ---------------------------------------------------------

    def is_registered(
        self,
        tool_name: str,
    ) -> bool:
        """
        Returns True if the tool is registered.
        """

        return tool_name in self._tools

    def clear(self) -> None:
        """
        Removes all registered tools.
        """

        self._tools.clear()

    def __contains__(
        self,
        tool_name: str,
    ) -> bool:

        return tool_name in self._tools

    def __len__(self) -> int:

        return len(self._tools)
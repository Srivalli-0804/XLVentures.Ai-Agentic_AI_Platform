"""
Agent Registry

Maintains a registry of all available business agents
mapped by capability.
"""

from __future__ import annotations

from typing import Any


class AgentRegistry:
    """
    Central registry for business agents.

    Agents register themselves using a capability name.

    Example:

        registry.register(
            "company_discovery",
            CompanyDiscoveryAgent()
        )
    """

    def __init__(self) -> None:
        self._agents: dict[str, Any] = {}

    def register(
        self,
        capability: str,
        agent: Any,
    ) -> None:
        """
        Register an agent.
        """

        if capability in self._agents:
            raise ValueError(
                f"Capability '{capability}' already registered."
            )

        self._agents[capability] = agent

    def unregister(
        self,
        capability: str,
    ) -> None:
        """
        Remove an agent.
        """

        self._agents.pop(capability, None)

    def get(
        self,
        capability: str,
    ) -> Any:
        """
        Retrieve an agent by capability.
        """

        if capability not in self._agents:
            raise KeyError(
                f"No agent registered for capability '{capability}'."
            )

        return self._agents[capability]

    def exists(
        self,
        capability: str,
    ) -> bool:
        """
        Check whether a capability exists.
        """

        return capability in self._agents

    def capabilities(
        self,
    ) -> list[str]:
        """
        Return all registered capabilities.
        """

        return sorted(self._agents.keys())

    def clear(self) -> None:
        """
        Remove every registered agent.
        """

        self._agents.clear()


agent_registry = AgentRegistry()
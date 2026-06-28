"""
Capability Router

Resolves workflow capabilities to registered business agents.
"""

from __future__ import annotations

from backend.agents.base.agent_registry import agent_registry


class CapabilityRouter:
    """
    Routes execution capabilities to registered agents.
    """

    def resolve(self, capability: str):
        """
        Resolve a capability into its registered agent.
        """

        return agent_registry.get(capability)

    def can_resolve(self, capability: str) -> bool:
        """
        Check whether a capability is registered.
        """

        return agent_registry.exists(capability)

    def available_capabilities(self) -> list[str]:
        """
        Return all registered capabilities.
        """

        return agent_registry.capabilities()


capability_router = CapabilityRouter()
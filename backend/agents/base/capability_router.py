from __future__ import annotations

import logging
from typing import List

from .agent_registry import AgentRegistry
from .base_agent import BaseAgent

logger = logging.getLogger(__name__)


class CapabilityRouter:
    """
    Routes requested capabilities to the appropriate agent.

    The Planner does not know agent names.
    It only requests capabilities.

    Example:
        capability = "company_discovery"

    Router:
        -> queries AgentRegistry
        -> finds matching agents
        -> selects one
        -> returns it
    """

    def __init__(self, registry: AgentRegistry):
        self.registry = registry

    # -----------------------------------------------------
    # Main Routing
    # -----------------------------------------------------

    def route(self, capability: str) -> BaseAgent:
        """
        Returns the most suitable agent
        for the requested capability.

        Raises:
            LookupError
            if no agent supports the capability.
        """

        agents = self.registry.get_agents_by_capability(capability)

        if not agents:
            raise LookupError(
                f"No registered agent found for capability '{capability}'."
            )

        selected_agent = self.select_best_agent(agents)

        logger.info(
            "Capability '%s' routed to '%s'",
            capability,
            selected_agent.name,
        )

        return selected_agent

    # -----------------------------------------------------
    # Strategy
    # -----------------------------------------------------

    def select_best_agent(
        self,
        agents: List[BaseAgent],
    ) -> BaseAgent:
        """
        Select the best agent among candidates.

        Current Strategy:
            Return the first registered agent.

        Future Strategies:
            - Priority based
            - Confidence based
            - Cost based
            - Load balancing
            - LLM planner decision
        """

        return agents[0]

    # -----------------------------------------------------
    # Utility
    # -----------------------------------------------------

    def supports(self, capability: str) -> bool:
        """
        Returns True if any registered
        agent supports this capability.
        """

        return (
            len(
                self.registry.get_agents_by_capability(capability)
            )
            > 0
        )

    def available_capabilities(self) -> List[str]:
        """
        Returns all unique capabilities
        currently available in the registry.
        """

        capabilities = set()

        for agent in self.registry.get_all_agents():
            capabilities.update(agent.capabilities)

        return sorted(capabilities)
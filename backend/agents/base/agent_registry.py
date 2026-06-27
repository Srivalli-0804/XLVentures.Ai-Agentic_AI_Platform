from __future__ import annotations

import logging
from typing import Dict, List, Optional

from .base_agent import BaseAgent

logger = logging.getLogger(__name__)


class AgentRegistry:
    """
    Central registry for all agents in the platform.

    The Planner never creates agents directly.
    Instead it queries this registry.

    This makes the platform easily extensible.
    """

    def __init__(self) -> None:
        self._agents: Dict[str, BaseAgent] = {}

    # ---------------------------------------------------------
    # Registration
    # ---------------------------------------------------------

    def register(self, agent: BaseAgent) -> None:
        """
        Register an agent.

        Raises:
            ValueError if an agent with the same
            name already exists.
        """

        if agent.name in self._agents:
            raise ValueError(
                f"Agent '{agent.name}' already registered."
            )

        self._agents[agent.name] = agent

        logger.info(f"Registered agent: {agent.name}")

    # ---------------------------------------------------------
    # Unregister
    # ---------------------------------------------------------

    def unregister(self, agent_name: str) -> None:
        """
        Remove an agent from registry.
        """

        if agent_name in self._agents:
            del self._agents[agent_name]

            logger.info(f"Unregistered agent: {agent_name}")

    # ---------------------------------------------------------
    # Lookup
    # ---------------------------------------------------------

    def get_agent(self, agent_name: str) -> Optional[BaseAgent]:
        """
        Returns an agent by name.
        """

        return self._agents.get(agent_name)

    # ---------------------------------------------------------
    # Capabilities
    # ---------------------------------------------------------

    def get_agents_by_capability(
        self,
        capability: str,
    ) -> List[BaseAgent]:
        """
        Returns all agents supporting
        a capability.
        """

        return [
            agent
            for agent in self._agents.values()
            if agent.can_handle(capability)
        ]

    # ---------------------------------------------------------
    # Listing
    # ---------------------------------------------------------

    def get_all_agents(self) -> List[BaseAgent]:
        """
        Returns all registered agents.
        """

        return list(self._agents.values())

    def get_registered_agent_names(self) -> List[str]:
        """
        Returns all registered agent names.
        """

        return list(self._agents.keys())

    # ---------------------------------------------------------
    # Utility
    # ---------------------------------------------------------

    def is_registered(self, agent_name: str) -> bool:
        """
        Check whether an agent exists.
        """

        return agent_name in self._agents

    def clear(self) -> None:
        """
        Clears the registry.
        """

        self._agents.clear()

        logger.info("Agent registry cleared.")

    def __len__(self) -> int:
        return len(self._agents)

    def __contains__(self, agent_name: str) -> bool:
        return agent_name in self._agents
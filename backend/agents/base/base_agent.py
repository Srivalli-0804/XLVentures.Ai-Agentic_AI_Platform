"""
Base Agent

Base class for all business agents.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from backend.agents.base.agent_context import AgentContext


class BaseAgent(ABC):
    """
    Base class for all agents.

    Business agents should only implement:

    - validate()
    - _run()
    """

    capability: str = "unknown"

    def execute(self, context: AgentContext) -> AgentContext:
        """
        Standard execution lifecycle.
        """

        self.validate(context)

        return self._run(context)

    @abstractmethod
    def validate(
        self,
        context: AgentContext,
    ) -> None:
        """
        Validate the input context.
        """
        ...

    @abstractmethod
    def _run(
        self,
        context: AgentContext,
    ) -> AgentContext:
        """
        Execute business logic.
        """
        ...
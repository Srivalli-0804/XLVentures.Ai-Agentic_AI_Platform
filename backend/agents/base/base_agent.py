from __future__ import annotations

import time
import logging
from abc import ABC, abstractmethod
from typing import List

from .agent_context import AgentContext


class BaseAgent(ABC):
    """
    Abstract base class for all agents in the Prospect Intelligence Platform.

    Every business agent must inherit from this class.

    Responsibilities:
    - Common execution lifecycle
    - Logging
    - Validation
    - Metadata
    - Capability management
    """

    def __init__(
        self,
        name: str,
        description: str,
        capabilities: List[str],
        version: str = "1.0.0",
    ) -> None:

        self.name = name
        self.description = description

        # Immutable metadata
        self.capabilities = tuple(capabilities)

        self.version = version

        # Agent-specific logger
        self.logger = logging.getLogger(self.__class__.__name__)

    # ---------------------------------------------------------
    # Public Execution Lifecycle
    # ---------------------------------------------------------

    async def execute(self, context: AgentContext) -> AgentContext:
        """
        Executes the complete lifecycle of an agent.

        Business agents should NOT override this method.

        Lifecycle:
            validate()
                ↓
            _run()
                ↓
            return updated context
        """

        self.logger.info("Execution Started")

        start_time = time.perf_counter()

        try:

            self.validate(context)

            updated_context = await self._run(context)

            execution_time = round(
                time.perf_counter() - start_time,
                3,
            )

            self.logger.info(
                "Execution Completed in %.3f seconds",
                execution_time,
            )

            return updated_context

        except Exception as ex:

            self.logger.exception(
                "Execution Failed: %s",
                str(ex),
            )

            raise

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    def validate(self, context: AgentContext) -> None:
        """
        Performs validation before execution.

        Child agents may override this method if
        additional validation is required.
        """

        if context is None:
            raise ValueError("AgentContext cannot be None.")

    # ---------------------------------------------------------
    # Business Logic
    # ---------------------------------------------------------

    @abstractmethod
    async def _run(
        self,
        context: AgentContext,
    ) -> AgentContext:
        """
        Business logic for the agent.

        Must be implemented by every child agent.
        """
        raise NotImplementedError

    # ---------------------------------------------------------
    # Capability Check
    # ---------------------------------------------------------

    def can_handle(self, capability: str) -> bool:
        """
        Returns True if this agent supports
        the requested capability.
        """

        return capability in self.capabilities

    # ---------------------------------------------------------
    # Metadata
    # ---------------------------------------------------------

    def get_metadata(self) -> dict:
        """
        Returns metadata describing this agent.
        """

        return {
            "name": self.name,
            "description": self.description,
            "version": self.version,
            "capabilities": list(self.capabilities),
        }

    # ---------------------------------------------------------
    # String Representation
    # ---------------------------------------------------------

    def __repr__(self) -> str:

        return (
            f"{self.__class__.__name__}"
            f"(name='{self.name}', version='{self.version}')"
        )
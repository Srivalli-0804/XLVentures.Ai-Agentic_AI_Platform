"""
ICP Qualifier Agent

Filters discovered companies using the configured
Ideal Customer Profile (ICP).
"""

from __future__ import annotations

from backend.agents.base.base_agent import BaseAgent
from backend.agents.base.agent_context import AgentContext
from backend.tools.base.tool_registry import tool_registry


class ICPQualifierAgent(BaseAgent):
    """
    Qualifies discovered companies.
    """

    capability = "qualification"

    def validate(
        self,
        context: AgentContext,
    ) -> None:

        if context is None:
            raise ValueError("AgentContext is required.")

    def _run(
        self,
        context: AgentContext,
    ) -> AgentContext:

        provider = tool_registry.get("icp")

        qualified = provider.execute(
            context.discovered_companies
        )

        context.qualified_companies.extend(
            qualified
        )

        return context
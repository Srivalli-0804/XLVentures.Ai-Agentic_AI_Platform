"""
Company Scoring Agent

Assigns priority scores to qualified companies.
"""

from __future__ import annotations

from backend.agents.base.base_agent import BaseAgent
from backend.agents.base.agent_context import AgentContext
from backend.tools.base.tool_registry import tool_registry


class CompanyScoringAgent(BaseAgent):

    capability = "company_scoring"

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

        provider = tool_registry.get("score")

        scored = provider.execute(
            context.qualified_companies
        )

        context.scored_companies = scored

        return context
"""
Company Discovery Agent

Discovers companies from trigger events.
"""

from __future__ import annotations

from backend.agents.base.base_agent import BaseAgent
from backend.agents.base.agent_context import AgentContext
from backend.tools.base.tool_registry import tool_registry


class CompanyDiscoveryAgent(BaseAgent):
    """
    Discovers companies using the registered provider.
    """

    capability = "company_discovery"

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

        provider = tool_registry.get("crunchbase")

        trigger_events = context.get_metadata("trigger_events")

        companies = provider.execute(trigger_events)

        context.discovered_companies.extend(companies)

        return context
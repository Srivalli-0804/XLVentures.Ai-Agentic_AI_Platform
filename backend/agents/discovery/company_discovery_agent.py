from __future__ import annotations

from typing import Any, Dict, List

from ..base.base_agent import BaseAgent
from ..base.agent_context import AgentContext


class CompanyDiscoveryAgent(BaseAgent):
    """
    Discovers companies that match the configured
    Ideal Customer Profile (ICP).

    For the hackathon, this agent generates sample
    company data. Later it will integrate with
    Google News, Crunchbase, LinkedIn, etc.
    """

    def __init__(self) -> None:
        super().__init__(
            name="Company Discovery Agent",
            description="Discovers companies matching the configured ICP.",
            capabilities=["company_discovery"],
        )

    def validate(self, context: AgentContext) -> None:
        super().validate(context)

        if not context.icp:
            raise ValueError(
                "ICP configuration is missing."
            )

    async def _run(
        self,
        context: AgentContext,
    ) -> AgentContext:

        discovered_companies: List[Dict[str, Any]] = []

        industry = context.icp.get("industry", "Unknown")
        location = context.icp.get("location", "Unknown")

        trigger_events = context.metadata.get(
            "trigger_events",
            [],
        )

        for index, event in enumerate(trigger_events, start=1):

            discovered_companies.append(
                {
                    "company_id": f"CMP-{index:03}",
                    "name": f"Company {index}",
                    "industry": industry,
                    "location": location,
                    "trigger": event["trigger"],
                    "status": "DISCOVERED",
                }
            )

        context.discovered_companies = discovered_companies

        return context
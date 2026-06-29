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

        industry = context.icp.get("industry", "SaaS")
        location = context.icp.get("location", "United States")

        context.discovered_companies = [
        {
            "company_id": "CMP-001",
            "name": "Company 1",
            "industry": industry,
            "location": location,
            "status": "DISCOVERED",
            "score": 76,
        },
        {
            "company_id": "CMP-002",
            "name": "Company 2",
            "industry": industry,
            "location": location,
            "status": "DISCOVERED",
            "score": 82,
        },
        {
            "company_id": "CMP-003",
            "name": "Company 3",
            "industry": industry,
            "location": location,
            "status": "DISCOVERED",
            "score": 91,
        },
]
        context.add_execution_step(
            self.name,
            "SUCCESS",
            "company_discovery",
        )

        return context
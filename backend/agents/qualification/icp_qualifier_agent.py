from __future__ import annotations

from typing import Any, Dict, List

from ..base.base_agent import BaseAgent
from ..base.agent_context import AgentContext


class ICPQualifierAgent(BaseAgent):
    """
    Qualifies discovered companies against the
    configured Ideal Customer Profile (ICP).
    """

    def __init__(self) -> None:
        super().__init__(
            name="ICP Qualifier Agent",
            description="Filters companies that match the configured ICP.",
            capabilities=["qualification"],
        )

    def validate(self, context: AgentContext) -> None:
        super().validate(context)

        if not context.discovered_companies:
            raise ValueError(
                "No discovered companies available."
            )

        if not context.icp:
            raise ValueError(
                "ICP configuration is missing."
            )

    async def _run(
        self,
        context: AgentContext,
    ) -> AgentContext:

        qualified_companies: List[Dict[str, Any]] = []
        rejected_companies: List[Dict[str, Any]] = []

        icp_industry = context.icp.get("industry")
        icp_location = context.icp.get("location")

        for company in context.discovered_companies:

            industry_match = (
                icp_industry is None
                or company.get("industry") == icp_industry
            )

            location_match = (
                icp_location is None
                or company.get("location") == icp_location
            )

            if industry_match and location_match:
                company["qualification_status"] = "QUALIFIED"
                qualified_companies.append(company)
            else:
                company["qualification_status"] = "REJECTED"
                rejected_companies.append(company)

        context.qualified_companies = qualified_companies
        context.rejected_companies = rejected_companies

        return context
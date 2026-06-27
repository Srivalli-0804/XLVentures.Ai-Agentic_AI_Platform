from __future__ import annotations

from typing import Dict, List

from ..base.base_agent import BaseAgent
from ..base.agent_context import AgentContext


class OutreachRecommenderAgent(BaseAgent):
    """
    Generates outreach recommendations for validated
    contacts and shortlisted companies.
    """

    def __init__(self) -> None:
        super().__init__(
            name="Outreach Recommender Agent",
            description="Generates outreach recommendations.",
            capabilities=["outreach_recommendation"],
        )

    def validate(self, context: AgentContext) -> None:
        super().validate(context)

        if not context.contacts:
            raise ValueError(
                "No contacts available for recommendation."
            )

        if not context.qualified_companies:
            raise ValueError(
                "No qualified companies available."
            )

    async def _run(
        self,
        context: AgentContext,
    ) -> AgentContext:

        recommendations: List[Dict] = []

        company_lookup = {
            company["company_id"]: company
            for company in context.qualified_companies
        }

        for contact in context.contacts:

            if not contact.get("is_valid"):
                continue

            company = company_lookup.get(
                contact["company_id"]
            )

            if company is None:
                continue

            recommendation = {
                "company_id": company["company_id"],
                "company_name": company["name"],
                "contact_id": contact["contact_id"],
                "contact_name": contact["name"],
                "designation": contact["designation"],
                "prospect_score": company.get(
                    "prospect_score",
                    0,
                ),
                "priority": (
                    "HIGH"
                    if company.get("prospect_score", 0) >= 85
                    else "MEDIUM"
                ),
                "recommended_channel": "LinkedIn",
                "status": "RECOMMENDED",
            }

            recommendations.append(recommendation)

        context.recommendations = recommendations

        return context
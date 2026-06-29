from __future__ import annotations

from typing import Dict, List

from ..base.base_agent import BaseAgent
from ..base.agent_context import AgentContext


class CompanyEnrichmentAgent(BaseAgent):
    """
    Enriches shortlisted companies with additional
    company-level information.

    Future implementation will integrate with:
        - Crunchbase
        - BuiltWith
        - Clearbit
        - Company Websites
    """

    def __init__(self) -> None:
        super().__init__(
            name="Company Enrichment Agent",
            description="Enriches company profiles.",
            capabilities=["company_enrichment"],
        )

    def validate(self, context: AgentContext) -> None:
        super().validate(context)

        if not context.qualified_companies:
            raise ValueError(
                "No qualified companies available for enrichment."
            )

    async def _run(
        self,
        context: AgentContext,
    ) -> AgentContext:

        enriched_profiles: List[Dict] = []

        for company in context.qualified_companies:

            profile = {
                "company_id": company["company_id"],
                "company_name": company["name"],
                "industry": company["industry"],
                "location": company["location"],
                "prospect_score": company.get("prospect_score", 0),
                "website": f"https://{company['name'].lower().replace(' ', '')}.com",
                "employee_count": 250,
                "funding_stage": "Series A",
                "annual_revenue": "$10M - $25M",
                "tech_stack": [
                    "React",
                    "FastAPI",
                    "PostgreSQL",
                    "AWS",
                ],
                "company_status": "ACTIVE",
            }

            enriched_profiles.append(profile)

        context.company_profiles = enriched_profiles

        return context
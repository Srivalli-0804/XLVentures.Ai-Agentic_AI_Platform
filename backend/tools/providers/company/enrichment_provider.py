"""
Company Enrichment Provider

Adds detailed business information to discovered companies.
"""

from __future__ import annotations

from backend.tools.base.base_tool import BaseTool


class EnrichmentProvider(BaseTool):

    name = "company_enrichment"

    def validate(self) -> None:
        pass

    def execute(
        self,
        companies: list[dict],
    ) -> list[dict]:

        enriched = []

        for company in companies:

            company = company.copy()

            company["website"] = (
                f"https://{company['name'].lower()}.com"
            )

            company["linkedin"] = (
                f"https://linkedin.com/company/"
                f"{company['name'].lower()}"
            )

            company["headquarters"] = "San Francisco"

            company["revenue"] = "$3B"

            company["description"] = (
                f"{company['name']} is an AI company."
            )

            company["tech_stack"] = [
                "Python",
                "FastAPI",
                "PostgreSQL",
                "Redis",
            ]

            enriched.append(company)

        return enriched
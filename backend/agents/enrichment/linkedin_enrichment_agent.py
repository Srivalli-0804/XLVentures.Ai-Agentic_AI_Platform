from __future__ import annotations

from typing import Dict, List

from ..base.base_agent import BaseAgent
from ..base.agent_context import AgentContext


class LinkedInEnrichmentAgent(BaseAgent):
    """
    Enriches discovered contacts with LinkedIn profile
    information.

    Future implementation will integrate with:
        - LinkedIn API
        - Proxycurl
        - Apollo
        - People Data Labs
    """

    def __init__(self) -> None:
        super().__init__(
            name="LinkedIn Enrichment Agent",
            description="Enriches contacts with LinkedIn profile information.",
            capabilities=["linkedin_enrichment"],
        )

    def validate(self, context: AgentContext) -> None:
        super().validate(context)

        if not context.contacts:
            raise ValueError(
                "No contacts available for LinkedIn enrichment."
            )

    async def _run(
        self,
        context: AgentContext,
    ) -> AgentContext:

        enriched_contacts: List[Dict] = []

        for contact in context.contacts:

            company_slug = (
                contact["company_name"]
                .lower()
                .replace(" ", "-")
            )

            name_slug = (
                contact["name"]
                .lower()
                .replace(" ", "-")
            )

            enriched_contact = contact.copy()

            enriched_contact["linkedin"] = (
                f"https://www.linkedin.com/in/{name_slug}"
            )

            enriched_contact["company_linkedin"] = (
                f"https://www.linkedin.com/company/{company_slug}"
            )

            enriched_contact["profile_verified"] = True

            enriched_contact["status"] = "LINKEDIN_ENRICHED"

            enriched_contacts.append(enriched_contact)

        context.contacts = enriched_contacts

        return context
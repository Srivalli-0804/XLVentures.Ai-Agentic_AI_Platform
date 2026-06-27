from __future__ import annotations

from typing import Dict, List

from ..base.base_agent import BaseAgent
from ..base.agent_context import AgentContext


class ContactDiscoveryAgent(BaseAgent):
    """
    Discovers key decision-makers for enriched companies.

    Future implementation will integrate with:
        - LinkedIn
        - Apollo
        - Hunter
        - Proxycurl
    """

    DEFAULT_PERSONAS = [
        "CEO",
        "CTO",
        "VP Engineering",
        "Head of HR",
    ]

    def __init__(self) -> None:
        super().__init__(
            name="Contact Discovery Agent",
            description="Discovers decision-makers for shortlisted companies.",
            capabilities=["contact_discovery"],
        )

    def validate(self, context: AgentContext) -> None:
        super().validate(context)

        if not context.company_profiles:
            raise ValueError(
                "No enriched company profiles available."
            )

    async def _run(
        self,
        context: AgentContext,
    ) -> AgentContext:

        contacts: List[Dict] = []

        personas = (
            context.target_personas
            if context.target_personas
            else self.DEFAULT_PERSONAS
        )

        for company in context.company_profiles:

            for index, persona in enumerate(personas, start=1):

                first_name = persona.split()[0]

                contacts.append(
                    {
                        "contact_id": (
                            f"{company['company_id']}-"
                            f"CONTACT-{index:02}"
                        ),
                        "company_id": company["company_id"],
                        "company_name": company["company_name"],
                        "name": (
                            f"{first_name} "
                            f"{company['company_name']}"
                        ),
                        "designation": persona,
                        "email": None,
                        "phone": None,
                        "linkedin": None,
                        "status": "DISCOVERED",
                    }
                )

        context.contacts = contacts

        return context
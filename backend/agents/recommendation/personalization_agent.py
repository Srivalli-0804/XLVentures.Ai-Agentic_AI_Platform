from __future__ import annotations

from typing import Dict, List

from ..base.base_agent import BaseAgent
from ..base.agent_context import AgentContext


class PersonalizationAgent(BaseAgent):
    """
    Generates personalized outreach messages for each
    recommended prospect.

    Future implementation will use LLMs to generate
    highly personalized outreach based on company news,
    market signals, LinkedIn profiles, and ICP.
    """

    def __init__(self) -> None:
        super().__init__(
            name="Personalization Agent",
            description="Generates personalized outreach messages.",
            capabilities=["personalization"],
        )

    def validate(self, context: AgentContext) -> None:
        super().validate(context)

        if not context.recommendations:
            raise ValueError(
                "No recommendations available for personalization."
            )

    async def _run(
        self,
        context: AgentContext,
    ) -> AgentContext:

        personalized_recommendations: List[Dict] = []

        company_lookup = {
            company["company_id"]: company
            for company in context.company_profiles
        }

        for recommendation in context.recommendations:

            personalized = recommendation.copy()

            company = company_lookup.get(
                recommendation["company_id"],
                {},
            )

            personalized["subject"] = (
                f"Helping {recommendation['company_name']} "
                "Scale Faster with AI"
            )

            personalized["message"] = (
                f"Hi {recommendation['contact_name']}, "
                f"I noticed that {recommendation['company_name']} "
                f"is growing in the {company.get('industry', 'technology')} "
                "space. I believe our AI platform can help improve "
                "prospect discovery and sales efficiency."
            )

            personalized["call_to_action"] = (
                "Would you be available for a quick 15-minute discussion?"
            )

            personalized["personalization_status"] = "GENERATED"

            personalized_recommendations.append(personalized)

        context.recommendations = personalized_recommendations

        return context
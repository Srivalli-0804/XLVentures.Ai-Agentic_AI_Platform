from __future__ import annotations

from typing import Dict, List

from ..base.base_agent import BaseAgent
from ..base.agent_context import AgentContext


class NextActionAgent(BaseAgent):
    """
    Determines the next best action for every
    personalized recommendation.

    Future implementation may use:
        - LLM reasoning
        - CRM history
        - Previous outreach history
        - Customer engagement metrics
    """

    HIGH_PRIORITY_THRESHOLD = 85

    def __init__(self) -> None:
        super().__init__(
            name="Next Action Agent",
            description="Determines the next best action for every recommendation.",
            capabilities=["next_action"],
        )

    def validate(self, context: AgentContext) -> None:
        super().validate(context)

        if not context.recommendations:
            raise ValueError(
                "No recommendations available."
            )

    async def _run(
        self,
        context: AgentContext,
    ) -> AgentContext:

        updated_recommendations: List[Dict] = []

        for recommendation in context.recommendations:

            recommendation = recommendation.copy()

            score = recommendation.get(
                "prospect_score",
                0,
            )

            if score >= self.HIGH_PRIORITY_THRESHOLD:

                recommendation["next_action"] = {
                    "action": "CONNECT_ON_LINKEDIN",
                    "priority": "HIGH",
                    "timeline": "Within 24 Hours",
                    "reason": (
                        "High-value prospect with strong qualification score."
                    ),
                }

            elif score >= 70:

                recommendation["next_action"] = {
                    "action": "SEND_EMAIL",
                    "priority": "MEDIUM",
                    "timeline": "Within 2 Days",
                    "reason": (
                        "Qualified prospect suitable for email outreach."
                    ),
                }

            else:

                recommendation["next_action"] = {
                    "action": "FOLLOW_UP_LATER",
                    "priority": "LOW",
                    "timeline": "Within 1 Week",
                    "reason": (
                        "Prospect requires additional monitoring before outreach."
                    ),
                }

            recommendation["workflow_status"] = "READY_FOR_APPROVAL"

            updated_recommendations.append(recommendation)

        context.recommendations = updated_recommendations

        return context
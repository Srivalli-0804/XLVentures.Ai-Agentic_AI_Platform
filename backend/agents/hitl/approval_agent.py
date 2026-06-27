from __future__ import annotations

from typing import Dict, List

from ..base.base_agent import BaseAgent
from ..base.agent_context import AgentContext


class ApprovalAgent(BaseAgent):
    """
    Handles the Human-in-the-Loop (HITL) approval process.

    Every recommendation is marked as pending approval.
    A human reviewer can later approve or reject the
    recommendation through the frontend.
    """

    def __init__(self) -> None:
        super().__init__(
            name="Approval Agent",
            description="Prepares recommendations for human approval.",
            capabilities=["approval"],
        )

    def validate(self, context: AgentContext) -> None:
        super().validate(context)

        if not context.recommendations:
            raise ValueError(
                "No recommendations available for approval."
            )

    async def _run(
        self,
        context: AgentContext,
    ) -> AgentContext:

        approval_queue: List[Dict] = []

        updated_recommendations: List[Dict] = []

        for recommendation in context.recommendations:

            recommendation = recommendation.copy()

            recommendation["approval_status"] = "PENDING"

            approval_record = {
                "recommendation_id": recommendation["contact_id"],
                "company_name": recommendation["company_name"],
                "contact_name": recommendation["contact_name"],
                "priority": recommendation["priority"],
                "status": "PENDING",
                "reviewed_by": None,
                "reviewed_at": None,
                "comments": None,
            }

            approval_queue.append(approval_record)

            updated_recommendations.append(recommendation)

        context.recommendations = updated_recommendations

        context.approvals = approval_queue

        context.metadata["approval_summary"] = {
            "total_pending": len(approval_queue),
            "approved": 0,
            "rejected": 0,
        }

        return context
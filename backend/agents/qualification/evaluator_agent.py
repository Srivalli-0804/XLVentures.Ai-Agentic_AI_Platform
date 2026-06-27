from __future__ import annotations

from typing import Dict, List

from ..base.base_agent import BaseAgent
from ..base.agent_context import AgentContext


class EvaluatorAgent(BaseAgent):
    """
    Evaluates scored companies and determines which
    companies should proceed to the enrichment phase.
    """

    DEFAULT_THRESHOLD = 70

    def __init__(self) -> None:
        super().__init__(
            name="Evaluator Agent",
            description="Evaluates scored companies against the qualification threshold.",
            capabilities=["evaluation"],
        )

    def validate(self, context: AgentContext) -> None:
        super().validate(context)

        if not context.qualified_companies:
            raise ValueError(
                "No qualified companies available for evaluation."
            )

    async def _run(
        self,
        context: AgentContext,
    ) -> AgentContext:

        shortlisted_companies: List[Dict] = []
        rejected_companies: List[Dict] = []

        threshold = context.metadata.get(
            "qualification_threshold",
            self.DEFAULT_THRESHOLD,
        )

        for company in context.qualified_companies:

            score = company.get("prospect_score", 0)

            if score >= threshold:

                company["evaluation_status"] = "SHORTLISTED"

                shortlisted_companies.append(company)

            else:

                company["evaluation_status"] = "REJECTED"

                rejected_companies.append(company)

        context.qualified_companies = shortlisted_companies

        context.rejected_companies.extend(rejected_companies)

        context.metadata["evaluation_summary"] = {
            "threshold": threshold,
            "shortlisted": len(shortlisted_companies),
            "rejected": len(rejected_companies),
        }

        return context
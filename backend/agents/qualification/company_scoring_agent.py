from __future__ import annotations

from typing import Dict, List

from ..base.base_agent import BaseAgent
from ..base.agent_context import AgentContext


class CompanyScoringAgent(BaseAgent):
    """
    Assigns a prospect score to each qualified company
    based on ICP matching and market signals.
    """

    def __init__(self) -> None:
        super().__init__(
            name="Company Scoring Agent",
            description="Calculates prospect scores for qualified companies.",
            capabilities=["company_scoring"],
        )

    def validate(self, context: AgentContext) -> None:
        super().validate(context)

        if not context.qualified_companies:
            raise ValueError(
                "No qualified companies available for scoring."
            )

    async def _run(
        self,
        context: AgentContext,
    ) -> AgentContext:

        market_signal_lookup = {
            signal["company_id"]: signal
            for signal in context.market_signals
        }

        scored_companies: List[Dict] = []

        for company in context.qualified_companies:

            # Base discovery score
            score = company.get("score", 0)

            signal = market_signal_lookup.get(
                company["company_id"]
            )

            # ----------------------------
            # Industry Match
            # ----------------------------

            company_industry = company.get("industry")
            icp_industry = context.icp.get("industry")

            if company_industry == icp_industry:
                score += 5

            # ----------------------------
            # Location Match
            # ----------------------------

            if (
                company.get("location")
                == context.icp.get("location")
            ):
                score += 5

            # ----------------------------
            # Market Signal
            # ----------------------------

            if signal:

                confidence = signal.get(
                    "confidence_score",
                    0,
                )

                score += int(confidence * 5)

                company["market_signal"] = signal

            # Keep score between 0 and 100
            score = min(score, 100)

            company["prospect_score"] = score

            scored_companies.append(company)

        scored_companies.sort(
            key=lambda company: company["prospect_score"],
            reverse=True,
        )

        print("\n========== COMPANY SCORES ==========")

        for company in scored_companies:
            print(
                f"{company['name']}  ->  "
                f"{company['prospect_score']}  "
                f"(confidence={company['market_signal']['confidence_score']})"
            )

        print("====================================\n")

        context.qualified_companies = scored_companies

        return context
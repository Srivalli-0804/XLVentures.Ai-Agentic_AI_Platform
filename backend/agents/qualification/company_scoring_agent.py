from __future__ import annotations

from typing import Dict, List

from ..base.base_agent import BaseAgent
from ..base.agent_context import AgentContext


class CompanyScoringAgent(BaseAgent):
    """
    Assigns a prospect score to each qualified company
    based on the configured ICP and discovered market
    signals.
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

            score = 0

            signal = market_signal_lookup.get(
                company["company_id"]
            )

            # ------------------------------------------
            # Industry Match
            # ------------------------------------------

            if (
                company.get("industry")
                == context.icp.get("industry")
            ):
                score += 40

            # ------------------------------------------
            # Location Match
            # ------------------------------------------

            if (
                company.get("location")
                == context.icp.get("location")
            ):
                score += 20

            # ------------------------------------------
            # Market Signal Confidence
            # ------------------------------------------

            if signal:

                confidence = signal.get(
                    "confidence_score",
                    0,
                )

                score += int(confidence * 40)

                company["market_signal"] = signal

            company["prospect_score"] = min(score, 100)

            scored_companies.append(company)

        scored_companies.sort(
            key=lambda company: company["prospect_score"],
            reverse=True,
        )

        context.qualified_companies = scored_companies

        return context
from __future__ import annotations

from typing import Any, Dict, List

from ..base.base_agent import BaseAgent
from ..base.agent_context import AgentContext


class MarketSignalAgent(BaseAgent):
    """
    Generates market signals for discovered companies.
    """

    def __init__(self) -> None:
        super().__init__(
            name="Market Signal Agent",
            description="Analyzes market signals for discovered companies.",
            capabilities=["market_signal_analysis"],
        )

    def validate(self, context: AgentContext) -> None:
        super().validate(context)

        if not context.discovered_companies:
            raise ValueError(
                "No discovered companies available."
            )

    async def _run(
        self,
        context: AgentContext,
    ) -> AgentContext:

        market_signals: List[Dict[str, Any]] = []

        for company in context.discovered_companies:

            base_score = company.get("score", 70)

            # Convert discovery score into confidence
            confidence = round(base_score / 100, 2)

            if base_score >= 90:
                signal_type = "Funding"
                strength = "Very High"

            elif base_score >= 80:
                signal_type = "Expansion"
                strength = "High"

            else:
                signal_type = "Hiring"
                strength = "Medium"

            signal = {
                "company_id": company["company_id"],
                "company_name": company["name"],
                "signal_type": signal_type,
                "signal_strength": strength,
                "confidence_score": confidence,
                "summary": (
                    f"{company['name']} shows "
                    f"{signal_type.lower()} signals."
                ),
            }

            market_signals.append(signal)

        context.market_signals = market_signals

        return context
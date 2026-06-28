"""
Score Provider

Assigns a priority score to qualified companies.

(Currently uses simple rule-based scoring.)
"""

from __future__ import annotations

from backend.tools.base.base_tool import BaseTool


class ScoreProvider(BaseTool):
    """
    Mock scoring provider.
    """

    name = "score"

    def validate(self) -> None:
        pass

    def execute(self, companies: list[dict]) -> list[dict]:

        scored = []

        for company in companies:

            score = 0

            if company["industry"] == "Artificial Intelligence":
                score += 40

            if company["country"] == "USA":
                score += 20

            if company["employees"] >= 500:
                score += 20

            if company.get("trigger") == "Funding Round":
                score += 20

            company = company.copy()
            company["score"] = score

            scored.append(company)

        return scored
"""
ICP Provider

Determines whether a company matches the
Ideal Customer Profile (ICP).

(Currently returns mock results.)
"""

from __future__ import annotations

from backend.tools.base.base_tool import BaseTool


class ICPProvider(BaseTool):
    """
    Mock ICP provider.
    """

    name = "icp"

    def validate(self) -> None:
        """
        Validate provider configuration.
        """
        pass

    def execute(self, companies: list[dict]) -> list[dict]:
        """
        Filter companies based on a simple ICP.

        ICP Rules:
        - Industry must be Artificial Intelligence
        - Country must be USA
        - Employees >= 500
        """

        qualified = []

        for company in companies:

            if (
                company["industry"] == "Artificial Intelligence"
                and company["country"] == "USA"
                and company["employees"] >= 500
            ):
                qualified.append(company)

        return qualified
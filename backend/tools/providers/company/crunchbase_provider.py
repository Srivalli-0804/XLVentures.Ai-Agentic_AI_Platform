"""
Crunchbase Provider

Fetches company information.

(Currently returns mock data.)
"""

from __future__ import annotations

from backend.tools.base.base_tool import BaseTool


class CrunchbaseProvider(BaseTool):
    """
    Mock Crunchbase provider.
    """

    name = "crunchbase"

    def validate(self) -> None:
        """
        Validate provider configuration.
        """
        pass

    def execute(self, trigger_events: list[dict]):
        """
        Return discovered companies.
        """

        companies = []

        for event in trigger_events:

            companies.append(
                {
                    "name": event["company"],
                    "industry": "Artificial Intelligence",
                    "country": "USA",
                    "employees": 1000,
                    "trigger": event["event"],
                }
            )

        return companies
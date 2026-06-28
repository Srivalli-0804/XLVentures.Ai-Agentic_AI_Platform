"""
Google News Provider

Fetches company trigger events from Google News.

(Currently returns mock data.)
"""

from __future__ import annotations

from backend.tools.base.base_tool import BaseTool


class GoogleNewsProvider(BaseTool):
    """
    Mock Google News provider.
    """

    name = "google_news"

    def validate(self) -> None:
        """
        Validate provider configuration.

        Later:
            Check GOOGLE_NEWS_API_KEY
        """
        pass

    def execute(self, company: str | None = None):
        """
        Return trigger events.

        Later this will call the actual API.
        """

        data = [
            {
                "company": "OpenAI",
                "event": "Funding Round",
                "source": "Google News",
            },
            {
                "company": "Anthropic",
                "event": "Hiring Surge",
                "source": "Google News",
            },
        ]

        if company:

            return [
                event
                for event in data
                if event["company"].lower()
                == company.lower()
            ]

        return data
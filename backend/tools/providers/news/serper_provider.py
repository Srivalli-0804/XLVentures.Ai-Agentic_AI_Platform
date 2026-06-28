from __future__ import annotations

from typing import Any, Dict, List

from ...base.base_tool import BaseTool


class SerperProvider(BaseTool):
    """
    Mock Serper provider.

    Simulates Google Search results for a company.

    Future implementation:
        - Serper API
        - Google Custom Search
    """

    def __init__(self) -> None:
        super().__init__(
            name="Serper Provider",
            description="Searches public web results for companies.",
        )

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    def validate(
        self,
        **kwargs: Any,
    ) -> None:

        query = kwargs.get("query")

        if not query:
            raise ValueError(
                "Parameter 'query' is required."
            )

    # ---------------------------------------------------------
    # Tool Implementation
    # ---------------------------------------------------------

    async def _execute(
        self,
        **kwargs: Any,
    ) -> Dict[str, Any]:

        query = kwargs["query"]

        search_results: List[Dict[str, Any]] = [
            {
                "title": f"{query} raises Series B funding",
                "url": f"https://example.com/{query.lower().replace(' ', '-')}/funding",
                "snippet": "Company announces successful Series B investment."
            },
            {
                "title": f"{query} hiring software engineers",
                "url": f"https://careers.example.com/{query.lower().replace(' ', '-')}",
                "snippet": "Multiple engineering positions are currently open."
            },
            {
                "title": f"{query} launches AI platform",
                "url": f"https://blog.example.com/{query.lower().replace(' ', '-')}",
                "snippet": "New AI-powered platform released for enterprise customers."
            },
        ]

        return {
            "provider": self.name,
            "query": query,
            "results": search_results,
            "total_results": len(search_results),
        }
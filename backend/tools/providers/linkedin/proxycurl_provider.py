from __future__ import annotations

from typing import Any, Dict, List

from ...base.base_tool import BaseTool


class ProxycurlProvider(BaseTool):
    """
    Mock Proxycurl provider.

    Simulates retrieval of decision makers from LinkedIn.

    Future implementation:
        - Proxycurl Person API
        - Proxycurl Company API
    """

    def __init__(self) -> None:
        super().__init__(
            name="Proxycurl Provider",
            description="Retrieves decision makers and LinkedIn profiles.",
        )

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    def validate(
        self,
        **kwargs: Any,
    ) -> None:

        company = kwargs.get("company")

        if not company:
            raise ValueError(
                "Parameter 'company' is required."
            )

    # ---------------------------------------------------------
    # Tool Implementation
    # ---------------------------------------------------------

    async def _execute(
        self,
        **kwargs: Any,
    ) -> Dict[str, Any]:

        company = kwargs["company"]

        contacts: List[Dict[str, Any]] = [
            {
                "id": "CNT-001",
                "name": "Sarah Johnson",
                "designation": "Chief Technology Officer",
                "department": "Technology",
                "company": company,
                "linkedin": "https://linkedin.com/in/sarah-johnson",
                "experience": "12 years",
                "location": "San Francisco, USA",
            },
            {
                "id": "CNT-002",
                "name": "Michael Brown",
                "designation": "VP Engineering",
                "department": "Engineering",
                "company": company,
                "linkedin": "https://linkedin.com/in/michael-brown",
                "experience": "10 years",
                "location": "New York, USA",
            },
            {
                "id": "CNT-003",
                "name": "Emily Davis",
                "designation": "Head of HR",
                "department": "Human Resources",
                "company": company,
                "linkedin": "https://linkedin.com/in/emily-davis",
                "experience": "8 years",
                "location": "Austin, USA",
            },
        ]

        return {
            "provider": self.name,
            "company": company,
            "contacts": contacts,
            "total_contacts": len(contacts),
        }
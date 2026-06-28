from __future__ import annotations

from typing import Any, Dict

from ...base.base_tool import BaseTool


class CrunchbaseProvider(BaseTool):
    """
    Mock Crunchbase provider.

    Simulates company information returned by Crunchbase.

    Future implementation:
        - Crunchbase REST API
        - Company enrichment APIs
    """

    def __init__(self) -> None:
        super().__init__(
            name="Crunchbase Provider",
            description="Retrieves company profile and funding information.",
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

        return {
            "provider": self.name,
            "company": {
                "id": "CMP-001",
                "name": company,
                "website": f"https://{company.lower().replace(' ', '')}.com",
                "industry": "SaaS",
                "description": (
                    f"{company} is a rapidly growing SaaS company "
                    "focused on enterprise AI solutions."
                ),
                "headquarters": "San Francisco, California, USA",
                "employee_count": 450,
                "revenue_range": "$50M - $100M",
                "funding_stage": "Series B",
                "total_funding": "$85M",
                "founded_year": 2019,
                "technology_stack": [
                    "AWS",
                    "Docker",
                    "Kubernetes",
                    "Python",
                    "React"
                ],
                "linkedin": f"https://linkedin.com/company/{company.lower().replace(' ', '-')}",
                "status": "ACTIVE"
            }
        }
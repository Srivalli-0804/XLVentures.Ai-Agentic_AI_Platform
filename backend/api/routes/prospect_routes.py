from fastapi import APIRouter, HTTPException

from backend.memory.short_term.session_memory import session_memory

router = APIRouter(
    prefix="/prospects",
    tags=["Prospects"],
)


@router.get("/{workflow_id}")
def get_prospects(workflow_id: str):
    """
    Return all pipeline stages for the dashboard.
    """

    workflow = session_memory.load(workflow_id)

    if workflow is None:
        raise HTTPException(
            status_code=404,
            detail="Workflow not found",
        )

    context = workflow.get("context", {})

    prospects = []

    # ----------------------------------
    # Discovered
    # ----------------------------------

    for company in context.get("discovered_companies", []):

        prospects.append(
            {
                "id": company.get("company_id"),
                "company": company.get("name"),
                "stage": "Discovered",
                "score": company.get("score", 0),
            }
        )

    # ----------------------------------
    # Qualified
    # ----------------------------------

    for company in context.get("qualified_companies", []):

        prospects.append(
            {
                "id": company.get("company_id"),
                "company": company.get("name"),
                "stage": "Qualified",
                "score": company.get(
                    "prospect_score",
                    company.get("score", 0),
                ),
            }
        )

    # ----------------------------------
    # Enriched
    # ----------------------------------

    for company in context.get("company_profiles", []):

        prospects.append(
            {
                "id": company.get("company_id"),
                "company": company.get("company_name"),
                "stage": "Enriched",
                "score": company.get(
                    "prospect_score",
                    0,
                ),
            }
        )

    # ----------------------------------
    # Recommended
    # ----------------------------------

    seen = set()

    for recommendation in context.get("recommendations", []):

        company_id = recommendation.get("company_id")

        if company_id in seen:
            continue

        seen.add(company_id)

        prospects.append(
            {
                "id": company_id,
                "company": recommendation.get("company_name"),
                "stage": "Recommended",
                "score": recommendation.get(
                    "prospect_score",
                    0,
                ),
            }
        )

    return prospects

@router.get("/{workflow_id}/{company_id}")
def get_company_details(
    workflow_id: str,
    company_id: str,
):
    """
    Return full details for a single company.
    """

    workflow = session_memory.load(workflow_id)

    if workflow is None:
        raise HTTPException(
            status_code=404,
            detail="Workflow not found",
        )

    context = workflow.get("context", {})

    # Search qualified companies first
    companies = context.get("qualified_companies", [])

    if not companies:
        companies = context.get("discovered_companies", [])

    for company in companies:

        if company.get("company_id") == company_id:

            return {
                "company_id": company.get("company_id"),
                "name": company.get("name"),
                "industry": company.get("industry"),
                "location": company.get("location"),
                "status": company.get(
                    "qualification_status",
                    company.get("status"),
                ),
                "prospect_score": company.get(
                    "prospect_score",
                    company.get("score", 0),
                ),
                "market_signal": company.get("market_signal"),
            }

    raise HTTPException(
        status_code=404,
        detail="Company not found",
    )
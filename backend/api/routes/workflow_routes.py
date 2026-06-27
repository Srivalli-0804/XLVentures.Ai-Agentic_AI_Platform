"""
Workflow API Routes
"""

from fastapi import APIRouter, HTTPException

from backend.services.workflow_service import WorkflowService

router = APIRouter(
    prefix="/workflows",
    tags=["Workflows"],
)

service = WorkflowService()


@router.post("/create")
def create_workflow(workflow_name: str):
    """
    Create a new workflow.
    """
    workflow = service.create_workflow(workflow_name)

    return {
        "workflow_id": workflow.workflow_id,
        "workflow_name": workflow.workflow_name,
        "status": workflow.status,
    }


@router.post("/{workflow_id}/start")
def start_workflow(workflow_id: str):
    """
    Start an existing workflow.
    """

    data = service.get_workflow(workflow_id)

    if data is None:
        raise HTTPException(
            status_code=404,
            detail="Workflow not found",
        )

    workflow = service.load_workflow(workflow_id)

    workflow = service.start_workflow(workflow)

    return {
        "workflow_id": workflow.workflow_id,
        "status": workflow.status,
    }


@router.post("/{workflow_id}/complete")
def complete_workflow(workflow_id: str):

    workflow = service.load_workflow(workflow_id)

    if workflow is None:
        raise HTTPException(
            status_code=404,
            detail="Workflow not found",
        )

    workflow = service.complete_workflow(workflow)

    return {
        "workflow_id": workflow.workflow_id,
        "status": workflow.status,
    }


@router.get("/{workflow_id}")
def get_workflow(workflow_id: str):

    workflow = service.get_workflow(workflow_id)

    if workflow is None:
        raise HTTPException(
            status_code=404,
            detail="Workflow not found",
        )

    return workflow
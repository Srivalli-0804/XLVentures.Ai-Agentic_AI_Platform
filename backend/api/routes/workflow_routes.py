"""
Workflow API Routes
"""

from fastapi import APIRouter, HTTPException

from backend.services.workflow_service import WorkflowService
from backend.api.schemas.workflow_schema import CreateWorkflowRequest

router = APIRouter(
    prefix="/workflows",
    tags=["Workflows"],
)

service = WorkflowService()


@router.post("/create")
def create_workflow(request: CreateWorkflowRequest):
    """Create a new workflow."""

    workflow = service.create_workflow(request.workflow_name)


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


@router.post("/{workflow_id}/run")
async def run_workflow(workflow_id: str):
    """
    Execute the complete workflow.
    """

    workflow = service.load_workflow(workflow_id)

    if workflow is None:
        raise HTTPException(
            status_code=404,
            detail="Workflow not found",
        )

    context = await service.run_workflow(workflow)

    return {
        "workflow_id": workflow.workflow_id,
        "status": workflow.status,
        "execution_history": context.execution_history,
        "recommendations": context.recommendations,
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

@router.get("/{workflow_id}/timeline")
def workflow_timeline(workflow_id: str):

    workflow = service.get_workflow(workflow_id)

    if workflow is None:
        raise HTTPException(
            status_code=404,
            detail="Workflow not found",
        )

    context = workflow.get("context", {})

    history = context.get("execution_history", [])

    return [
        {
            "step": item["details"],
            "status": item["status"],
        }
        for item in history
    ]


@router.get("/{workflow_id}/trace")
def workflow_trace(workflow_id: str):

    workflow = service.get_workflow(workflow_id)

    if workflow is None:
        raise HTTPException(
            status_code=404,
            detail="Workflow not found",
        )

    context = workflow.get("context", {})

    return context.get("execution_history", [])
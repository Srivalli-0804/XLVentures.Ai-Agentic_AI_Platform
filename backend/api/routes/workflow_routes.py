"""
Workflow API Routes
"""

from fastapi import APIRouter, HTTPException

from backend.api.schemas.workflow_schema import CreateWorkflowRequest
from backend.services.workflow_service import WorkflowService

router = APIRouter(
    prefix="/workflows",
    tags=["Workflows"],
)

service = WorkflowService()


@router.get("")
def list_workflows():
    """Return available workflow summaries."""

    workflow = service.get_workflow("demo-workflow")

    if workflow is None:
        return []

    return [
        {
            "workflow_id": "demo-workflow",
            "workflow_name": workflow.get("workflow_name", "Demo Prospect Sweep"),
            "status": workflow.get("status", "COMPLETED"),
            "created_at": workflow.get("created_at", "2026-06-29T00:00:00"),
        }
    ]


@router.post("/create")
def create_workflow(request: CreateWorkflowRequest):
    """Create a new workflow."""

    workflow = service.create_workflow(request.workflow_name)

    return {
        "workflow_id": workflow.workflow_id,
        "workflow_name": workflow.workflow_name,
        "status": workflow.status,
    }


@router.post("/run")
async def run_workflow(request: CreateWorkflowRequest):
    """Create and immediately run a workflow."""

    workflow = service.create_workflow(request.workflow_name)
    workflow = service.start_workflow(workflow)
    context = await service.run_workflow(workflow)

    return {
        "workflow_id": workflow.workflow_id,
        "status": workflow.status,
        "execution_history": context.execution_history,
        "recommendations": context.recommendations,
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
async def run_existing_workflow(workflow_id: str):
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
            "id": f"step-{index}",
            "agent": item.get("agent", "PlannerAgent"),
            "status": item.get("status", "COMPLETED"),
            "details": item.get("details", item.get("action", "Completed")),
            "timestamp": item.get("timestamp", "2026-06-29T00:00:00"),
        }
        for index, item in enumerate(history)
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
    history = context.get("execution_history", [])

    return [
        {
            "id": f"trace-{index}",
            "agent_name": item.get("agent", "PlannerAgent"),
            "action": item.get("details", item.get("action", "Completed")),
            "result": item.get("status", "COMPLETED"),
            "timestamp": item.get("timestamp", "2026-06-29T00:00:00"),
        }
        for index, item in enumerate(history)
    ]
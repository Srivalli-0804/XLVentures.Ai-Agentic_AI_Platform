"""
Workflow Service

Coordinates workflow execution between the API layer and
the orchestration layer.
"""

from __future__ import annotations

import uuid

from backend.orchestration.workflow_state import WorkflowState
from backend.memory.short_term.session_memory import session_memory


class WorkflowService:
    """
    Service responsible for managing workflow lifecycle.
    """

    def create_workflow(
        self,
        workflow_name: str,
    ) -> WorkflowState:
        """
        Create a new workflow execution.
        """

        workflow = WorkflowState(
            workflow_id=str(uuid.uuid4()),
            workflow_name=workflow_name,
        )

        session_memory.save(
            workflow.workflow_id,
            {
                "workflow_name": workflow.workflow_name,
                "status": workflow.status,
            },
        )

        return workflow

    def start_workflow(
        self,
        workflow: WorkflowState,
    ) -> WorkflowState:
        """
        Mark workflow as running.
        """

        workflow.mark_running()

        session_memory.save(
            workflow.workflow_id,
            {
                "workflow_name": workflow.workflow_name,
                "status": workflow.status,
            },
        )

        return workflow

    def complete_workflow(
        self,
        workflow: WorkflowState,
    ) -> WorkflowState:
        """
        Mark workflow as completed.
        """

        workflow.mark_completed()

        session_memory.save(
            workflow.workflow_id,
            {
                "workflow_name": workflow.workflow_name,
                "status": workflow.status,
            },
        )

        return workflow

    def fail_workflow(
        self,
        workflow: WorkflowState,
        error: str,
    ) -> WorkflowState:
        """
        Mark workflow as failed.
        """

        workflow.mark_failed(error)

        session_memory.save(
            workflow.workflow_id,
            {
                "workflow_name": workflow.workflow_name,
                "status": workflow.status,
                "errors": workflow.errors,
            },
        )

        return workflow
    
    def get_workflow(
        self,
        workflow_id: str,
    ):
        """
        Retrieve workflow data from session memory.
        """
        return session_memory.load(workflow_id)

    def load_workflow(
        self,
        workflow_id: str,
    ) -> WorkflowState | None:
        """
        Recreate WorkflowState from session memory.
        """

        data = session_memory.load(workflow_id)

        if data is None:
            return None

        workflow = WorkflowState(
            workflow_id=workflow_id,
            workflow_name=data["workflow_name"],
        )

        workflow.status = data["status"]

        return workflow
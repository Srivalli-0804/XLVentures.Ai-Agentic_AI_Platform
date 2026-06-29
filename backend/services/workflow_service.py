"""
Workflow Service

Coordinates workflow execution between the API layer and
the orchestration layer.
"""

from __future__ import annotations

import uuid

from backend.agents.base.agent_context import AgentContext

from backend.core.config_loader import config_loader
from backend.memory.short_term.session_memory import session_memory
from backend.orchestration.workflow_state import WorkflowState

from backend.runtime.runtime import planner


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

    # ---------------------------------------------------------
    # Agent Context Helper
    # ---------------------------------------------------------

    def _create_context(
        self,
        workflow: WorkflowState,
        user_query: str = "Discover B2B prospects",
    ) -> AgentContext:
        """
        Create and populate an AgentContext for planner execution.
        """

        context = AgentContext(
            workflow_id=workflow.workflow_id,
            workflow_name=workflow.workflow_name,
            user_query=user_query,
        )

        context.icp = config_loader.get_icp()
        context.triggers = config_loader.get_triggers()

        context.metadata["providers"] = (
            config_loader.get_providers()
        )

        context.metadata["workflow"] = (
            config_loader.get_workflow()
        )

        return context

    # ---------------------------------------------------------
    # Execute Workflow
    # ---------------------------------------------------------

    async def run_workflow(
        self,
        workflow: WorkflowState,
        user_query: str = "Discover B2B prospects",
    ) -> AgentContext:
        """
        Execute the workflow using the Planner.
        """

        workflow.mark_running()

        context = self._create_context(
            workflow,
            user_query=user_query,
        )

        context = await planner.execute(context)
        

        session_memory.save(
            workflow.workflow_id,
            {
                "workflow_name": workflow.workflow_name,
                "status": workflow.status,
                "context": context.model_dump(),
            },
        )

        return context

    # ---------------------------------------------------------
    # Lifecycle Methods
    # ---------------------------------------------------------

    def start_workflow(
        self,
        workflow: WorkflowState,
    ) -> WorkflowState:
        """
        Mark workflow as running.
        """

        workflow.mark_running()

        existing = session_memory.load(workflow.workflow_id) or {}

        existing["workflow_name"] = workflow.workflow_name
        existing["status"] = workflow.status

        session_memory.save(
            workflow.workflow_id,
            existing,
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

        existing = session_memory.load(workflow.workflow_id) or {}

        existing["workflow_name"] = workflow.workflow_name
        existing["status"] = workflow.status

        session_memory.save(
            workflow.workflow_id,
            existing,
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

    # ---------------------------------------------------------
    # Retrieval
    # ---------------------------------------------------------

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
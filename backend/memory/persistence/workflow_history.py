"""
Workflow History Service

Persists and retrieves workflow execution history.
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from backend.models.workflow import Workflow
from backend.memory.persistence.repositories import WorkflowRepository


class WorkflowHistory:

    def __init__(self, db: Session):
        self.repository = WorkflowRepository(db)

    def save(self, workflow: Workflow) -> Workflow:
        """
        Save a workflow execution.
        """
        return self.repository.add(workflow)

    def get(self, workflow_id: int) -> Workflow | None:
        """
        Retrieve a workflow execution.
        """
        return self.repository.get_by_id(workflow_id)

    def list(self) -> list[Workflow]:
        """
        Retrieve all workflow executions.
        """
        return self.repository.get_all()
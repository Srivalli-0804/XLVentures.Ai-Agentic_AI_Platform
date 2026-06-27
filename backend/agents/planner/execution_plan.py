from __future__ import annotations

from datetime import datetime
from typing import Dict, List

from pydantic import BaseModel, Field

from .workflow_models import WorkflowNode


class ExecutionPlan(BaseModel):
    """
    Represents a workflow execution plan generated
    by the Planner.

    The Planner creates an ExecutionPlan, and the
    ExecutionEngine executes it.
    """

    workflow_name: str

    workflow_version: str = "1.0.0"

    created_at: datetime = Field(default_factory=datetime.utcnow)

    steps: List[WorkflowNode]

    status: str = "PENDING"

    metadata: Dict[str, str] = Field(default_factory=dict)

    def total_steps(self) -> int:
        """
        Returns the total number of workflow steps.
        """
        return len(self.steps)

    def capabilities(self) -> List[str]:
        """
        Returns the ordered list of capabilities.
        """
        return [
            node.capability
            for node in self.steps
        ]
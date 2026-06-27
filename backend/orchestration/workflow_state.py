"""
Runtime Workflow State

This object represents the current execution state of a workflow.
It is passed between the planner, execution engine, agents,
memory, and orchestration components.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class WorkflowState:
    """
    Runtime state for a workflow execution.
    """

    workflow_id: str
    workflow_name: str

    status: str = "PENDING"

    current_step: str | None = None

    execution_plan: list[str] = field(default_factory=list)

    planner_output: dict[str, Any] = field(default_factory=dict)

    shared_memory: dict[str, Any] = field(default_factory=dict)

    results: dict[str, Any] = field(default_factory=dict)

    errors: list[str] = field(default_factory=list)

    started_at: datetime = field(default_factory=datetime.utcnow)

    completed_at: datetime | None = None

    metadata: dict[str, Any] = field(default_factory=dict)

    def mark_running(self) -> None:
        self.status = "RUNNING"

    def mark_completed(self) -> None:
        self.status = "COMPLETED"
        self.completed_at = datetime.utcnow()

    def mark_failed(self, error: str) -> None:
        self.status = "FAILED"
        self.errors.append(error)
        self.completed_at = datetime.utcnow()

    def add_result(self, key: str, value: Any) -> None:
        self.results[key] = value

    def update_metadata(self, key: str, value: Any) -> None:
        self.metadata[key] = value
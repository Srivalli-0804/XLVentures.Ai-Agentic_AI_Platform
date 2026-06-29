from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional
from uuid import uuid4

from pydantic import BaseModel ,ConfigDict,Field


class AgentContext(BaseModel):
    """
    Shared context passed between all agents.

    Every agent reads from this object,
    updates it,
    and returns the same object.

    This acts as the shared memory for the workflow.
    """

    # -------------------------------------------------
    # Workflow Information
    # -------------------------------------------------

    workflow_id: str = Field(default_factory=lambda: str(uuid4()))
    task_id: str = Field(default_factory=lambda: str(uuid4()))

    workflow_name: Optional[str] = None
    current_step: Optional[str] = None

    created_at: datetime = Field(default_factory=datetime.utcnow)

    # -------------------------------------------------
    # User Input
    # -------------------------------------------------

    user_query: Optional[str] = None

    business_domain: Optional[str] = None

    target_personas: List[str] = Field(default_factory=list)

    icp: Dict[str, Any] = Field(default_factory=dict)

    triggers: List[str] = Field(default_factory=list)

    # -------------------------------------------------
    # Discovery Results
    # -------------------------------------------------

    discovered_companies: List[Dict[str, Any]] = Field(default_factory=list)

    market_signals: List[Dict[str, Any]] = Field(default_factory=list)

    # -------------------------------------------------
    # Qualification
    # -------------------------------------------------

    qualified_companies: List[Dict[str, Any]] = Field(default_factory=list)

    rejected_companies: List[Dict[str, Any]] = Field(default_factory=list)

    # -------------------------------------------------
    # Enrichment
    # -------------------------------------------------

    company_profiles: List[Dict[str, Any]] = Field(default_factory=list)

    contacts: List[Dict[str, Any]] = Field(default_factory=list)

    # -------------------------------------------------
    # Recommendations
    # -------------------------------------------------

    recommendations: List[Dict[str, Any]] = Field(default_factory=list)

    # -------------------------------------------------
    # Human Approval
    # -------------------------------------------------

    approvals: List[Dict[str, Any]] = Field(default_factory=list)

    # -------------------------------------------------
    # Shared Memory
    # -------------------------------------------------

    shared_memory: Dict[str, Any] = Field(default_factory=dict)

    metadata: Dict[str, Any] = Field(default_factory=dict)

    execution_history: List[Dict[str, Any]] = Field(default_factory=list)

    # -------------------------------------------------
    # Utility Methods
    # -------------------------------------------------

    def add_execution_step(
        self,
        agent_name: str,
        status: str,
        details: Optional[str] = None,
    ) -> None:
        """
        Records agent execution history.
        """

        self.execution_history.append(
            {
                "agent": agent_name,
                "status": status,
                "details": details,
                "timestamp": datetime.utcnow(),
            }
        )

    def set_memory(self, key: str, value: Any) -> None:
        """
        Store a value in shared memory.
        """

        self.shared_memory[key] = value

    def get_memory(self, key: str, default: Any = None) -> Any:
        """
        Retrieve a value from shared memory.
        """

        return self.shared_memory.get(key, default)

    model_config = ConfigDict(
        arbitrary_types_allowed=True
    )
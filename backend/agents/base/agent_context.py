"""
Agent Context

Shared execution context passed between agents.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class AgentContext:
    """
    Shared context for workflow execution.

    Agents exchange data only through this object.
    """

    workflow_id: str

    workflow_name: str

    metadata: dict[str, Any] = field(default_factory=dict)

    discovered_companies: list[Any] = field(default_factory=list)

    qualified_companies: list[Any] = field(default_factory=list)

    scored_companies: list[Any] = field(default_factory=list)

    enriched_companies: list[Any] = field(default_factory=list)

    contacts: list[Any] = field(default_factory=list)

    enriched_contacts: list[Any] = field(default_factory=list)

    validated_contacts: list[Any] = field(default_factory=list)

    recommendations: list[Any] = field(default_factory=list)

    approvals: list[Any] = field(default_factory=list)

    errors: list[str] = field(default_factory=list)

    def add_error(self, message: str) -> None:
        """
        Store workflow errors.
        """
        self.errors.append(message)

    def set_metadata(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Store metadata.
        """
        self.metadata[key] = value

    def get_metadata(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        """
        Retrieve metadata.
        """
        return self.metadata.get(key, default)
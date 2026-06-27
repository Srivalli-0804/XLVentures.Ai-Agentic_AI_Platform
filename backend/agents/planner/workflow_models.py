from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class WorkflowNode(BaseModel):
    """
    Represents a single capability in a workflow.

    A node does NOT know about agents.
    It only represents a business capability.

    Example:
        company_discovery
        qualification
        enrichment
    """

    id: str

    capability: str

    description: str

    dependencies: List[str] = Field(default_factory=list)

    next_nodes: List[str] = Field(default_factory=list)

    metadata: Dict[str, str] = Field(default_factory=dict)


class WorkflowDefinition(BaseModel):
    """
    Represents a complete workflow.

    Example

    Prospect Discovery

        company_discovery
                ↓
        qualification
                ↓
        enrichment
                ↓
        recommendation
                ↓
        approval
    """

    name: str

    description: str

    start_node: str

    nodes: Dict[str, WorkflowNode]

    version: str = "1.0.0"

    metadata: Dict[str, str] = Field(default_factory=dict)

    def get_node(self, node_id: str) -> Optional[WorkflowNode]:
        """
        Returns a workflow node by its ID.
        """

        return self.nodes.get(node_id)

    def has_node(self, node_id: str) -> bool:
        """
        Checks whether the workflow contains a node.
        """

        return node_id in self.nodes

    def list_capabilities(self) -> List[str]:
        """
        Returns all capabilities in this workflow.
        """

        return [
            node.capability
            for node in self.nodes.values()
        ]
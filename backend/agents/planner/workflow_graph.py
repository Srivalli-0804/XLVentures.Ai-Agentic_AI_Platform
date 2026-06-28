"""
Workflow Graph

Defines workflow execution as a directed graph.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class WorkflowNode:
    """
    Represents one execution step.
    """

    id: str
    capability: str
    description: str

    dependencies: list[str] = field(default_factory=list)

    next_nodes: list[str] = field(default_factory=list)


class WorkflowGraph:
    """
    Stores workflow definition.
    """

    def __init__(self):

        self.nodes: dict[str, WorkflowNode] = {}

    def add_node(
        self,
        node: WorkflowNode,
    ):

        self.nodes[node.id] = node

    def get_node(
        self,
        node_id: str,
    ) -> WorkflowNode:

        return self.nodes[node_id]

    def get_roots(
        self,
    ) -> list[WorkflowNode]:

        return [
            node
            for node in self.nodes.values()
            if not node.dependencies
        ]

    def __iter__(self):
        return iter(self.nodes.values())
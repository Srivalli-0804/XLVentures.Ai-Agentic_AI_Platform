"""
Planner Agent

Builds workflow graphs and generates execution plans.
"""

from __future__ import annotations

from backend.agents.planner.execution_engine import ExecutionEngine
from backend.agents.planner.workflow_graph import (
    WorkflowGraph,
    WorkflowNode,
)


class PlannerAgent:
    """
    Responsible for generating execution plans.
    """

    def __init__(self) -> None:
        self.engine = ExecutionEngine()

    def build_company_discovery_workflow(self) -> WorkflowGraph:
        """
        Build the Company Discovery workflow graph.
        """

        graph = WorkflowGraph()

        graph.add_node(
            WorkflowNode(
                id="trigger",
                capability="trigger_monitor",
                description="Monitor trigger events",
                next_nodes=["discovery"],
            )
        )

        graph.add_node(
            WorkflowNode(
                id="discovery",
                capability="company_discovery",
                description="Discover companies",
                dependencies=["trigger"],
                next_nodes=["qualification"],
            )
        )

        graph.add_node(
            WorkflowNode(
                id="qualification",
                capability="qualification",
                description="Qualify discovered companies",
                dependencies=["discovery"],
                next_nodes=["scoring"],
            )
        )

        graph.add_node(
            WorkflowNode(
                id="scoring",
                capability="company_scoring",
                description="Score qualified companies",
                dependencies=["qualification"],
                next_nodes=["enrichment"],
            )
        )

        graph.add_node(
            WorkflowNode(
                id="enrichment",
                capability="company_enrichment",
                description="Enrich company data",
                dependencies=["scoring"],
                next_nodes=["contacts"],
            )
        )

        graph.add_node(
            WorkflowNode(
                id="contacts",
                capability="contact_discovery",
                description="Discover contacts",
                dependencies=["enrichment"],
                next_nodes=["recommendation"],
            )
        )

        graph.add_node(
            WorkflowNode(
                id="recommendation",
                capability="recommendation",
                description="Generate outreach recommendations",
                dependencies=["contacts"],
                next_nodes=["approval"],
            )
        )

        graph.add_node(
            WorkflowNode(
                id="approval",
                capability="approval",
                description="Human approval",
                dependencies=["recommendation"],
            )
        )

        return graph

    def create_execution_plan(self):
        """
        Generate execution plan.
        """

        graph = self.build_company_discovery_workflow()

        return self.engine.build_execution_plan(graph)
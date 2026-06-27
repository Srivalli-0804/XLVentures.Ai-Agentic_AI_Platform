"""
LangGraph Builder

Responsible only for converting a workflow definition into a
LangGraph StateGraph.

No business logic belongs here.
"""

from __future__ import annotations

from typing import Callable

try:
    from langgraph.graph import StateGraph
except ImportError:
    StateGraph = None


class LangGraphBuilder:
    """
    Builds executable LangGraph workflows.
    """

    def __init__(self) -> None:
        if StateGraph is None:
            raise ImportError(
                "LangGraph is not installed. "
                "Run: pip install langgraph"
            )

    def build(
        self,
        state_type: type,
    ) -> StateGraph:
        """
        Create an empty StateGraph.

        Nodes and edges will be added by the planner.
        """
        return StateGraph(state_type)

    @staticmethod
    def add_node(
        graph: StateGraph,
        node_name: str,
        node: Callable,
    ) -> None:
        """
        Register a node.
        """
        graph.add_node(node_name, node)

    @staticmethod
    def add_edge(
        graph: StateGraph,
        source: str,
        target: str,
    ) -> None:
        """
        Register an edge.
        """
        graph.add_edge(source, target)

    @staticmethod
    def compile(graph: StateGraph):
        """
        Compile the graph.
        """
        return graph.compile()
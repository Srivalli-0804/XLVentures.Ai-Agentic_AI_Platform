"""
Execution Engine

Generates an execution plan from a workflow graph.
"""

from __future__ import annotations

from collections import deque

from backend.agents.planner.workflow_graph import (
    WorkflowGraph,
    WorkflowNode,
)

from backend.agents.base.agent_context import AgentContext
from backend.agents.base.capability_router import capability_router

class ExecutionEngine:
    """
    Generates execution order from a workflow graph.
    """

    def build_execution_plan(
        self,
        graph: WorkflowGraph,
    ) -> list[WorkflowNode]:
        """
        Returns workflow nodes in dependency order.
        """

        indegree: dict[str, int] = {}
        queue: deque[str] = deque()
        execution_plan: list[WorkflowNode] = []

        # Calculate indegree
        for node in graph:
            indegree[node.id] = len(node.dependencies)

        # Add root nodes
        for node in graph.get_roots():
            queue.append(node.id)

        # Topological Sort (Kahn's Algorithm)
        while queue:

            node_id = queue.popleft()

            node = graph.get_node(node_id)

            execution_plan.append(node)

            for next_node_id in node.next_nodes:

                if next_node_id not in indegree:
                    continue

                indegree[next_node_id] -= 1

                if indegree[next_node_id] == 0:
                    queue.append(next_node_id)

        # Detect cycles
        if len(execution_plan) != len(graph.nodes):
            raise ValueError(
                "Workflow graph contains a cycle."
            )

        return execution_plan
    def execute(
        self,
        graph: WorkflowGraph,
        context: AgentContext,
    ) -> AgentContext:
        """
        Execute a workflow graph.

        For each workflow node:
        1. Resolve the capability to an agent.
        2. Execute the agent.
        3. Pass the updated context to the next agent.
        """

        execution_plan = self.build_execution_plan(graph)

        for node in execution_plan:

            if not capability_router.can_resolve(node.capability):
                raise ValueError(
                    f"No agent registered for capability "
                    f"'{node.capability}'."
                )

            agent = capability_router.resolve(node.capability)

            context = agent.execute(context)

        return context
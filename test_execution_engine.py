from backend.agents.planner.execution_engine import ExecutionEngine
from backend.agents.planner.workflow_graph import (
    WorkflowGraph,
    WorkflowNode,
)

graph = WorkflowGraph()

graph.add_node(
    WorkflowNode(
        id="trigger",
        capability="trigger_monitor",
        description="Trigger Monitor",
        next_nodes=["discovery"],
    )
)

graph.add_node(
    WorkflowNode(
        id="discovery",
        capability="company_discovery",
        description="Company Discovery",
        dependencies=["trigger"],
        next_nodes=["qualification"],
    )
)

graph.add_node(
    WorkflowNode(
        id="qualification",
        capability="qualification",
        description="ICP Qualification",
        dependencies=["discovery"],
    )
)

engine = ExecutionEngine()

plan = engine.build_execution_plan(graph)

for node in plan:
    print(node.id)
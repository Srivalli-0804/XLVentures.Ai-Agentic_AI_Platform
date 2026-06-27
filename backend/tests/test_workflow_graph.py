from agents.planner.workflow_graph import WorkflowGraph
from agents.planner.workflow_models import (
    WorkflowDefinition,
    WorkflowNode,
)


def main():

    workflow_graph = WorkflowGraph()

    workflow = WorkflowDefinition(
        name="Prospect Discovery Workflow",
        description="End-to-end prospect discovery workflow.",
        start_node="trigger",

        nodes={
            "trigger": WorkflowNode(
                id="trigger",
                capability="trigger_monitor",
                description="Monitor business triggers.",
                next_nodes=["discovery"],
            ),

            "discovery": WorkflowNode(
                id="discovery",
                capability="company_discovery",
                description="Discover matching companies.",
                dependencies=["trigger"],
                next_nodes=["market"],
            ),

            "market": WorkflowNode(
                id="market",
                capability="market_signal_analysis",
                description="Analyze market signals.",
                dependencies=["discovery"],
            ),
        },
    )

    print("=" * 60)
    print("Registering Workflow")
    print("=" * 60)

    workflow_graph.register_workflow(workflow)

    print("Workflow Registered Successfully\n")

    retrieved = workflow_graph.get_workflow(
        "Prospect Discovery Workflow"
    )

    print("=" * 60)
    print("Workflow Information")
    print("=" * 60)

    print("Name :", retrieved.name)
    print("Start Node :", retrieved.start_node)

    print("\nCapabilities:")

    for capability in retrieved.list_capabilities():
        print("-", capability)

    print()

    print("=" * 60)
    print("Workflow Graph Test Passed")
    print("=" * 60)


if __name__ == "__main__":
    main()
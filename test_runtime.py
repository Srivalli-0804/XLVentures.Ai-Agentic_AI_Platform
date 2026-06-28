from backend.agents.base.agent_context import AgentContext
from backend.agents.base.base_agent import BaseAgent
from backend.agents.base.agent_registry import agent_registry
from backend.agents.planner.execution_engine import ExecutionEngine


class TriggerAgent(BaseAgent):

    capability = "trigger_monitor"

    def validate(self, context):
        pass

    def _run(self, context):
        print("Trigger Agent")
        context.set_metadata(
            "trigger_events",
            ["Funding Round"],
        )
        return context


class DiscoveryAgent(BaseAgent):

    capability = "company_discovery"

    def validate(self, context):
        pass

    def _run(self, context):
        print("Discovery Agent")
        context.discovered_companies.append(
            "OpenAI"
        )
        return context


class QualificationAgent(BaseAgent):

    capability = "qualification"

    def validate(self, context):
        pass

    def _run(self, context):
        print("Qualification Agent")
        context.qualified_companies.append(
            "OpenAI"
        )
        return context


# Register only the first three capabilities
agent_registry.clear()

agent_registry.register(
    "trigger_monitor",
    TriggerAgent(),
)

agent_registry.register(
    "company_discovery",
    DiscoveryAgent(),
)

agent_registry.register(
    "qualification",
    QualificationAgent(),
)

from backend.agents.planner.workflow_graph import WorkflowGraph, WorkflowNode

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
        description="Qualification",
        dependencies=["discovery"],
    )
)

context = AgentContext(
    workflow_id="wf-001",
    workflow_name="Company Discovery",
)

engine = ExecutionEngine()

context = engine.execute(
    graph,
    context,
)

print(context.get_metadata("trigger_events"))
print(context.discovered_companies)
print(context.qualified_companies)
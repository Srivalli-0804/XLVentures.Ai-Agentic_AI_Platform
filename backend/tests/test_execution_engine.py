import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
import asyncio

from agents.base.agent_context import AgentContext
from agents.base.agent_registry import AgentRegistry
from agents.base.capability_router import CapabilityRouter

from agents.discovery.trigger_monitor_agent import TriggerMonitorAgent
from agents.discovery.company_discovery_agent import CompanyDiscoveryAgent
from agents.discovery.market_signal_agent import MarketSignalAgent

from agents.planner.execution_engine import ExecutionEngine
from agents.planner.execution_plan import ExecutionPlan
from agents.planner.workflow_models import WorkflowNode



async def main():

    registry = AgentRegistry()

    registry.register(TriggerMonitorAgent())
    registry.register(CompanyDiscoveryAgent())
    registry.register(MarketSignalAgent())

    router = CapabilityRouter(registry)

    engine = ExecutionEngine(router)

    plan = ExecutionPlan(
        workflow_name="Test Workflow",
        steps=[
            WorkflowNode(
                id="1",
                capability="trigger_monitor",
                description="Trigger Monitor",
            ),
            WorkflowNode(
                id="2",
                capability="company_discovery",
                description="Company Discovery",
            ),
            WorkflowNode(
                id="3",
                capability="market_signal_analysis",
                description="Market Signals",
            ),
        ],
    )

    context = AgentContext()
    context.triggers = [
    "Funding Round",
    "Hiring Spike",
    "Product Launch",
]
    context.icp = {
    "industry": "SaaS",
    "location": "United States",
}

    context = await engine.execute_plan(
        plan,
        context,
    )

    print("=" * 60)
    print("Execution Engine Test Passed")
    print("=" * 60)

    print()

    print("Execution History")

    for step in context.execution_history:
        print(step)


if __name__ == "__main__":
    asyncio.run(main())
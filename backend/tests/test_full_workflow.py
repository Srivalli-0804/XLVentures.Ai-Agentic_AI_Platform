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

from agents.qualification.icp_qualifier_agent import ICPQualifierAgent
from agents.qualification.company_scoring_agent import CompanyScoringAgent
from agents.qualification.evaluator_agent import EvaluatorAgent

from agents.enrichment.company_enrichment_agent import CompanyEnrichmentAgent
from agents.enrichment.contact_discovery_agent import ContactDiscoveryAgent
from agents.enrichment.linkedin_enrichment_agent import LinkedInEnrichmentAgent
from agents.enrichment.contact_validation_agent import ContactValidationAgent

from agents.recommendation.outreach_recommender_agent import (
    OutreachRecommenderAgent,
)
from agents.recommendation.personalization_agent import (
    PersonalizationAgent,
)
from agents.recommendation.next_action_agent import NextActionAgent

from agents.hitl.approval_agent import ApprovalAgent



async def main():

    registry = AgentRegistry()

    registry.register(TriggerMonitorAgent())
    registry.register(CompanyDiscoveryAgent())
    registry.register(MarketSignalAgent())
    registry.register(ICPQualifierAgent())
    registry.register(CompanyScoringAgent())
    registry.register(EvaluatorAgent())

    registry.register(CompanyEnrichmentAgent())
    registry.register(ContactDiscoveryAgent())
    registry.register(LinkedInEnrichmentAgent())
    registry.register(ContactValidationAgent())

    registry.register(OutreachRecommenderAgent())
    registry.register(PersonalizationAgent())
    registry.register(NextActionAgent())

    registry.register(ApprovalAgent())

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
    WorkflowNode(
        id="4",
        capability="qualification",
        description="ICP Qualification",
    ),
    WorkflowNode(
        id="5",
        capability="company_scoring",
        description="Company Scoring",
    ),
    WorkflowNode(
        id="6",
        capability="company_enrichment",
        description="Company Enrichment",
    ),
    WorkflowNode(
        id="7",
        capability="contact_discovery",
        description="Contact Discovery",
    ),
    WorkflowNode(
        id="8",
        capability="linkedin_enrichment",
        description="LinkedIn Enrichment",
    ),
    WorkflowNode(
        id="9",
        capability="contact_validation",
        description="Contact Validation",
    ),
    WorkflowNode(
        id="10",
        capability="outreach_recommendation",
        description="Outreach Recommendation",
    ),
    WorkflowNode(
        id="11",
        capability="personalization",
        description="Personalization",
    ),
    WorkflowNode(
        id="12",
        capability="next_action",
        description="Next Action",
    ),
    WorkflowNode(
        id="13",
        capability="approval",
        description="Approval",
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
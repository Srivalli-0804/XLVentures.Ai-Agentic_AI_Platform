from __future__ import annotations

from backend.agents.base.agent_registry import AgentRegistry
from backend.agents.base.capability_router import CapabilityRouter

from backend.agents.discovery.trigger_monitor_agent import TriggerMonitorAgent
from backend.agents.discovery.company_discovery_agent import CompanyDiscoveryAgent
from backend.agents.discovery.market_signal_agent import MarketSignalAgent

from backend.agents.qualification.icp_qualifier_agent import ICPQualifierAgent
from backend.agents.qualification.company_scoring_agent import CompanyScoringAgent
from backend.agents.qualification.evaluator_agent import EvaluatorAgent

from backend.agents.enrichment.company_enrichment_agent import CompanyEnrichmentAgent
from backend.agents.enrichment.contact_discovery_agent import ContactDiscoveryAgent
from backend.agents.enrichment.linkedin_enrichment_agent import LinkedInEnrichmentAgent
from backend.agents.enrichment.contact_validation_agent import ContactValidationAgent

from backend.agents.recommendation.outreach_recommender_agent import (
    OutreachRecommenderAgent,
)
from backend.agents.recommendation.personalization_agent import (
    PersonalizationAgent,
)
from backend.agents.recommendation.next_action_agent import NextActionAgent

from backend.agents.hitl.approval_agent import ApprovalAgent

from backend.agents.planner.execution_engine import ExecutionEngine
from backend.agents.planner.planner_agent import PlannerAgent
from backend.agents.planner.planning_strategy import RuleBasedPlanningStrategy
from backend.agents.planner.workflow_graph import WorkflowGraph

from .workflows import create_prospect_workflow


def create_execution_engine():

    registry = AgentRegistry()

    # -----------------------------
    # Discovery
    # -----------------------------

    registry.register(TriggerMonitorAgent())
    registry.register(CompanyDiscoveryAgent())
    registry.register(MarketSignalAgent())

    # -----------------------------
    # Qualification
    # -----------------------------

    registry.register(ICPQualifierAgent())
    registry.register(CompanyScoringAgent())
    registry.register(EvaluatorAgent())

    # -----------------------------
    # Enrichment
    # -----------------------------

    registry.register(CompanyEnrichmentAgent())
    registry.register(ContactDiscoveryAgent())
    registry.register(LinkedInEnrichmentAgent())
    registry.register(ContactValidationAgent())

    # -----------------------------
    # Recommendation
    # -----------------------------

    registry.register(OutreachRecommenderAgent())
    registry.register(PersonalizationAgent())
    registry.register(NextActionAgent())

    # -----------------------------
    # HITL
    # -----------------------------

    registry.register(ApprovalAgent())

    router = CapabilityRouter(registry)

    return ExecutionEngine(router)


# Existing execution engine singleton (do not remove)
execution_engine = create_execution_engine()

# -----------------------------
# WorkflowGraph singleton
# -----------------------------

workflow_graph = WorkflowGraph()
workflow_graph.register_workflow(create_prospect_workflow())

# -----------------------------
# Planner singleton
# -----------------------------

_planning_strategy = RuleBasedPlanningStrategy()
planner = PlannerAgent(
    planning_strategy=_planning_strategy,
    workflow_graph=workflow_graph,
    execution_engine=execution_engine,
)

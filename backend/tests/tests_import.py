print("=" * 60)
print("Testing Base Layer")
print("=" * 60)

from agents.base.base_agent import BaseAgent
from agents.base.agent_context import AgentContext
from agents.base.agent_registry import AgentRegistry
from agents.base.capability_router import CapabilityRouter

print("✓ Base Layer Imported")


print("=" * 60)
print("Testing Planner Layer")
print("=" * 60)

from agents.planner.workflow_models import WorkflowNode, WorkflowDefinition
from agents.planner.workflow_graph import WorkflowGraph
from agents.planner.execution_plan import ExecutionPlan
from agents.planner.execution_engine import ExecutionEngine
from agents.planner.planning_strategy import (
    PlanningStrategy,
    RuleBasedPlanningStrategy,
)
from agents.planner.planner_agent import PlannerAgent

print("✓ Planner Layer Imported")


print("=" * 60)
print("Testing Discovery Agents")
print("=" * 60)

from agents.discovery.trigger_monitor_agent import TriggerMonitorAgent
from agents.discovery.company_discovery_agent import CompanyDiscoveryAgent
from agents.discovery.market_signal_agent import MarketSignalAgent

print("✓ Discovery Agents Imported")


print("=" * 60)
print("Testing Qualification Agents")
print("=" * 60)

from agents.qualification.icp_qualifier_agent import ICPQualifierAgent
from agents.qualification.company_scoring_agent import CompanyScoringAgent
from agents.qualification.evaluator_agent import EvaluatorAgent

print("✓ Qualification Agents Imported")


print("=" * 60)
print("Testing Enrichment Agents")
print("=" * 60)

from agents.enrichment.company_enrichment_agent import CompanyEnrichmentAgent
from agents.enrichment.contact_discovery_agent import ContactDiscoveryAgent
from agents.enrichment.linkedin_enrichment_agent import LinkedInEnrichmentAgent
from agents.enrichment.contact_validation_agent import ContactValidationAgent

print("✓ Enrichment Agents Imported")


print("=" * 60)
print("Testing Recommendation Agents")
print("=" * 60)

from agents.recommendation.outreach_recommender_agent import OutreachRecommenderAgent
from agents.recommendation.personalization_agent import PersonalizationAgent
from agents.recommendation.next_action_agent import NextActionAgent

print("✓ Recommendation Agents Imported")


print("=" * 60)
print("Testing HITL")
print("=" * 60)

from agents.hitl.approval_agent import ApprovalAgent

print("✓ HITL Imported")


print("=" * 60)
print("Testing Tools")
print("=" * 60)

from tools.base.base_tool import BaseTool
from tools.base.tool_registry import ToolRegistry
from tools.web_scraper import WebScraper
from tools.html_parser import HTMLParser
from tools.llm_extractor import LLMExtractor
from tools.fallback_manager import FallbackManager

print("✓ Tools Imported")


print("=" * 60)
print("ALL IMPORTS SUCCESSFUL")
print("=" * 60)
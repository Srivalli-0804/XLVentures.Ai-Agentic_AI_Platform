"""
Registers all available business agents.
"""

from backend.agents.base.agent_registry import agent_registry

# Discovery
from backend.agents.discovery.trigger_monitor_agent import TriggerMonitorAgent
from backend.agents.discovery.company_discovery_agent import CompanyDiscoveryAgent

# Qualification
from backend.agents.qualification.icp_qualifier_agent import ICPQualifierAgent
from backend.agents.qualification.company_scoring_agent import CompanyScoringAgent

# Enrichment
from backend.agents.enrichment.company_enrichment_agent import CompanyEnrichmentAgent
from backend.agents.enrichment.contact_discovery_agent import ContactDiscoveryAgent
from backend.agents.enrichment.linkedin_enrichment_agent import LinkedInEnrichmentAgent
from backend.agents.enrichment.contact_validation_agent import ContactValidationAgent

# Recommendation
from backend.agents.recommendation.outreach_recommender_agent import (
    OutreachRecommenderAgent,
)
from backend.agents.hitl.approval_agent import ApprovalAgent


def register_all_agents() -> None:
    """
    Register every available business agent.
    """

    agent_registry.clear()

    agents = [
        TriggerMonitorAgent(),
        CompanyDiscoveryAgent(),
        ICPQualifierAgent(),
        CompanyScoringAgent(),
        CompanyEnrichmentAgent(),
        ContactDiscoveryAgent(),
        LinkedInEnrichmentAgent(),
        ContactValidationAgent(),
        OutreachRecommenderAgent(),
        ApprovalAgent(),
    ]

    for agent in agents:
        agent_registry.register(
            agent.capability,
            agent,
        )
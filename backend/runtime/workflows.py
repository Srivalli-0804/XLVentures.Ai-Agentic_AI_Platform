from __future__ import annotations

"""backend/runtime/workflows.py

Workflow definitions for ProspectIQ.

This module ONLY creates WorkflowDefinition instances using the existing
Workflow models (WorkflowDefinition / WorkflowNode). It does not register
or execute workflows.
"""

from typing import Dict, List

from backend.agents.planner.workflow_models import (
    WorkflowDefinition,
    WorkflowNode,
)


def _node(
    *,
    node_id: str,
    capability: str,
    description: str,
    dependencies: List[str] | None = None,
    next_nodes: List[str] | None = None,
) -> WorkflowNode:
    return WorkflowNode(
        id=node_id,
        capability=capability,
        description=description,
        dependencies=dependencies or [],
        next_nodes=next_nodes or [],
    )


def create_prospect_workflow() -> WorkflowDefinition:
    """Create the ProspectIQ end-to-end prospect intelligence workflow."""

    # Node ids are internal identifiers for graph traversal.
    # Node.capability values must match the CapabilityRouter keys
    # (i.e., agent capabilities).

    nodes: Dict[str, WorkflowNode] = {}

    # Discovery
    nodes["trigger_monitor"] = _node(
        node_id="trigger_monitor",
        capability="trigger_monitor",
        description="Monitor triggers and start prospect intelligence run.",
        next_nodes=["company_discovery"],
    )

    nodes["company_discovery"] = _node(
        node_id="company_discovery",
        capability="company_discovery",
        description="Discover target companies relevant to the ICP.",
        dependencies=["trigger_monitor"],
        next_nodes=["market_signal_analysis"],
    )

    nodes["market_signal_analysis"] = _node(
        node_id="market_signal_analysis",
        capability="market_signal_analysis",
        description="Analyze market signals for discovered companies.",
        dependencies=["company_discovery"],
        next_nodes=["qualification"],
    )

    # Qualification / Scoring
    nodes["qualification"] = _node(
        node_id="qualification",
        capability="qualification",
        description="Qualify companies against ICP and qualification criteria.",
        dependencies=["market_signal_analysis"],
        next_nodes=["company_scoring"],
    )

    nodes["company_scoring"] = _node(
        node_id="company_scoring",
        capability="company_scoring",
        description="Score qualified companies for prioritization.",
        dependencies=["qualification"],
        next_nodes=["company_enrichment"],
    )

    # Enrichment
    nodes["company_enrichment"] = _node(
        node_id="company_enrichment",
        capability="company_enrichment",
        description="Enrich company profiles with additional intelligence.",
        dependencies=["company_scoring"],
        next_nodes=["contact_discovery"],
    )

    nodes["contact_discovery"] = _node(
        node_id="contact_discovery",
        capability="contact_discovery",
        description="Discover relevant contacts for enriched companies.",
        dependencies=["company_enrichment"],
        next_nodes=["linkedin_enrichment"],
    )

    nodes["linkedin_enrichment"] = _node(
        node_id="linkedin_enrichment",
        capability="linkedin_enrichment",
        description="Enrich contacts using LinkedIn and related signals.",
        dependencies=["contact_discovery"],
        next_nodes=["contact_validation"],
    )

    nodes["contact_validation"] = _node(
        node_id="contact_validation",
        capability="contact_validation",
        description="Validate and filter contacts for outreach readiness.",
        dependencies=["linkedin_enrichment"],
        next_nodes=["outreach_recommendation"],
    )

    # Recommendation
    nodes["outreach_recommendation"] = _node(
        node_id="outreach_recommendation",
        capability="outreach_recommendation",
        description="Recommend outreach strategy and messages candidates.",
        dependencies=["contact_validation"],
        next_nodes=["personalization"],
    )

    nodes["personalization"] = _node(
        node_id="personalization",
        capability="personalization",
        description="Personalize outreach for each validated contact.",
        dependencies=["outreach_recommendation"],
        next_nodes=["next_action"],
    )

    nodes["next_action"] = _node(
        node_id="next_action",
        capability="next_action",
        description="Determine next actions for the outreach workflow.",
        dependencies=["personalization"],
        next_nodes=["approval"],
    )

    # HITL
    nodes["approval"] = _node(
        node_id="approval",
        capability="approval",
        description="Human-in-the-loop approval for generated outreach.",
        dependencies=["next_action"],
        next_nodes=[],
    )

    return WorkflowDefinition(
        name="prospect_discovery",
        description="Prospect intelligence workflow (end-to-end).",
        start_node="trigger_monitor",
        nodes=nodes,
        version="1.0.0",
        metadata={"platform": "ProspectIQ"},
    )


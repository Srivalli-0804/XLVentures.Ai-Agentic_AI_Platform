"""
Standard event types used across the platform.
"""

from enum import Enum


class EventType(str, Enum):

    WORKFLOW_STARTED = "workflow_started"
    WORKFLOW_COMPLETED = "workflow_completed"
    WORKFLOW_FAILED = "workflow_failed"

    AGENT_STARTED = "agent_started"
    AGENT_COMPLETED = "agent_completed"
    AGENT_FAILED = "agent_failed"

    TASK_STARTED = "task_started"
    TASK_COMPLETED = "task_completed"

    COMPANY_DISCOVERED = "company_discovered"

    COMPANY_QUALIFIED = "company_qualified"

    COMPANY_ENRICHED = "company_enriched"

    CONTACT_DISCOVERED = "contact_discovered"

    CONTACT_VALIDATED = "contact_validated"

    RECOMMENDATION_GENERATED = "recommendation_generated"

    APPROVAL_REQUESTED = "approval_requested"

    APPROVAL_COMPLETED = "approval_completed"
from __future__ import annotations

from abc import ABC, abstractmethod

from ..base.agent_context import AgentContext


class PlanningStrategy(ABC):
    """
    Abstract strategy for selecting a workflow.

    Different planning implementations can inherit
    from this class.

    Examples:
        - RuleBasedPlanningStrategy
        - LLMPlanningStrategy
        - HybridPlanningStrategy
    """

    @abstractmethod
    async def plan(
        self,
        context: AgentContext,
    ) -> str:
        """
        Returns the workflow name that should
        be executed.

        Parameters
        ----------
        context:
            Shared AgentContext.

        Returns
        -------
        str
            Workflow name.
        """
        raise NotImplementedError


class RuleBasedPlanningStrategy(PlanningStrategy):
    """
    Default planning strategy.

    Uses simple business rules to determine
    which workflow should execute.

    This implementation can later be replaced
    by an LLM without changing PlannerAgent.
    """

    async def plan(
        self,
        context: AgentContext,
    ) -> str:

        query = (context.user_query or "").lower()

        # --------------------------------------------------
        # Prospect Discovery Workflow
        # --------------------------------------------------

        if any(
            keyword in query
            for keyword in [
                "discover",
                "find",
                "prospect",
                "lead",
                "company",
            ]
        ):
            return "prospect_discovery"

        # --------------------------------------------------
        # Contact Enrichment Workflow
        # --------------------------------------------------

        if any(
            keyword in query
            for keyword in [
                "contact",
                "email",
                "linkedin",
                "phone",
                "enrich",
            ]
        ):
            return "contact_enrichment"

        # --------------------------------------------------
        # Recommendation Workflow
        # --------------------------------------------------

        if any(
            keyword in query
            for keyword in [
                "recommend",
                "outreach",
                "next action",
            ]
        ):
            return "recommendation"

        # --------------------------------------------------
        # Default Workflow
        # --------------------------------------------------

        return "prospect_discovery"
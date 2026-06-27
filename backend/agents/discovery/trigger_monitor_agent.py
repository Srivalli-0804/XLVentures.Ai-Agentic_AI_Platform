from __future__ import annotations

from typing import Any, Dict, List

from ..base.base_agent import BaseAgent
from ..base.agent_context import AgentContext


class TriggerMonitorAgent(BaseAgent):
    """
    Monitors incoming business triggers and stores
    relevant trigger information inside the shared context.
    """

    def __init__(self) -> None:
        super().__init__(
            name="Trigger Monitor Agent",
            description="Monitors configured business triggers.",
            capabilities=["trigger_monitor"],
        )

    def validate(self, context: AgentContext) -> None:
        super().validate(context)

        if not context.triggers:
            raise ValueError(
                "No business triggers configured."
            )

    async def _run(
        self,
        context: AgentContext,
    ) -> AgentContext:
        """
        Processes configured triggers.

        For the hackathon, this agent simply converts the
        configured trigger list into structured trigger events.

        Future implementations will monitor:
            - Google News
            - RSS feeds
            - Company websites
            - LinkedIn
            - Funding announcements
        """

        detected_events: List[Dict[str, Any]] = []

        for trigger in context.triggers:

            detected_events.append(
                {
                    "trigger": trigger,
                    "status": "DETECTED",
                }
            )

        context.metadata["trigger_events"] = detected_events

        return context
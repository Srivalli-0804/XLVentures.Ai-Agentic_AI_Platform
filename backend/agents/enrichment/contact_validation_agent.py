from __future__ import annotations

import re
from typing import Dict, List

from ..base.base_agent import BaseAgent
from ..base.agent_context import AgentContext


class ContactValidationAgent(BaseAgent):
    """
    Validates enriched contact information before
    it is passed to the recommendation phase.

    Future implementation will integrate with:
        - Hunter.io
        - Apollo
        - NeverBounce
        - ZeroBounce
    """

    EMAIL_PATTERN = re.compile(
        r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    )

    PHONE_PATTERN = re.compile(
        r"^\+?[0-9]{10,15}$"
    )

    def __init__(self) -> None:
        super().__init__(
            name="Contact Validation Agent",
            description="Validates enriched contact information.",
            capabilities=["contact_validation"],
        )

    def validate(self, context: AgentContext) -> None:
        super().validate(context)

        if not context.contacts:
            raise ValueError(
                "No contacts available for validation."
            )

    async def _run(
        self,
        context: AgentContext,
    ) -> AgentContext:

        validated_contacts: List[Dict] = []

        for contact in context.contacts:

            validated_contact = contact.copy()

            email = validated_contact.get("email")
            phone = validated_contact.get("phone")
            linkedin = validated_contact.get("linkedin")

            email_valid = (
                bool(email)
                and self.EMAIL_PATTERN.match(email) is not None
            )

            phone_valid = (
                bool(phone)
                and self.PHONE_PATTERN.match(phone) is not None
            )

            linkedin_valid = (
                bool(linkedin)
                and linkedin.startswith(
                    "https://www.linkedin.com/"
                )
            )

            validated_contact["validation"] = {
                "email_valid": email_valid,
                "phone_valid": phone_valid,
                "linkedin_valid": linkedin_valid,
            }

            validated_contact["is_valid"] = (
                email_valid
                or phone_valid
                or linkedin_valid
            )

            validated_contact["status"] = (
                "VALIDATED"
                if validated_contact["is_valid"]
                else "INVALID"
            )

            validated_contacts.append(validated_contact)

        context.contacts = validated_contacts

        return context
"""
Workflow execution model.
"""

from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.database.base import Base


class Workflow(Base):
    __tablename__ = "workflows"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    workflow_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="PENDING",
    )

    trigger_source: Mapped[str | None] = mapped_column(
        String(100)
    )

    planner_name: Mapped[str | None] = mapped_column(
        String(100)
    )

    workflow_metadata: Mapped[dict | None] = mapped_column(
        "metadata",
        JSONB
    )

    started_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime
    )

    agent_runs: Mapped[list["AgentRun"]] = relationship(
        back_populates="workflow",
        cascade="all, delete-orphan",
    )
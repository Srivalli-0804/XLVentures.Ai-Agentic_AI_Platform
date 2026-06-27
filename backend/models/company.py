"""
backend/models/company.py

SQLAlchemy model representing a discovered company.
"""

from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import DateTime, Float, Integer, String, Text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship



from backend.database.base import Base


class Company(Base):
    __tablename__ = "companies"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    name: Mapped[str] = mapped_column(String(255), nullable=False)

    website: Mapped[str | None] = mapped_column(String(255))

    domain: Mapped[str | None] = mapped_column(String(255), unique=True)

    industry: Mapped[str | None] = mapped_column(String(100))

    company_size: Mapped[str | None] = mapped_column(String(50))

    employee_count: Mapped[int | None] = mapped_column(Integer)

    headquarters: Mapped[str | None] = mapped_column(String(255))

    country: Mapped[str | None] = mapped_column(String(100))

    linkedin_url: Mapped[str | None] = mapped_column(String(500))

    description: Mapped[str | None] = mapped_column(Text)

    annual_revenue: Mapped[float | None] = mapped_column(Float)

    technology_stack: Mapped[dict | None] = mapped_column(JSONB)

    score: Mapped[float | None] = mapped_column(Float)

    qualification_status: Mapped[str] = mapped_column(
        String(50),
        default="PENDING",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    contacts: Mapped[list["Contact"]] = relationship(
        back_populates="company",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return (
            f"<Company(id={self.id}, "
            f"name='{self.name}', "
            f"score={self.score})>"
        )
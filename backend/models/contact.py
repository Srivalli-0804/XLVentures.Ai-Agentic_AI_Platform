"""
backend/models/contact.py

SQLAlchemy model representing a contact within a company.
"""

from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.database.base import Base


class Contact(Base):
    __tablename__ = "contacts"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    company_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("companies.id", ondelete="CASCADE"),
        nullable=False,
    )

    first_name: Mapped[str] = mapped_column(String(100))

    last_name: Mapped[str] = mapped_column(String(100))

    job_title: Mapped[str | None] = mapped_column(String(200))

    department: Mapped[str | None] = mapped_column(String(100))

    email: Mapped[str | None] = mapped_column(
        String(255),
        unique=True,
    )

    phone: Mapped[str | None] = mapped_column(String(30))

    linkedin_url: Mapped[str | None] = mapped_column(String(500))

    email_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    phone_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    company: Mapped["Company"] = relationship(
        back_populates="contacts"
    )

    def __repr__(self):
        return f"<Contact {self.first_name} {self.last_name}>"
"""
Base event model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any
import uuid

from .event_types import EventType


@dataclass(slots=True)
class Event:
    """
    Represents a platform event.
    """

    event_type: EventType

    payload: dict[str, Any] = field(default_factory=dict)

    workflow_id: str | None = None

    agent_name: str | None = None

    timestamp: datetime = field(default_factory=datetime.utcnow)

    event_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )
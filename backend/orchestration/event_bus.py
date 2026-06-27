"""
Central Event Bus for the Agentic AI Platform.

Supports:
- Publish/Subscribe
- Multiple handlers per event
- Thread-safe
- Easy future migration to Kafka/RabbitMQ
"""

from __future__ import annotations

import logging
from collections import defaultdict
from threading import Lock
from typing import Callable

from backend.orchestration.events.event import Event
from backend.orchestration.events.event_types import EventType

logger = logging.getLogger(__name__)


class EventBus:
    """
    In-memory publish/subscribe event bus.
    """

    def __init__(self) -> None:
        self._subscribers: dict[
            EventType,
            list[Callable[[Event], None]]
        ] = defaultdict(list)

        self._lock = Lock()

    def subscribe(
        self,
        event_type: EventType,
        handler: Callable[[Event], None],
    ) -> None:
        """
        Register a handler for an event.
        """

        with self._lock:
            self._subscribers[event_type].append(handler)

        logger.info(
            "Subscribed %s -> %s",
            handler.__name__,
            event_type.value,
        )

    def unsubscribe(
        self,
        event_type: EventType,
        handler: Callable[[Event], None],
    ) -> None:
        """
        Remove a handler.
        """

        with self._lock:

            if handler in self._subscribers[event_type]:
                self._subscribers[event_type].remove(handler)

    def publish(self, event: Event) -> None:
        """
        Publish an event to all subscribers.
        """

        handlers = self._subscribers.get(event.event_type, [])

        logger.info(
            "Publishing event: %s",
            event.event_type.value,
        )

        for handler in handlers:
            try:
                handler(event)

            except Exception:
                logger.exception(
                    "Event handler failed for %s",
                    event.event_type.value,
                )


# Singleton instance
event_bus = EventBus()
"""
Session Memory

Stores workflow-specific runtime data.
"""

from __future__ import annotations

from typing import Any

from backend.memory.short_term.redis_cache import redis_cache


class SessionMemory:
    """
    Short-term workflow memory.
    """

    PREFIX = "workflow"

    def _key(self, workflow_id: str) -> str:
        return f"{self.PREFIX}:{workflow_id}"

    def save(
        self,
        workflow_id: str,
        data: dict[str, Any],
        ttl: int = 3600,
    ) -> None:
        redis_cache.set(
            self._key(workflow_id),
            data,
            expire_seconds=ttl,
        )

    def load(
        self,
        workflow_id: str,
    ) -> dict[str, Any] | None:
        return redis_cache.get(
            self._key(workflow_id)
        )

    def delete(
        self,
        workflow_id: str,
    ) -> None:
        redis_cache.delete(
            self._key(workflow_id)
        )

    def exists(
        self,
        workflow_id: str,
    ) -> bool:
        return redis_cache.exists(
            self._key(workflow_id)
        )


session_memory = SessionMemory()
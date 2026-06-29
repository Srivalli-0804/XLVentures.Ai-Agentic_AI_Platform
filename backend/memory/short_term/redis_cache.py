"""
In-Memory Cache Manager

Acts as a drop-in replacement for Redis during local
development and hackathons.
"""

from __future__ import annotations

from typing import Any


class RedisCache:
    """
    Simple in-memory cache implementing the same interface
    as the Redis wrapper.
    """

    def __init__(self) -> None:
        self._store: dict[str, Any] = {}

    def set(
        self,
        key: str,
        value: Any,
        expire_seconds: int | None = None,
    ) -> None:
        # expire_seconds ignored for local memory
        self._store[key] = value

    def get(
        self,
        key: str,
    ) -> Any | None:
        return self._store.get(key)

    def delete(
        self,
        key: str,
    ) -> None:
        self._store.pop(key, None)

    def exists(
        self,
        key: str,
    ) -> bool:
        return key in self._store

    def clear(self) -> None:
        self._store.clear()


redis_cache = RedisCache()
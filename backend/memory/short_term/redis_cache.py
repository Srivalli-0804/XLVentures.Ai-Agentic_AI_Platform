"""
Redis Cache Manager

Provides a thin abstraction over Redis for caching and
short-term workflow memory.
"""

from __future__ import annotations

import json
from typing import Any

import redis

from backend.core.settings import settings


class RedisCache:
    """
    Wrapper around Redis client.
    """

    def __init__(self) -> None:
        self.client = redis.Redis.from_url(
            settings.REDIS_URL,
            decode_responses=True,
        )

    def set(
        self,
        key: str,
        value: Any,
        expire_seconds: int | None = None,
    ) -> None:
        """
        Store a value in Redis.
        """
        self.client.set(
            key,
            json.dumps(value),
            ex=expire_seconds,
        )

    def get(self, key: str) -> Any | None:
        """
        Retrieve a value from Redis.
        """
        value = self.client.get(key)

        if value is None:
            return None

        return json.loads(value)

    def delete(self, key: str) -> None:
        """
        Delete a key.
        """
        self.client.delete(key)

    def exists(self, key: str) -> bool:
        """
        Check whether a key exists.
        """
        return bool(self.client.exists(key))

    def clear(self) -> None:
        """
        Flush the Redis database.
        """
        self.client.flushdb()


redis_cache = RedisCache()
"""
Simple in-memory task queue.

Future implementations can replace this with:
- Celery
- Redis Queue
- RabbitMQ
- Kafka
"""

from __future__ import annotations

from collections import deque
from threading import Lock
from typing import Any


class TaskQueue:
    """
    Thread-safe FIFO task queue.
    """

    def __init__(self) -> None:
        self._queue: deque[Any] = deque()
        self._lock = Lock()

    def enqueue(self, task: Any) -> None:
        """
        Add a task to the queue.
        """
        with self._lock:
            self._queue.append(task)

    def dequeue(self) -> Any | None:
        """
        Remove and return the next task.
        """
        with self._lock:
            if not self._queue:
                return None

            return self._queue.popleft()

    def peek(self) -> Any | None:
        """
        Return the next task without removing it.
        """
        with self._lock:
            if not self._queue:
                return None

            return self._queue[0]

    def is_empty(self) -> bool:
        """
        Check whether the queue is empty.
        """
        with self._lock:
            return len(self._queue) == 0

    def size(self) -> int:
        """
        Number of queued tasks.
        """
        with self._lock:
            return len(self._queue)

    def clear(self) -> None:
        """
        Remove all queued tasks.
        """
        with self._lock:
            self._queue.clear()


task_queue = TaskQueue()
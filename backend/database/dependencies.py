"""
Database dependency for FastAPI.
"""

from collections.abc import Generator

from sqlalchemy.orm import Session

from backend.database.session import SessionLocal


def get_db() -> Generator[Session, None, None]:
    """
    FastAPI dependency that provides a SQLAlchemy session.
    """
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
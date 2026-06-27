"""
Database engine configuration.
"""

from sqlalchemy import create_engine

from backend.core.settings import settings

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    echo=False,
    future=True,
)
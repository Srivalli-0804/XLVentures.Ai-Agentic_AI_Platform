"""
backend/core/settings.py

Application settings loaded from environment variables.
"""

from __future__ import annotations

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from backend.core.config_loader import config_loader


class Settings(BaseSettings):
    """
    Global application settings.
    Values are loaded from the .env file.
    """

    # -----------------------------
    # Application
    # -----------------------------
    APP_NAME: str = "ProspectIQ"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = Field(default="development")

    # -----------------------------
    # FastAPI
    # -----------------------------
    HOST: str = Field(default="0.0.0.0")
    PORT: int = Field(default=8000)

    # -----------------------------
    # Database
    # -----------------------------
    DATABASE_URL: str = Field(default="sqlite:///./prospectiq.db")

    # -----------------------------
    # Redis
    # -----------------------------
    REDIS_URL: str = Field(default="redis://localhost:6379")

    # -----------------------------
    # Vector Database
    # -----------------------------
    VECTOR_DB_PATH: str = Field(default="./vector_store")

    # -----------------------------
    # LLM
    # -----------------------------
    OPENAI_API_KEY: str | None = None

    # -----------------------------
    # External Providers
    # -----------------------------
    SERPER_API_KEY: str | None = None
    PROXYCURL_API_KEY: str | None = None
    HUNTER_API_KEY: str | None = None
    APOLLO_API_KEY: str | None = None
    CRUNCHBASE_API_KEY: str | None = None

    # -----------------------------
    # Pydantic Settings
    # -----------------------------
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """
    Returns a cached Settings instance.
    """
    return Settings()


settings = get_settings()

# Shared configuration loader
configs = config_loader
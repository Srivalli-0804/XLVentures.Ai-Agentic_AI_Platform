"""
backend/core/config_loader.py

Centralized YAML configuration loader for the ProspectIQ platform.
Loads, caches and provides access to all YAML configuration files.
"""

from __future__ import annotations

import logging
from pathlib import Path
from threading import Lock
from typing import Any

import yaml

logger = logging.getLogger(__name__)


class ConfigLoader:
    """Loads and caches YAML configuration files."""

    def __init__(self, config_dir: str | Path):
        self.config_dir = Path(config_dir)
        self._cache: dict[str, dict[str, Any]] = {}
        self._lock = Lock()

    def load(self, filename: str) -> dict[str, Any]:
        """
        Load a YAML configuration file.

        Example:
            loader.load("icp.yaml")
        """

        with self._lock:

            if filename in self._cache:
                return self._cache[filename]

            file_path = self.config_dir / filename

            if not file_path.exists():
                raise FileNotFoundError(
                    f"Configuration file not found: {file_path}"
                )

            with open(file_path, "r", encoding="utf-8") as file:
                config = yaml.safe_load(file) or {}

            self._cache[filename] = config

            logger.info("Loaded configuration: %s", filename)

            return config

    def reload(self, filename: str) -> dict[str, Any]:
        """Reload a configuration file."""

        with self._lock:
            self._cache.pop(filename, None)

        return self.load(filename)

    def clear_cache(self) -> None:
        """Clear all cached configuration."""

        with self._lock:
            self._cache.clear()

    def list_configs(self) -> list[str]:
        """Return available YAML configuration files."""

        return sorted(
            file.name
            for file in self.config_dir.glob("*.yaml")
        )

    # --------------------------------------------------------
    # Convenience methods
    # --------------------------------------------------------

    def icp(self):
        return self.load("icp.yaml")

    def personas(self):
        return self.load("personas.yaml")

    def providers(self):
        return self.load("providers.yaml")

    def workflow(self):
        return self.load("workflow.yaml")

    def triggers(self):
        return self.load("triggers.yaml")

    def scoring(self):
        return self.load("scoring.yaml")

        # --------------------------------------------------------
    # Backward compatibility methods
    # --------------------------------------------------------

    def get_icp(self):
        return self.icp()

    def get_personas(self):
        return self.personas()

    def get_providers(self):
        return self.providers()

    def get_workflow(self):
        return self.workflow()

    def get_triggers(self):
        return self.triggers()


PROJECT_ROOT = Path(__file__).resolve().parents[2]

CONFIG_DIR = PROJECT_ROOT / "config"

config_loader = ConfigLoader(CONFIG_DIR)
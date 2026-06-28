from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

import yaml


class ConfigLoader:
    """
    Central configuration loader for the ProspectIQ platform.

    Responsibilities
    ----------------
    - Load YAML configuration files.
    - Cache configurations.
    - Provide a simple API for accessing settings.

    Configuration files:
        config/icp.yaml
        config/personas.yaml
        config/triggers.yaml
        config/providers.yaml
        config/workflow.yaml
    """

    def __init__(
        self,
        config_directory: str = "config",
    ) -> None:

        project_root = Path(__file__).resolve().parents[2]

        self.config_directory = project_root / config_directory

        self._cache: Dict[str, Dict[str, Any]] = {}

    # ---------------------------------------------------------
    # Internal Loader
    # ---------------------------------------------------------

    def _load_yaml(
        self,
        filename: str,
    ) -> Dict[str, Any]:
        """
        Loads a YAML file.

        Uses an in-memory cache so every file
        is loaded only once.
        """

        if filename in self._cache:
            return self._cache[filename]

        file_path = self.config_directory / filename

        if not file_path.exists():
            raise FileNotFoundError(
                f"Configuration file '{filename}' not found."
            )

        with open(
            file_path,
            "r",
            encoding="utf-8",
        ) as file:

            data = yaml.safe_load(file) or {}

        self._cache[filename] = data

        return data

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def get_icp(self) -> Dict[str, Any]:

        return self._load_yaml("icp.yaml")

    def get_personas(self) -> Dict[str, Any]:

        return self._load_yaml("personas.yaml")

    def get_triggers(self) -> Dict[str, Any]:

        return self._load_yaml("triggers.yaml")

    def get_providers(self) -> Dict[str, Any]:

        return self._load_yaml("providers.yaml")

    def get_workflow(self) -> Dict[str, Any]:

        return self._load_yaml("workflow.yaml")

    # ---------------------------------------------------------
    # Utility
    # ---------------------------------------------------------

    def clear_cache(self) -> None:
        """
        Clears all cached configuration.
        """

        self._cache.clear()

    def reload(self) -> None:
        """
        Forces all configuration files
        to be reloaded on the next request.
        """

        self.clear_cache()
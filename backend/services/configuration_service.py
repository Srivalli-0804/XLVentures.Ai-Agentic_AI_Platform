"""
backend/services/configuration_service.py

Service responsible for retrieving platform configuration.
"""

from backend.core.settings import configs


class ConfigurationService:
    """Provides access to YAML configurations."""

    def get_icp(self):
        return configs.icp()

    def get_personas(self):
        return configs.personas()

    def get_triggers(self):
        return configs.triggers()

    def get_workflow(self):
        return configs.workflow()

    def get_providers(self):
        return configs.providers()

    def get_scoring(self):
        return configs.scoring()


configuration_service = ConfigurationService()
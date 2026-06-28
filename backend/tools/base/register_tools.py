"""
Registers all available external tools.
"""

from backend.tools.base.tool_registry import tool_registry
from backend.tools.providers.company.crunchbase_provider import (
    CrunchbaseProvider,
)
from backend.tools.providers.company.score_provider import (
    ScoreProvider,
)
from backend.tools.providers.company.enrichment_provider import (
    EnrichmentProvider,
)
from backend.tools.providers.company.icp_provider import ICPProvider

def register_all_tools() -> None:
    """
    Register every available tool.
    """

    tool_registry.clear()

    # Import here to avoid circular imports
    from backend.tools.providers.news.google_news_provider import (
        GoogleNewsProvider,
    )

    tools = [
        GoogleNewsProvider(),
        CrunchbaseProvider(),
        ICPProvider(),
        ScoreProvider(),
        EnrichmentProvider(),
    ]

    for tool in tools:
        tool_registry.register(tool)
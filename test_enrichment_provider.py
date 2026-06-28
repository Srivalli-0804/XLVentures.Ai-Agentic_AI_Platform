from backend.tools.providers.company.enrichment_provider import (
    EnrichmentProvider,
)

provider = EnrichmentProvider()

companies = [
    {
        "name": "OpenAI",
        "industry": "Artificial Intelligence",
        "country": "USA",
        "employees": 1000,
        "score": 100,
    }
]

print(provider.execute(companies))
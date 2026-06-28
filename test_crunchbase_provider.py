from backend.tools.providers.company.crunchbase_provider import (
    CrunchbaseProvider,
)

provider = CrunchbaseProvider()

events = [
    {
        "company": "OpenAI",
        "event": "Funding Round",
    }
]

print(provider.execute(events))
from backend.tools.providers.company.score_provider import ScoreProvider

provider = ScoreProvider()

companies = [
    {
        "name": "OpenAI",
        "industry": "Artificial Intelligence",
        "country": "USA",
        "employees": 1000,
        "trigger": "Funding Round",
    }
]

print(provider.execute(companies))
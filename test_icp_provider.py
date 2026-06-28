from backend.tools.providers.company.icp_provider import ICPProvider

provider = ICPProvider()

companies = [
    {
        "name": "OpenAI",
        "industry": "Artificial Intelligence",
        "country": "USA",
        "employees": 1000,
    },
    {
        "name": "Local Startup",
        "industry": "Artificial Intelligence",
        "country": "India",
        "employees": 25,
    },
]

qualified = provider.execute(companies)

print(qualified)
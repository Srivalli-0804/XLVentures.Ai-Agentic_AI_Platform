from backend.tools.providers.news.google_news_provider import (
    GoogleNewsProvider,
)

provider = GoogleNewsProvider()

provider.validate()

print(provider.execute())

print()

print(provider.execute("OpenAI"))
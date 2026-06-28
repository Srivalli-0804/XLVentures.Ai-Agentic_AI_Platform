import sys
from pathlib import Path

BACKEND_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BACKEND_DIR))

import asyncio

from tools.providers.news.google_news_provider import GoogleNewsProvider
from tools.providers.news.serper_provider import SerperProvider
from tools.providers.company.crunchbase_provider import CrunchbaseProvider
from tools.providers.linkedin.proxycurl_provider import ProxycurlProvider
from tools.providers.linkedin.apify_provider import ApifyProvider
from tools.providers.email.hunter_provider import HunterProvider
from tools.providers.email.apollo_provider import ApolloProvider
from tools.providers.phone.peopledata_provider import PeopleDataProvider


async def main():

    print("=" * 60)
    print("Testing Tool Providers")
    print("=" * 60)

    google = GoogleNewsProvider()
    print("✓ Google News")
    print(await google.execute(company="OpenAI"))

    serper = SerperProvider()
    print("\n✓ Serper")
    print(await serper.execute(query="OpenAI"))

    crunchbase = CrunchbaseProvider()
    print("\n✓ Crunchbase")
    print(await crunchbase.execute(company="OpenAI"))

    proxycurl = ProxycurlProvider()
    print("\n✓ Proxycurl")
    print(await proxycurl.execute(company="OpenAI"))

    apify = ApifyProvider()
    print("\n✓ Apify")
    print(
        await apify.execute(
            linkedin_url="https://linkedin.com/in/johndoe"
        )
    )

    hunter = HunterProvider()
    print("\n✓ Hunter")
    print(
        await hunter.execute(
            full_name="John Doe",
            company="OpenAI"
        )
    )

    apollo = ApolloProvider()
    print("\n✓ Apollo")
    print(
        await apollo.execute(
            full_name="John Doe",
            company="OpenAI"
        )
    )

    people = PeopleDataProvider()
    print("\n✓ People Data")
    print(
        await people.execute(
            full_name="John Doe",
            company="OpenAI"
        )
    )

    print()
    print("=" * 60)
    print("ALL PROVIDERS PASSED")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())

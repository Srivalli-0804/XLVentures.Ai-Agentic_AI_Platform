from __future__ import annotations

from typing import Any, Dict, Optional

import httpx
from bs4 import BeautifulSoup


class WebScraper:
    """
    Generic web scraper utility.

    Responsible for:
        - Downloading web pages
        - Returning HTML
        - Parsing HTML
    """

    DEFAULT_TIMEOUT = 30

    def __init__(
        self,
        timeout: int = DEFAULT_TIMEOUT,
        headers: Optional[Dict[str, str]] = None,
    ) -> None:

        self.timeout = timeout

        self.headers = headers or {
            "User-Agent": (
                "Mozilla/5.0 "
                "(Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/125.0 Safari/537.36"
            )
        }

    # ---------------------------------------------------------
    # HTTP
    # ---------------------------------------------------------

    async def fetch(
        self,
        url: str,
    ) -> str:
        """
        Downloads a webpage.

        Returns
        -------
        HTML string.
        """

        async with httpx.AsyncClient(
            timeout=self.timeout,
            headers=self.headers,
            follow_redirects=True,
        ) as client:

            response = await client.get(url)

            response.raise_for_status()

            return response.text

    # ---------------------------------------------------------
    # HTML
    # ---------------------------------------------------------

    def parse(
        self,
        html: str,
    ) -> BeautifulSoup:
        """
        Parses HTML into BeautifulSoup.
        """

        return BeautifulSoup(
            html,
            "html.parser",
        )

    # ---------------------------------------------------------
    # Text Extraction
    # ---------------------------------------------------------

    def extract_text(
        self,
        html: str,
    ) -> str:
        """
        Extracts visible text from HTML.
        """

        soup = self.parse(html)

        return soup.get_text(
            separator=" ",
            strip=True,
        )

    # ---------------------------------------------------------
    # Metadata
    # ---------------------------------------------------------

    def extract_metadata(
        self,
        html: str,
    ) -> Dict[str, Any]:
        """
        Extracts basic webpage metadata.
        """

        soup = self.parse(html)

        title = ""

        if soup.title:
            title = soup.title.get_text(strip=True)

        return {
            "title": title,
        }

    # ---------------------------------------------------------
    # Complete Scrape
    # ---------------------------------------------------------

    async def scrape(
        self,
        url: str,
    ) -> Dict[str, Any]:
        """
        Downloads and extracts webpage information.
        """

        html = await self.fetch(url)

        return {
            "url": url,
            "html": html,
            "text": self.extract_text(html),
            "metadata": self.extract_metadata(html),
        }
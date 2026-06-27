from __future__ import annotations

from typing import Any, Dict, List

from bs4 import BeautifulSoup


class HTMLParser:
    """
    Utility class for extracting structured information
    from HTML documents.
    """

    # ---------------------------------------------------------
    # Parsing
    # ---------------------------------------------------------

    def parse(
        self,
        html: str,
    ) -> BeautifulSoup:
        """
        Parses HTML into a BeautifulSoup object.
        """

        return BeautifulSoup(
            html,
            "html.parser",
        )

    # ---------------------------------------------------------
    # Title
    # ---------------------------------------------------------

    def extract_title(
        self,
        soup: BeautifulSoup,
    ) -> str:
        """
        Extracts the page title.
        """

        if soup.title:
            return soup.title.get_text(strip=True)

        return ""

    # ---------------------------------------------------------
    # Headings
    # ---------------------------------------------------------

    def extract_headings(
        self,
        soup: BeautifulSoup,
    ) -> List[str]:
        """
        Extracts all headings (h1-h6).
        """

        headings: List[str] = []

        for level in range(1, 7):
            headings.extend(
                heading.get_text(strip=True)
                for heading in soup.find_all(f"h{level}")
            )

        return headings

    # ---------------------------------------------------------
    # Paragraphs
    # ---------------------------------------------------------

    def extract_paragraphs(
        self,
        soup: BeautifulSoup,
    ) -> List[str]:
        """
        Extracts paragraph text.
        """

        return [
            paragraph.get_text(strip=True)
            for paragraph in soup.find_all("p")
            if paragraph.get_text(strip=True)
        ]

    # ---------------------------------------------------------
    # Links
    # ---------------------------------------------------------

    def extract_links(
        self,
        soup: BeautifulSoup,
    ) -> List[Dict[str, str]]:
        """
        Extracts hyperlinks.
        """

        links: List[Dict[str, str]] = []

        for link in soup.find_all("a", href=True):

            links.append(
                {
                    "text": link.get_text(strip=True),
                    "url": link["href"],
                }
            )

        return links

    # ---------------------------------------------------------
    # Meta Tags
    # ---------------------------------------------------------

    def extract_meta_tags(
        self,
        soup: BeautifulSoup,
    ) -> Dict[str, str]:
        """
        Extracts HTML meta tags.
        """

        metadata: Dict[str, str] = {}

        for meta in soup.find_all("meta"):

            key = meta.get("name") or meta.get("property")

            value = meta.get("content")

            if key and value:
                metadata[key] = value

        return metadata

    # ---------------------------------------------------------
    # Complete Extraction
    # ---------------------------------------------------------

    def extract(
        self,
        html: str,
    ) -> Dict[str, Any]:
        """
        Extracts structured information from HTML.
        """

        soup = self.parse(html)

        return {
            "title": self.extract_title(soup),
            "headings": self.extract_headings(soup),
            "paragraphs": self.extract_paragraphs(soup),
            "links": self.extract_links(soup),
            "metadata": self.extract_meta_tags(soup),
        }
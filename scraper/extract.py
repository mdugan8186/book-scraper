# scraper/extract.py

"""
Parse product data from the saved BooksToScrape HTML.
Uses Selectolax for fast, clean extraction.
"""

from selectolax.parser import HTMLParser
from pathlib import Path
from typing import List, Dict
from urllib.parse import urljoin


BASE_URL = "https://books.toscrape.com/"
HTML_FILE = Path("extras/homepage_2025-07-17_21-33.html")  # Adjust if needed


def extract_books_from_html(html: str) -> List[Dict]:
    """Extract book data from the homepage HTML."""
    tree = HTMLParser(html)
    books = []

    for article in tree.css("article.product_pod"):
        title = article.css_first("h3 a").attributes.get("title", "").strip()
        rel_url = article.css_first("h3 a").attributes.get("href", "")
        product_url = urljoin(BASE_URL, rel_url)

        price = article.css_first("p.price_color").text(strip=True)
        availability = article.css_first(
            "p.instock.availability").text(strip=True)

        star_element = article.css_first("p.star-rating")
        star_rating = star_element.attributes.get(
            "class", "").replace("star-rating", "").strip()

        books.append({
            "title": title,
            "price": price,
            "availability": availability,
            "rating": star_rating,
            "url": product_url
        })

    return books


def load_html_from_file(filepath: Path) -> str:
    """Load HTML content from a local file."""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def main():
    html = load_html_from_file(HTML_FILE)
    books = extract_books_from_html(html)

    for book in books:
        print(book)


if __name__ == "__main__":
    main()

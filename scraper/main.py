# scraper/main.py

"""
Main script to scrape live book data from BooksToScrape.
Step 2: fetch and parse the homepage using extract.py.
"""

from pathlib import Path
import requests
from scraper.extract import extract_books_from_html
from selectolax.parser import HTMLParser
from datetime import datetime
import csv


def get_next_page_url(html: str) -> str | None:
    """Extract the 'next' page URL from the pagination section."""
    tree = HTMLParser(html)
    next_link = tree.css_first("li.next > a")

    if next_link:
        return next_link.attributes["href"]
    return None


BASE_URL = "https://books.toscrape.com/"


def fetch_page(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def main():
    url = BASE_URL
    all_books = []

    while url:
        print(f"Scraping: {url}")
        response = requests.get(url)
        response.raise_for_status()

        html = response.text
        books = extract_books_from_html(html)
        all_books.extend(books)
        print(f"  ↳ Extracted {len(books)} books (total: {len(all_books)})")

        next_page = get_next_page_url(html)
        if next_page:
            # Construct full URL (handle relative links)
            if "catalogue" not in next_page:
                next_page = "catalogue/" + next_page
            url = BASE_URL + next_page
        else:
            url = None

    print(f"\n✅ Done. Extracted {len(all_books)} total books.")

    # Prepare timestamped output filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_path = Path("output") / f"books_{timestamp}.csv"

    # Write to CSV
    with output_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=all_books[0].keys())
        writer.writeheader()
        writer.writerows(all_books)

    print(f"📁 Saved to {output_path}")


if __name__ == "__main__":
    main()

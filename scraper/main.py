# ==== main.py ====

from time import sleep
import requests
from scraper.config import BASE_URL, HEADERS, REQUEST_DELAY
from scraper.extract import extract_books_from_html, get_next_page
from scraper.utils import save_to_csv


def fetch_html(url: str) -> str:
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.text


def scrape_all_books(start_url: str = BASE_URL) -> list[dict]:
    all_books = []
    next_url = start_url

    while next_url:
        print(f"Scraping: {next_url}")
        html = fetch_html(next_url)
        books = extract_books_from_html(html)
        all_books.extend(books)
        print(f"  ↳ Extracted {len(books)} books (total: {len(all_books)})")
        next_url = get_next_page(html, current_url=next_url)

        if REQUEST_DELAY > 0:
            sleep(REQUEST_DELAY)

    return all_books


def main():
    books = scrape_all_books()
    save_to_csv(books)


if __name__ == "__main__":
    main()

# scraper/capture.py

"""
Capture raw HTML from BooksToScrape for parsing and inspection.
Saves the HTML with a timestamped filename in the extras/ folder.
"""

import requests
from pathlib import Path
from datetime import datetime


URL = "https://books.toscrape.com/"
SAVE_DIR = Path("extras")


def fetch_html(url: str) -> str:
    """Fetch the raw HTML content from a given URL."""
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def save_html(content: str, label: str = "homepage") -> str:
    """Save HTML content to a timestamped file in the extras/ folder."""
    SAVE_DIR.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"{label}_{timestamp}.html"
    filepath = SAVE_DIR / filename

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[+] HTML saved to {filepath}")
    return str(filepath)


def main():
    print(f"[+] Fetching HTML from {URL}")
    html = fetch_html(URL)
    save_html(html, label="homepage")


if __name__ == "__main__":
    main()

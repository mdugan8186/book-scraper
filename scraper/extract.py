# ==== extract.py ====

"""
Parse product data from the saved BooksToScrape HTML
and export the results to a timestamped CSV file.
"""

from selectolax.parser import HTMLParser
from scraper.config import BASE_URL, HTML_FILE
from scraper.utils import load_html_from_file, save_to_csv
from urllib.parse import urljoin

# Mapping for converting star rating words to integers
STAR_RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}


def extract_books_from_html(html: str) -> list[dict]:
    """Extract book data from the given HTML using CSS selectors."""
    tree = HTMLParser(html)
    books = []

    for article in tree.css("article.product_pod"):
        title = article.css_first("h3 a").attributes.get("title", "").strip()
        rel_url = article.css_first("h3 a").attributes.get("href", "")
        product_url = urljoin(BASE_URL, rel_url)

        # Clean and convert price to float
        raw_price = article.css_first("p.price_color").text(strip=True)
        price_str = raw_price.replace("Â", "").replace("£", "")
        price = float(price_str)

        availability = article.css_first(
            "p.instock.availability").text(strip=True)

        star_element = article.css_first("p.star-rating")
        star_rating = 0  # Default if not found or unknown
        if star_element:
            rating_str = star_element.attributes.get(
                "class", "").replace("star-rating", "").strip()
            star_rating = STAR_RATING_MAP.get(rating_str, 0)

        books.append({
            "title": title,
            "price": price,
            "availability": availability,
            "rating": star_rating,
            "url": product_url
        })

    return books


def get_next_page(html: str, current_url: str) -> str | None:
    """Find the absolute URL of the next page, relative to the current page."""
    tree = HTMLParser(html)
    next_button = tree.css_first("li.next a")

    if next_button:
        relative_url = next_button.attributes.get("href", "")
        return urljoin(current_url, relative_url)

    return None


def main():
    html = load_html_from_file(HTML_FILE)
    books = extract_books_from_html(html)
    save_to_csv(books)


if __name__ == "__main__":
    main()

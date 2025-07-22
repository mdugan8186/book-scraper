# ==== extract.py ====

"""
Parse product data from the saved BooksToScrape HTML
and export the results to a timestamped CSV file.
"""

from selectolax.parser import HTMLParser
from config import BASE_URL, HTML_FILE
from utils import load_html_from_file, save_to_csv
from urllib.parse import urljoin


def extract_books_from_html(html: str) -> list[dict]:
    """Extract book data from the given HTML using CSS selectors."""
    tree = HTMLParser(html)
    books = []

    for article in tree.css("article.product_pod"):
        title = article.css_first("h3 a").attributes.get("title", "").strip()
        rel_url = article.css_first("h3 a").attributes.get("href", "")
        product_url = urljoin(BASE_URL, rel_url)

        price = article.css_first("p.price_color").text(
            strip=True).replace("£", "")
        availability = article.css_first(
            "p.instock.availability").text(strip=True)

        star_element = article.css_first("p.star-rating")
        star_rating = ""
        if star_element:
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


def main():
    html = load_html_from_file(HTML_FILE)
    books = extract_books_from_html(html)
    save_to_csv(books)


if __name__ == "__main__":
    main()

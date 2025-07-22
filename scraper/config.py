# ==== config.py ====

from pathlib import Path

# Base site URL
BASE_URL = "https://books.toscrape.com/"

# Directory where output files (raw HTML, CSVs, etc.) will be saved
OUTPUT_DIR = Path("output")

# CSV filename template — we'll append a timestamp automatically
CSV_FILENAME_TEMPLATE = "books_{timestamp}.csv"

# Optional: raw HTML filename pattern
RAW_HTML_FILENAME = "homepage_{timestamp}.html"

# Optional: set a delay between requests (if needed for politeness)
REQUEST_DELAY = 0  # 0 = no delay

# Path to the locally saved HTML file used for parsing in extract.py
HTML_FILE = Path("extras/homepage_2025-07-17_21-33.html")

# Custom headers (can help prevent blocking in real-world scraping)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; BookScraperBot/1.0)"
}

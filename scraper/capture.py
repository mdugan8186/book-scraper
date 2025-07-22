# ==== capture.py ====

import requests
from datetime import datetime
from config import BASE_URL, HEADERS, RAW_HTML_TEMPLATE, OUTPUT_DIR


def save_raw_html(content: str, filename_template: str = RAW_HTML_TEMPLATE) -> str:
    """Save raw HTML content to a timestamped file."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    filepath = OUTPUT_DIR / filename_template.format(timestamp=timestamp)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Raw HTML saved to {filepath}")
    return str(filepath)


def main():
    print(f"📥 Requesting: {BASE_URL}")
    response = requests.get(BASE_URL, headers=HEADERS)
    response.raise_for_status()
    html = response.text

    save_raw_html(html)


if __name__ == "__main__":
    main()

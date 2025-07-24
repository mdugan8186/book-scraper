# 📚 Book Scraper

A lightweight web scraper for [BooksToScrape.com](https://books.toscrape.com/), designed to collect book data such as title, price, availability, star rating, and product URL. This project uses `Selectolax` for fast HTML parsing and saves data to timestamped CSV files.

---

## 📦 Features

- Extracts book title, price, availability, star rating, and URL
- Handles pagination to scrape all available books
- Saves extracted data to clean, timestamped CSV files
- Post-processes data to remove artifacts, convert price to floats, and map star ratings
- Includes both raw and cleaned data for transparency
- Lightweight and easy to extend

---

## 🛠️ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/book-scraper.git
cd book-scraper
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

Minimum required packages:

```text
selectolax
pandas
requests
```

(Optionally install `lxml`, `beautifulsoup4`, or `playwright` if you want to extend or adapt scraping features.)

---

## 🚀 Usage

### 1. Scrape and save HTML:

```bash
python3 -m scraper.main
```

This will:

- Scrape the entire book catalog
- Save raw HTML for each page (optional)
- Output a timestamped CSV in the `output/` folder

### 2. Local extract from HTML:

```bash
python3 -m scraper.extract
```

This will:

- Use a saved HTML file
- Extract book data and export to CSV

### 3. Postprocess cleaned data:

```bash
python3 postprocess.py
```

This will:

- Load the latest raw CSV file
- Remove encoding artifacts
- Convert prices to floats
- Map star ratings to integers
- Save the cleaned file to `samples/`
- Save summaries to `summary.md` and `summary.txt`

---

## 📂 Project Structure

```
book-scraper/
├── output/              # Raw extracted CSVs
├── samples/             # Cleaned and validated CSVs
├── extras/              # Saved HTML files for offline parsing
├── scraper/
│   ├── __init__.py
│   ├── config.py        # URL, paths, headers
│   ├── utils.py         # Reusable I/O functions
│   ├── extract.py       # HTML parsing logic
│   └── main.py          # Main scraping loop
├── postprocess.py       # Cleans data, generates summary
├── run.py               # Entry point for live scrape
└── README.md
```

---

## ✍️ Author

**Michael Dugan**  
Built with Python 3.13, Selectolax, and Pandas.  
For feedback or collaboration, reach out via GitHub or project issues.

---

## 📃 License

This project is open-source and available under the [MIT License](LICENSE).

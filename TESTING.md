# Testing – BooksToScrape eCommerce Scraper

## Sanity Flow
1. Run a short scrape (e.g., 1 page)
   ```bash
   python main.py --pages 1
   ```
   - Expects `output/books.csv` to be created

2. Open CSV and verify columns:
   - `title, price, availability, rating, category, product_url, image_url`
   - Optional: `upc, tax, price_excl, price_incl, stock, description`

---

## Selector Checks
- Inspect book cards and detail pages to ensure CSS selectors match current site markup.
- Update selectors in `main.py` (or `config.json`) if fields are missing.

---

## Data Quality
- [ ] Prices normalized (strip currency symbol, convert to float)
- [ ] Ratings mapped consistently (e.g., "Three" → 3)
- [ ] Availability parsed to integer (e.g., "In stock (22 available)" → 22)
- [ ] No duplicate `product_url` entries
- [ ] Category assigned correctly for each book

---

## Pagination
- [ ] Script terminates at last page (no infinite loop)
- [ ] Next-page selector still valid

---

## Troubleshooting
- **Empty CSV**: Check selectors, ensure network requests succeeded
- **Slow runs**: Add `time.sleep()` or throttle requests
- **Encoding issues**: Confirm UTF-8 when saving CSV

---

## Optional Enhancements
- Validate `upc`, `tax`, `price_excl`, `price_incl` if scraping product pages
- Add CLI flags for category/page limits
- Add schema validation test (ensure expected columns exist before saving)

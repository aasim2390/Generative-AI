## Google Shopping Scraper with LLM Integration

### Overview

This project is a Python-based scraper that extracts product information from Google Shopping. The scraper is designed to work like a human with delays and random interactions to avoid detection. 
It also uses LLM-assisted parsing to extract structured product data from HTML snippets for better accuracy.

The project is modular, configurable, and designed to be easy to maintain. Selectors are stored in a JSON file so that minor website changes can be accommodated without modifying the code.

---

### Features

- Scrapes top N products from Google Shopping for a given query.
- Extracts Title, Price, and Image URLs.
- Supports price validation against a reference value.
- Uses LLM for parsing cleaned HTML snippets into structured data.
- Modular design with separate components for scraping, parsing, and utilities.
- Implements human-like delays to avoid triggering captchas.

---

### Project Structure
```graphql
google_shopping_scraper/
│
├─ main.py                  # Entry point for running the scraper
├─ scraper.py               # Playwright-based scraping logic
├─ llm_parser.py            # Handles structured parsing via LLM
├─ utils.py                 # Utility functions (e.g., human_delay)
├─ models.py                # Pydantic models for structured output
├─ input.csv                # Input CSV with product queries and expected prices
└─ requirements.txt         # Python dependencies
```
---

### Usage

1. Populate input.csv with the product queries and expected prices. Example:
```csv
Product,Price
iPhone 16,99999
Samsung Galaxy S23,79999

```

2. Run the scraper:
```bash
python main.py
```

Output:

Prints structured product data with fields:
- title
- price
- image_urls
- isPriceMatch (True if extracted price matches expected)

---

### Notes

- The scraper is **human-like** and includes **random delays** for safer automation.
- **LLM** is used to polish and structure scraped data for better reliability.
- You can extend the project to save data in CSV/JSON or integrate with **databases**.

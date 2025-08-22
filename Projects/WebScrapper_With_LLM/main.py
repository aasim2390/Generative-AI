import asyncio
import csv
from scraper import scrape_google_product
from llm_parser import extract_product_info

async def main():
    input_file = "input.csv"
    output_file = "output.csv"

    products = []
    # Read input.csv
    with open(input_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            query = row["Product"]
            expected_price = int(row["Price"]) if row.get("Price") else None

            html_snippets = await scrape_google_product(query, top_n=3)
            for snippet in html_snippets:
                product_info = extract_product_info(snippet, expected_price)
                products.append(product_info.dict())

    # Save CSV
    keys = ["title","description","price","img_urls","isPriceMatch"]
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(products)

    print("Scraping completed. Output saved to", output_file)

if __name__ == "__main__":
    asyncio.run(main())

import asyncio
from playwright.async_api import async_playwright
from utils import human_delay

async def scrape_google_product(query: str, top_n: int = 3):
    """Scrape Google Shopping and return HTML snippets."""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                       "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        await page.goto("https://www.google.com/shopping")

        # Search product
        await page.fill("textarea[name='q']", query)
        await page.keyboard.press("Enter")
        await human_delay(1000, 15000)

        await page.wait_for_selector("//g-inner-card[@jscontroller]", timeout=45000)

        cards = page.locator("//g-inner-card[@jscontroller]")
        count = await cards.count()
        max_cards = min(top_n, count)

        snippets = []
        for i in range(max_cards):
            card = cards.nth(i)
            html = await card.inner_html()
            snippets.append(html)
            await human_delay(800, 1500)

        await browser.close()
    return snippets

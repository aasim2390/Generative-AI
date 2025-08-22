import asyncio
import re

async def human_delay(min_ms=500, max_ms=1500):
    """Random delay to simulate human behavior."""
    import random
    await asyncio.sleep(random.uniform(min_ms, max_ms) / 1000)

def extract_price(text: str) -> int:
    """Extract price from text like ₹69,900 or $1,299."""
    match = re.search(r'(₹|[$])\s*([\d,]+)', text)
    if match:
        return int(match.group(2).replace(",", ""))
    return None

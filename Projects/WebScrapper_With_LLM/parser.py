from langchain_openai import ChatOpenAI
from pydantic import ValidationError
import re
from models import ProductInfo





def parse_product_html(html: str, expected_price: int = None) -> ProductInfo:
    """
    Extract title, price, images from HTML snippet using regex.
    """
    # Title
    title_match = re.search(r'title="([^"]+)"', html)
    title = title_match.group(1) if title_match else None

    # Price
    price_match = re.search(r'₹\s*([\d,]+)', html)
    price = int(price_match.group(1).replace(',', '')) if price_match else None


    # Images (top 3)
    images = re.findall(r'src="(https://encrypted[^"]+)"', html)
    images = images[:3]

    # Price match
    isPriceMatch = expected_price is not None and price == expected_price

    return ProductInfo(
        title=title,
        price=price,
        images=images,
        isPriceMatch=isPriceMatch
    )


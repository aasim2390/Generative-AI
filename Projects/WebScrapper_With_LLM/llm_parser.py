from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from models import ProductInfo
from utils import extract_price
import re
from dotenv import load_dotenv


load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

parser = PydanticOutputParser(pydantic_object=ProductInfo)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a product data extractor. Extract structured product info."),
    ("user", "You are given partial extracted product data:\n{cleaned_data}\n\n"
             "{format_instructions}")
])

def clean_product_data(html: str):
    """Extract key hints from HTML using regex."""
    # Price
    price = None
    price_match = re.search(r'(₹|[$])\s*([\d,]+)', html)
    if price_match:
        price = int(price_match.group(2).replace(",", ""))

    # Extract the value inside title=""
    title_match = re.search(r'title="([^"]+)"', html)
    title = title_match.group(1) if title_match else None


    # Description fallback
    #desc_match = re.search(r'<div[^>]+class="[^"]*description[^"]*"[^>]*>(.*?)</div>', html, re.DOTALL|re.#IGNORECASE)
    #description = desc_match.group(1).strip() if desc_match else title

    # Images
    img_matches = re.findall(r'src="(https://encrypted[^"]+)"', html)
    img_urls = img_matches[:3] if img_matches else []

    return {
        "title": title,
        #"description": description,
        "price": price,
        "img_urls": img_urls
    }

def extract_product_info(html_snippet: str, expected_price: int = None):
    cleaned_data = clean_product_data(html_snippet)
    input_data = {
        "cleaned_data": cleaned_data,
        "format_instructions": parser.get_format_instructions()
    }

    llm_response_text = llm.predict(prompt.format_prompt(**input_data).to_string())
    product_info = parser.parse(llm_response_text)

    # Fallback to cleaned data if missing
    for key in ["title","price","img_urls"]:
        if not getattr(product_info, key) and cleaned_data.get(key):
            setattr(product_info, key, cleaned_data[key])

    # Price match
    product_info.isPriceMatch = False
    if expected_price and product_info.price and expected_price == product_info.price:
        product_info.isPriceMatch = True

    return product_info

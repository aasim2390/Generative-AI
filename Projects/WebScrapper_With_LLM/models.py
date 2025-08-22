from pydantic import BaseModel
from typing import List, Optional

class ProductInfo(BaseModel):
    title: Optional[str]
    price: Optional[int]
    img_urls: Optional[List[str]] = []
    isPriceMatch: Optional[bool] = False

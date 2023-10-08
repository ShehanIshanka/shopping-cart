from typing import List, Optional

from src.base.infra.http import Request, Response
from src.module.product.domain.product import Product


class CreatProductRequestSchema(Request):
    name: str
    amount: float
    description: Optional[str] = None


class CreatProductResponseSchema(Response):
    id: str


class FetchProductsResponseSchema(Response):
    products: List[Product]


class FetchProductByIdResponseSchema(Response):
    product: Product

from datetime import datetime
from typing import List, Optional

from src.base.infra.http import Request, Response
from src.module.cart.domain.cart import Cart
from src.module.product.domain.product import Product


class CreatCartRequestSchema(Request):
    product_ids: List[str]


class CreatCartResponseSchema(Response):
    id: str
    items: List[Product]
    total: float
    created_time: datetime
    last_modified_time: datetime


class FetchCartByIdResponseSchema(Response):
    cart: Cart

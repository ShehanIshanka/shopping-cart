from datetime import datetime
from typing import List

from src.base.infra.http import Request, Response
from src.module.cart.domain.cart import Cart
from src.module.cart.domain.order import Order
from src.module.product.domain.product import Product


class CreatCartRequestSchema(Request):
    product_ids: List[str]


class CreatCartResponseSchema(Response):
    id: str
    items: List[Product]
    total: float
    created_time: datetime
    last_modified_time: datetime


class FindCartByIdResponseSchema(Response):
    cart: Cart


class AddItemToCartRequestSchema(Response):
    cart_id: str
    item_id: str


class AddItemToCartResponseSchema(Response):
    cart: Cart


class RemoveItemFromCartRequestSchema(Response):
    cart_id: str
    item_id: str


class RemoveItemFromCartResponseSchema(Response):
    cart: Cart


class CheckoutCartRequestSchema(Response):
    cart_id: str
    delivery_time: datetime


class CheckoutCartResponseSchema(Response):
    order: Order

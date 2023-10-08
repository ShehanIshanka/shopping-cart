from dataclasses import dataclass
from datetime import datetime
from typing import List

from src.module.cart.domain.cart_id import CartId
from src.module.product.domain.amount import Amount
from src.module.product.domain.product import Product


@dataclass()
class Cart:
    id: CartId
    items: List[Product]
    total: Amount
    created_time: datetime
    last_modified_time: datetime

    @staticmethod
    def create(
        items: List[Product],
        total: float,
        created_time: datetime,
        last_modified_time: datetime,
    ) -> "Cart":
        return Cart(
            id=CartId.create(),
            items=items,
            total=Amount.create(total),
            created_time=created_time,
            last_modified_time=last_modified_time,
        )

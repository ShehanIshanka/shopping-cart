from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List

from src.module.cart.domain.cart_id import CartId
from src.module.product.domain.amount import Amount
from src.module.product.domain.product import Product


@dataclass()
class Order:
    id: CartId
    items: List[Product]
    total: Amount
    created_time: datetime
    delivery_time: datetime

    def items_to_dict(self) -> List[Dict]:
        return [
            {"id": str(item.id), "name": item.name, "amount": item.amount}
            for item in self.items
        ]

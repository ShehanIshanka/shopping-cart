from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from src.module.product.domain.amount import Amount
from src.module.product.domain.product_id import ProductId


@dataclass()
class Product:
    id: ProductId
    name: str
    amount: Amount
    created_time: datetime
    last_modified_time: datetime
    description: Optional[str] = None

    @staticmethod
    def create(
        name: str,
        amount: float,
        created_time: datetime,
        last_modified_time: datetime,
        product_id: Optional[str] = None,
        description: Optional[str] = None,
    ) -> "Product":
        return Product(
            id=ProductId.create(product_id),
            name=name,
            description=description,
            amount=Amount.create(amount),
            created_time=created_time,
            last_modified_time=last_modified_time,
        )

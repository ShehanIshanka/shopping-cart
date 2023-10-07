from dataclasses import dataclass
from decimal import Decimal, getcontext
from typing import Optional

from src.base.domain import ValueObject

getcontext().prec = 2


@dataclass
class Amount(ValueObject):
    value: Decimal
    currency: Optional[str] = "LKR"

    @staticmethod
    def create(value: float) -> "Amount":
        return Amount(value=Decimal(value))

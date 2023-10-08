from dataclasses import dataclass
from uuid import uuid4

from pydantic import UUID4
from src.base.domain import ValueObject


@dataclass
class ProductId(ValueObject):
    id: UUID4

    @staticmethod
    def create() -> "ProductId":
        return ProductId(id=uuid4())

    def to_str(self) -> str:
        return str(self.id)

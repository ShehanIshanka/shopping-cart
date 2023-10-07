from dataclasses import dataclass
from typing import Optional
from uuid import UUID, uuid4

from pydantic import UUID4
from src.base.domain import ValueObject


@dataclass
class ProductId(ValueObject):
    id: UUID4

    @staticmethod
    def create(id: Optional[str] = None) -> "ProductId":
        return ProductId(id=UUID(id) if id is None else uuid4())

    def to_str(self) -> str:
        return str(self.id)

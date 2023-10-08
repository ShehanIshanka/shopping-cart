from dataclasses import dataclass
from uuid import uuid4

from pydantic import UUID4


@dataclass
class AggregateRoot:
    pass


@dataclass
class Entity:
    pass


@dataclass
class ValueObject:
    pass


@dataclass
class UniqueId(ValueObject):
    id: UUID4

    @staticmethod
    def create() -> "UniqueId":
        return UniqueId(id=uuid4())

    def to_str(self) -> str:
        return str(self.id)

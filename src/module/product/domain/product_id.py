from dataclasses import dataclass

from src.base.domain import UniqueId


@dataclass
class ProductId(UniqueId):
    pass

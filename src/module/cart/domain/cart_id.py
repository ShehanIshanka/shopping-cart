from dataclasses import dataclass

from src.base.domain import UniqueId


@dataclass
class CartId(UniqueId):
    pass

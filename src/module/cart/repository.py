from abc import ABC, abstractmethod
from typing import List, Optional


from src.base.infra.postgres.database import Database
from src.base.infra.postgres.model import CartItemModel, CartModel
from src.module.cart.domain.cart import Cart
from src.module.cart.mapper import CartItemMapper, CartMapper


class CartRepository(ABC):
    @abstractmethod
    def create(self, cart: Cart) -> str:
        raise NotImplementedError

    @abstractmethod
    def add_items_to_cart(self, cart: Cart) -> None:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, cart_id: str) -> Optional[Cart]:
        raise NotImplementedError

    @abstractmethod
    def update(self, cart: Cart) -> Optional[Cart]:
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, cart_id: str) -> bool:
        raise NotImplementedError


class PostgresCartRepositoryImpl(CartRepository):
    def __init__(self, db: Database) -> None:
        self.db: Database = db

    def create(self, cart: Cart) -> str:
        with self.db.get_session() as session:
            cart_model: CartModel = CartMapper.to_persistence(cart)
            session.add(cart_model)

        return cart.id.to_str()

    def add_items_to_cart(self, cart: Cart) -> None:
        with self.db.get_session() as session:
            cart_item_models: List[CartItemModel] = CartItemMapper.to_persistence(cart)
            session.bulk_save_objects(cart_item_models)
            session.commit()

    def find_by_id(self, cart_id: str) -> Optional[Cart]:
        with self.db.get_session() as session:
            cart_model = session.query(CartModel).filter_by(id=cart_id).one()
            print(cart_model.cart_items.__dict__)
            return CartMapper.to_domain(cart_model)

    def update(self, cart: Cart) -> Optional[Cart]:
        raise NotImplementedError

    def delete_by_id(self, cart_id: str) -> bool:
        with self.db.get_session() as session:
            cart = session.query(CartModel).filter_by(id=cart_id).first()
            if cart:
                session.delete(cart)
                session.commit()
                return True

        return False

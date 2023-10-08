from abc import ABC, abstractmethod
from typing import List, Optional


from src.base.infra.postgres.database import Database
from src.base.infra.postgres.model import CartItemModel, CartModel, OrderModel
from src.module.cart.domain.cart import Cart
from src.module.cart.domain.order import Order
from src.module.cart.mapper import CartItemMapper, CartMapper


class CartRepository(ABC):
    @abstractmethod
    def create(self, cart: Cart) -> str:
        raise NotImplementedError

    @abstractmethod
    def add_item_to_cart(self, cart_id: str, item_id: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def add_items_to_cart(self, cart: Cart) -> None:
        raise NotImplementedError

    @abstractmethod
    def remove_item_from_cart(self, cart_id: str, item_id: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, cart_id: str) -> Optional[Cart]:
        raise NotImplementedError

    @abstractmethod
    def create_order(self, order: Order) -> None:
        raise NotImplementedError


class PostgresCartRepositoryImpl(CartRepository):
    def __init__(self, db: Database) -> None:
        self.db: Database = db

    def create(self, cart: Cart) -> str:
        with self.db.get_session() as session:
            cart_model: CartModel = CartMapper.to_persistence(cart)
            session.add(cart_model)

        return cart.id.to_str()

    def add_item_to_cart(self, cart_id: str, item_id: str) -> None:
        with self.db.get_session() as session:
            cart_item_model: CartItemModel = CartItemMapper.to_persistence(
                cart_id=cart_id, item_id=item_id
            )
            session.add(cart_item_model)

    def add_items_to_cart(self, cart: Cart) -> None:
        with self.db.get_session() as session:
            cart_item_models: List[CartItemModel] = CartItemMapper.to_persistence_list(
                cart
            )
            session.bulk_save_objects(cart_item_models)
            session.commit()

    def remove_item_from_cart(self, cart_id: str, item_id: str) -> bool:
        with self.db.get_session() as session:
            cart_itme = (
                session.query(CartItemModel)
                .filter_by(cart_id=cart_id, item_id=item_id)
                .first()
            )
            if cart_itme:
                session.delete(cart_itme)
                session.commit()
                return True

        return False

    def find_by_id(self, cart_id: str) -> Optional[Cart]:
        with self.db.get_session() as session:
            cart_model = session.query(CartModel).filter_by(id=cart_id).one()
            return CartMapper.to_domain(cart_model)

    def create_order(self, order: Order) -> None:
        with self.db.get_session() as session:
            session.add(
                OrderModel(
                    id=order.id,
                    basket=order.items_to_dict(),
                    amount=order.total,
                    delivery_time=order.delivery_time,
                    created_time=order.created_time,
                )
            )

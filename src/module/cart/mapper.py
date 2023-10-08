from typing import List

from src.base.infra.mapper import Mapper
from src.base.infra.postgres.model import CartItemModel, CartModel
from src.module.cart.domain.cart import Cart
from src.module.product.domain.product import Product


class CartMapper(Mapper):
    @staticmethod
    def to_domain(cart_model: CartModel) -> Cart:
        return Cart(
            id=cart_model.id,
            items=[CartItemMapper.to_domain(item) for item in cart_model.cart_items],
            total=cart_model.amount,
            created_time=cart_model.created_time,
            last_modified_time=cart_model.last_modified_time,
        )

    @staticmethod
    def to_persistence(cart: Cart) -> CartModel:
        return CartModel(
            id=cart.id.id,
            amount=cart.total.value,
            created_time=cart.created_time,
            last_modified_time=cart.last_modified_time,
        )


class CartItemMapper(Mapper):
    @staticmethod
    def to_domain(cart_item_model: CartItemModel) -> Product:
        return Product(
            id=cart_item_model.item_id,
            name=cart_item_model.product.name,
            description=cart_item_model.product.description,
            amount=cart_item_model.product.amount,
            created_time=cart_item_model.product.created_time,
            last_modified_time=cart_item_model.product.last_modified_time,
        )

    @staticmethod
    def to_persistence(cart: Cart) -> List[CartModel]:
        return [
            CartItemModel(
                cart_id=cart.id.id,
                item_id=item.id,
                created_time=cart.last_modified_time,
            )
            for item in cart.items
        ]

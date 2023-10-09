from datetime import datetime


from src.base.usecase import UseCase
from src.module.cart.domain.cart import Cart
from src.module.cart.domain.order import Order
from src.module.cart.repository import CartRepository
from src.module.cart.schema import (
    AddItemToCartRequestSchema,
    AddItemToCartResponseSchema,
    CheckoutCartRequestSchema,
    CheckoutCartResponseSchema,
    CreatCartRequestSchema,
    CreatCartResponseSchema,
    FindCartByIdResponseSchema,
    RemoveItemFromCartRequestSchema,
    RemoveItemFromCartResponseSchema,
)
from src.module.product.repository import ProductRepository


class CreateCartUseCase(UseCase):
    def __init__(
        self, product_repo: ProductRepository, cart_repo: CartRepository
    ) -> None:
        self.cart_repo = cart_repo
        self.product_repo = product_repo

    def execute(self, request: CreatCartRequestSchema) -> CreatCartResponseSchema:
        now: datetime = datetime.now()

        total = 0
        products = []
        for product_id in request.product_ids:
            product = self.product_repo.find_by_id(product_id=product_id)
            total += product.amount
            products.append(product)

        cart: Cart = Cart.create(
            items=products,
            total=total,
            created_time=now,
            last_modified_time=now,
        )

        self.cart_repo.create(cart)
        self.cart_repo.add_items_to_cart(cart)

        return CreatCartResponseSchema(
            id=cart.id.to_str(),
            items=cart.items,
            total=cart.total.value,
            created_time=cart.created_time,
            last_modified_time=cart.last_modified_time,
        )


class FindCartByIdUseCase(UseCase):
    def __init__(self, cart_repo: CartRepository) -> None:
        self.cart_repo = cart_repo

    def execute(self, request: str) -> FindCartByIdResponseSchema:
        return FindCartByIdResponseSchema(
            cart=self.cart_repo.find_by_id(cart_id=request)
        )


class AddItemToCartUseCase(UseCase):
    def __init__(self, cart_repo: CartRepository) -> None:
        self.cart_repo = cart_repo

    def execute(
        self, request: AddItemToCartRequestSchema
    ) -> AddItemToCartResponseSchema:
        self.cart_repo.add_item_to_cart(
            cart_id=request.cart_id, item_id=request.item_id
        )

        # Missing update cart table

        return AddItemToCartResponseSchema(
            cart=self.cart_repo.find_by_id(cart_id=request.cart_id)
        )


class RemoveItemFromCartUseCase(UseCase):
    def __init__(self, cart_repo: CartRepository) -> None:
        self.cart_repo = cart_repo

    def execute(
        self, request: RemoveItemFromCartRequestSchema
    ) -> RemoveItemFromCartResponseSchema:
        self.cart_repo.remove_item_from_cart(
            cart_id=request.cart_id, item_id=request.item_id
        )

        # Missing update cart table

        return RemoveItemFromCartResponseSchema(
            cart=self.cart_repo.find_by_id(cart_id=request.cart_id)
        )


class CheckoutCartUseCase(UseCase):
    def __init__(self, cart_repo: CartRepository) -> None:
        self.cart_repo = cart_repo

    def execute(self, request: CheckoutCartRequestSchema) -> CheckoutCartResponseSchema:
        cart: Cart = self.cart_repo.find_by_id(cart_id=request.cart_id)

        order: Order = Order(
            id=cart.id,
            items=cart.items,
            total=cart.total,
            created_time=datetime.now(),
            delivery_time=request.delivery_time,
        )
        self.cart_repo.create_order(order=order)

        return CheckoutCartResponseSchema(order=order)

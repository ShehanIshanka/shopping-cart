from datetime import datetime

from src.base.infra.http import Request, Response
from src.base.usecase import UseCase
from src.module.cart.domain.cart import Cart
from src.module.cart.repository import CartRepository
from src.module.cart.schema import (
    CreatCartRequestSchema,
    CreatCartResponseSchema,
    FetchCartByIdResponseSchema,
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

    def execute(self, request: str) -> FetchCartByIdResponseSchema:
        return FetchCartByIdResponseSchema(
            cart=self.cart_repo.find_by_id(cart_id=request)
        )


class DeleteCartByIdUseCase(UseCase):
    def __init__(self, cart_repo: CartRepository) -> None:
        self.cart_repo = cart_repo

    def execute(self, request: str) -> bool:
        return self.cart_repo.delete_by_id(cart_id=request)

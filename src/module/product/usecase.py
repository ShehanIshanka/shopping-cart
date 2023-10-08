from datetime import datetime

from src.base.infra.http import Request, Response
from src.base.usecase import UseCase
from src.module.product.domain.product import Product
from src.module.product.repository import ProductRepository
from src.module.product.schema import (
    CreatProductResponseSchema,
    FetchProductByIdResponseSchema,
    FetchProductsResponseSchema,
)


class CreateProductUseCase(UseCase):
    def __init__(self, product_repo: ProductRepository) -> None:
        self.product_repo = product_repo

    def execute(self, request: Request) -> Response:
        now: datetime = datetime.now()
        product_id: str = self.product_repo.create(
            Product.create(
                name=request.name,
                description=request.description,
                amount=request.amount,
                created_time=now,
                last_modified_time=now,
            )
        )

        return CreatProductResponseSchema(id=product_id)


class FetchProductsUseCase(UseCase):
    def __init__(self, product_repo: ProductRepository) -> None:
        self.product_repo = product_repo

    def execute(self, request: Request = None) -> Response:
        products = self.product_repo.fetch_products()

        return FetchProductsResponseSchema(products=products)


class FindProductByIdUseCase(UseCase):
    def __init__(self, product_repo: ProductRepository) -> None:
        self.product_repo = product_repo

    def execute(self, request: str) -> Response:
        return FetchProductByIdResponseSchema(
            product=self.product_repo.find_by_id(product_id=request)
        )


class DeleteProductByIdUseCase(UseCase):
    def __init__(self, product_repo: ProductRepository) -> None:
        self.product_repo = product_repo

    def execute(self, request: str) -> bool:
        return self.product_repo.delete_by_id(product_id=request)

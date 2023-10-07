from datetime import datetime

from src.base.infra.http import Request
from src.base.usecase import UseCase
from src.module.product.domain.product import Product
from src.module.product.repository import ProductRepository


class CreateProductUseCase(UseCase):
    def __init__(self, product_repo: ProductRepository) -> None:
        self.product_repo = product_repo

    def execute(self, request: Request) -> None:
        now: datetime = datetime.now()
        self.product_repo.create(
            Product.create(
                name=request.name,
                amount=request.amount,
                created_time=now,
                last_modified_time=now,
            )
        )


class FindProductByIdUseCase(UseCase):
    def __init__(self, product_repo: ProductRepository) -> None:
        self.product_repo = product_repo

    def execute(self, request: str) -> Product:
        return self.product_repo.find_by_id(product_id=request)

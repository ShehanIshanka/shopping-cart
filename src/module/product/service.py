import json
import requests
from typing import Optional

from pydantic import ValidationError
from src.base.exceptions import DatabaseError
from src.base.infra.http import Response
from src.module.product.domain.product import Product
from src.module.product.repository import ProductRepository
from src.module.product.schema import CreatProductPostRequestSchema
from src.module.product.usecase import CreateProductUseCase


class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self._product_repository: ProductRepository = product_repository

    def create_product_record(self, data: json) -> Response:
        try:
            data = CreatProductPostRequestSchema.model_validate(data)
        except ValidationError as e:
            return Response(msg=str(e), status=requests.codes.bad_request)

        try:
            CreateProductUseCase(product_repo=self._product_repository).execute(data)
        except DatabaseError as e:
            return Response(msg=str(e), status=requests.codes.bad_request)

        return Response(msg="Success")

    def fetch_product_by_id(self, product_id: str) -> Response:
        pass
        # try:
        #     product_dto: ProductDTO = self.session.query(ProductDTO).filter_by(id=product_id).one()
        # except NoResultFound:
        #     return None
        # except:

    def fetch_products(self) -> Response:
        pass

    def delete_product_by_id(self, product_id: str) -> Response:
        pass

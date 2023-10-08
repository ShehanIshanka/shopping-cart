import json
import logging

import requests
from pydantic import ValidationError
from src.base.exceptions import DatabaseError, NoResultFoundError
from src.base.infra.http import HttpResponse, Response
from src.module.product.repository import ProductRepository
from src.module.product.schema import CreatProductRequestSchema
from src.module.product.usecase import (
    CreateProductUseCase,
    DeleteProductByIdUseCase,
    FetchProductsUseCase,
    FindProductByIdUseCase,
)


class ProductService:
    def __init__(self, product_repository: ProductRepository) -> None:
        self._product_repository: ProductRepository = product_repository

    def create_product_record(self, data: json) -> Response:
        try:
            data = CreatProductRequestSchema.model_validate(data)
            response: Response = CreateProductUseCase(
                product_repo=self._product_repository
            ).execute(data)
        except ValidationError as e:
            logging.exception(e)
            return HttpResponse(
                msg="Validation Error", status=requests.codes.bad_request
            )
        except DatabaseError as e:
            logging.exception(e)
            return HttpResponse(
                msg="Database Error", status=requests.codes.server_error
            )

        logging.info("Successfully created product record.")
        return response

    def fetch_products(self) -> Response:
        try:
            response: Response = FetchProductsUseCase(
                product_repo=self._product_repository
            ).execute()
        except ValidationError as e:
            logging.exception(e)
            return HttpResponse(
                msg="Validation Error", status=requests.codes.bad_request
            )
        except DatabaseError as e:
            logging.exception(e)
            return HttpResponse(
                msg="Database Error", status=requests.codes.server_error
            )

        logging.info("Successfully fetched products.")
        return response

    def fetch_product_by_id(self, product_id: str) -> Response:
        try:
            response: Response = FindProductByIdUseCase(
                product_repo=self._product_repository
            ).execute(product_id)
        except ValidationError as e:
            logging.exception(e)
            return HttpResponse(
                msg="Validation Error", status=requests.codes.bad_request
            )
        except NoResultFoundError:
            logging.info(f"No result found for product id: {product_id}")
            return HttpResponse(msg="No result found.", status=requests.codes.not_found)
        except DatabaseError as e:
            logging.exception(e)
            return HttpResponse(
                msg="Database Error", status=requests.codes.server_error
            )

        logging.info(f"Successfully fetched product id: {product_id}")
        return response

    def delete_product_by_id(self, product_id: str) -> Response:
        try:
            response = DeleteProductByIdUseCase(
                product_repo=self._product_repository
            ).execute(product_id)
        except ValidationError as e:
            logging.exception(e)
            return HttpResponse(
                msg="Validation Error", status=requests.codes.bad_request
            )
        except DatabaseError as e:
            logging.exception(e)
            return HttpResponse(
                msg="Database Error", status=requests.codes.server_error
            )

        if response:
            logging.info(f"Successfully deleted product id: {product_id}")
            return HttpResponse(msg="Success", status=requests.codes.ok)
        else:
            logging.info(f"Product id: {product_id} does not exist.")
            return HttpResponse(
                msg=f"Product id: {product_id} does not exist.",
                status=requests.codes.ok,
            )

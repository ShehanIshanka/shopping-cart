import json
import logging

import requests
from pydantic import ValidationError
from src.base.exceptions import DatabaseError, NoResultFoundError
from src.base.infra.http import HttpResponse, Response
from src.module.cart.repository import CartRepository
from src.module.cart.schema import CreatCartRequestSchema
from src.module.cart.usecase import (
    CreateCartUseCase,
    DeleteCartByIdUseCase,
    FindCartByIdUseCase,
)
from src.module.product.repository import ProductRepository


class CartService:
    def __init__(
        self, product_repository: ProductRepository, cart_repository: CartRepository
    ) -> None:
        self._cart_repository: CartRepository = cart_repository
        self._product_repository: ProductRepository = product_repository

    def create_cart_record(self, data: json) -> Response:
        try:
            data = CreatCartRequestSchema.model_validate(data)
            response: Response = CreateCartUseCase(
                product_repo=self._product_repository, cart_repo=self._cart_repository
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

        logging.info("Successfully created cart record.")
        return response

    def fetch_cart_by_id(self, cart_id: str) -> Response:
        try:
            response: Response = FindCartByIdUseCase(
                cart_repo=self._cart_repository
            ).execute(cart_id)
        except ValidationError as e:
            logging.exception(e)
            return HttpResponse(
                msg="Validation Error", status=requests.codes.bad_request
            )
        except NoResultFoundError:
            logging.info(f"No result found for cart id: {cart_id}")
            return HttpResponse(msg="No result found.", status=requests.codes.not_found)
        except DatabaseError as e:
            logging.exception(e)
            return HttpResponse(
                msg="Database Error", status=requests.codes.server_error
            )

        logging.info(f"Successfully fetched cart id: {cart_id}")
        return response

    def delete_cart_by_id(self, cart_id: str) -> Response:
        try:
            response = DeleteCartByIdUseCase(cart_repo=self._cart_repository).execute(
                cart_id
            )
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
            logging.info(f"Successfully deleted cart id: {cart_id}")
            return HttpResponse(msg="Success", status=requests.codes.ok)
        else:
            logging.info(f"Cart id: {cart_id} does not exist.")
            return HttpResponse(
                msg=f"Cart id: {cart_id} does not exist.",
                status=requests.codes.ok,
            )

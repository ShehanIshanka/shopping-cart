import logging

from flask import Blueprint, current_app, jsonify, request, Response


products = Blueprint("products", __name__, url_prefix="/v1")


@products.route("/", methods=["GET", "POST"])
def product() -> Response:
    print("aaaaaa")
    logging.info(request.data)
    if request.method == "GET":
        return jsonify(current_app.product_service.fetch_products(request.data).dict())

    if request.method == "POST":
        logging.info(request.data)
        return jsonify(
            current_app.product_service.create_product_record(request.data).dict()
        )


# @products.route("/", methods=["GET"])
# def fetch_products() -> Response:
#     print("aaa")
#     return jsonify(current_app.product_service.fetch_products(request.data).dict())


@products.route("/<product_id>", methods=["GET"])
def fetch_product(product_id: str) -> Response:
    return jsonify(
        current_app.product_service.fetch_product_by_id(product_id=product_id).dict()
    )


@products.route("/<product_id>", methods=["DELETE"])
def delete_product(product_id: str) -> Response:
    return jsonify(
        current_app.product_service.delete_product_by_id(product_id=product_id).dict()
    )

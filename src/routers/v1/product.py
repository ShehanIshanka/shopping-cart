from flask import Blueprint, current_app, jsonify, request, Response


products = Blueprint("products", __name__, url_prefix="/v1")


@products.route("/products", methods=["POST"])
def create_product() -> Response:
    # if request.method == "GET":
    #     return jsonify(current_app.product_service.fetch_products(request.data).dict())
    #
    # if request.method == "POST":
    return jsonify(
        current_app.product_service.create_product_record(request.get_json()).dict()
    )


@products.route("/products", methods=["GET"])
def fetch_products() -> Response:
    return jsonify(current_app.product_service.fetch_products().dict())

    # if request.method == "POST":
    #     return jsonify(
    #         current_app.product_service.create_product_record(request.get_json()).dict()
    #     )


@products.route("/products/<product_id>", methods=["GET"])
def fetch_product(product_id: str) -> Response:
    return jsonify(
        current_app.product_service.fetch_product_by_id(product_id=product_id).dict()
    )


@products.route("/products/<product_id>", methods=["DELETE"])
def delete_product(product_id: str) -> Response:
    return jsonify(
        current_app.product_service.delete_product_by_id(product_id=product_id).dict()
    )

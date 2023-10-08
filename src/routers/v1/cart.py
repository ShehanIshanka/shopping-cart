from flask import Blueprint, current_app, jsonify, request, Response


carts = Blueprint("carts", __name__, url_prefix="/v1")


@carts.route("/carts", methods=["POST"])
def create_cart() -> Response:
    return jsonify(
        current_app.cart_service.create_cart_record(request.get_json()).dict()
    )


@carts.route("/carts/<cart_id>/items", methods=["GET"])
def fetch_cart_items(cart_id: str) -> Response:
    return jsonify(current_app.cart_service.fetch_cart_by_id(cart_id=cart_id).dict())


@carts.route("/carts/<cart_id>/items/<item_id>", methods=["PUT"])
def add_item_to_cart(cart_id: str, item_id: str) -> Response:
    return jsonify(current_app.cart_service.fetch_cart_by_id(cart_id=cart_id).dict())


@carts.route("/carts/<cart_id>/items/<item_id>", methods=["DELETE"])
def remove_item_from_cart(cart_id: str) -> Response:
    return jsonify(current_app.cart_service.fetch_cart_by_id(cart_id=cart_id).dict())


@carts.route("/carts/<cart_id>/checkout", methods=["POST"])
def checkout_cart(cart_id: str) -> Response:
    return jsonify(current_app.cart_service.delete_cart_by_id(cart_id=cart_id).dict())

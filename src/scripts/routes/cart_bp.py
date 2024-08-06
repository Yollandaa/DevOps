"""
    @authors: Caleb Potts - E1005278, Yolanda Dastile - 
    Summary: Handles CRUD operations for shopping carts,
    fetching initial data from an API and a local file, 
    and performing create, read, update, and delete actions 
    on the carts, while saving changes to the local file. 
    Last modufied date: 02/08/2024
    Last modufied usesr: Caleb Potts
"""

from flask import Blueprint, request, jsonify
from scripts.data.data import DataHandler

carts_bp = Blueprint("carts_bp", __name__)


# Get all carts
@carts_bp.route("/", methods=["GET"])
def get_carts():
    return jsonify(DataHandler.all_carts_api_call), 200


# Get cart by id
@carts_bp.route("/<int:cart_id>", methods=["GET"])
def get_cart_by_id(cart_id):
    # Filter carts_data to find the cart with the matching id
    cart = next(
        (cart for cart in DataHandler.all_carts_api_call if cart["id"] == cart_id), None
    )
    if cart:
        return jsonify(cart), 200
    else:
        return jsonify({"error": "Cart not found"}), 404


# Post new Cart
@carts_bp.route("/", methods=["POST"])
def post_cart():
    new_cart = request.json
    # Generate a new ID for the cart
    new_cart["id"] = (
        max([cart["id"] for cart in DataHandler.all_carts_api_call]) + 1
        if DataHandler.all_carts_api_call
        else 1
    )
    DataHandler.all_carts_api_call.append(new_cart)

    return jsonify(new_cart), 201


# Delete a Cart using ID
@carts_bp.route("/<int:cart_id>", methods=["DELETE"])
def delete_cart(cart_id):
    cart = next(
        (cart for cart in DataHandler.all_carts_api_call if cart["id"] == cart_id), None
    )
    if cart:
        DataHandler.all_carts_api_call.remove(cart)
        return jsonify({"message": "Cart deleted successfully"}), 200
    else:
        return jsonify({"error": "Cart not found"}), 404


# Edit Cart using ID
@carts_bp.route("/<int:cart_id>", methods=["PUT"])
def edit_cart(cart_id):
    edit_cart_data = request.json
    cart = next(
        (cart for cart in DataHandler.all_carts_api_call if cart["id"] == cart_id), None
    )

    if cart:
        # Update the cart with the new data
        cart.update(edit_cart_data)
        return jsonify({"message": "Cart updated successfully"}), 200
    else:
        return jsonify({"error": "Cart not found"}), 404

"""
    @authors: Caleb Potts - E1005278, Yolanda Dastile - 
    Summary: Handles CRUD operations for shopping carts,
    fetching initial data from an API and a local file, 
    and performing create, read, update, and delete actions 
    on the carts, while saving changes to the local file. 
    Last modufied date: 02/08/2024
    Last modufied usesr: Caleb Potts
"""

import os
from flask import Blueprint, request, jsonify
from scripts.data.data import DataHandler
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("DATA.RESOURCE.API.CARTS.URL")
CARTS_FILE = os.getenv("DATA.RESOURCE.CARTS.FILE")

carts_bp = Blueprint("carts_bp", __name__)

# Since we can't edit the fakestore api, let's create a local copy of the data
carts_data = DataHandler.fetch_initial_data(BASE_URL, CARTS_FILE)


# Get all carts
@carts_bp.route("/", methods=["GET"])
def get_carts():
    return jsonify(carts_data), 200


# Get product with id
@carts_bp.route("/<int:cart_id>", methods=["GET"])
def get_cart_by_id(cart_id):
    cart = next((cart for cart in carts_data if cart["id"] == cart_id), None)
    if cart:
        return jsonify(cart), 200
    else:
        return jsonify({"error": "Cart not found"}), 404


# Post new Product
@carts_bp.route("/", methods=["POST"])
def post_cart():
    new_cart = request.json
    new_cart["id"] = max([cart["id"] for cart in carts_data]) + 1 if carts_data else 1
    carts_data.append(new_cart)

    # Save the new product to the JSON file
    DataHandler.save_to_file(new_cart, CARTS_FILE)

    return jsonify(new_cart), 201


# Delete a product using id
@carts_bp.route("/<int:cart_id>", methods=["DELETE"])
def delete_cart(cart_id):
    global carts_data
    cart = next((cart for cart in carts_data if cart["id"] == cart_id), None)
    if cart:
        carts_data.remove(cart)
        DataHandler.remove_product_in_file(
            cart, CARTS_FILE
        )  # Remove product from JSON file if it is there
        return jsonify({"message": "Cart deleted successfully"}), 200
    else:
        return jsonify({"error": "Cart not found"}), 404


# Edit product using id
@carts_bp.route("/<int:cart_id>", methods=["PUT"])
def edit_cart(cart_id):
    global carts_data
    edit_cart = request.json

    cart = next((cart for cart in carts_data if cart["id"] == cart_id), None)

    if cart:
        # Update the product with the new data
        cart.update(edit_cart)

        # Update the local JSON file if data is there
        if DataHandler.update_product_in_file(cart, CARTS_FILE):
            return jsonify({"message": "Cart updated successfully"}), 200
        else:
            return jsonify({"error": "Failed to update JSON file"}), 500
    else:
        return jsonify({"error": "Cart not found"}), 404

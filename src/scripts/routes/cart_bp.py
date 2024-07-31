from flask import Blueprint, request, jsonify
from scripts.data.data import *
import json
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("DATA.RESOURCE.API.CARTS.URL")
CARTS_FILE = os.getenv("CARTS_FILE")


carts_bp = Blueprint("carts_bp", __name__)

carts = fetch_initial_data(BASE_URL, CARTS_FILE)


@carts_bp.route("/", methods=["GET"])
def get_carts():
    return jsonify(carts), 200


@carts_bp.route("/<int:id>", methods=["GET"])
def get_cart_by_id(id):
    filtered_carts = [cart for cart in carts if cart["id"] == id]
    if filtered_carts:
        return jsonify(filtered_carts), 200
    else:
        return jsonify({"message": "Cart not found"}), 404


@carts_bp.route("/", methods=["POST"])
def add_cart():
    try:
        cart_data = request.get_json()

        if carts:
            max_id = max(cart["id"] for cart in carts)
        else:
            max_id = 0

        cart_data["id"] = max_id + 1
        carts.append(cart_data)

        save_to_file(cart_data, CARTS_FILE)
        return jsonify({"message": "Cart added successfully"}), 201
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)}), 500


@carts_bp.route("/<int:id>", methods=["PUT"])
def update_cart(id):
    try:
        global carts
        updated_data = request.get_json()
        for index, cart in enumerate(carts):
            if cart["id"] == id:
                carts[index] = {**cart, **updated_data}
                save_to_file(carts, CARTS_FILE)
                return jsonify({"message": "Cart updated successfully"}), 200
        return jsonify({"message": "Cart not found"}), 404
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)}), 500


@carts_bp.route("/<int:id>", methods=["DELETE"])
def delete_cart(id):
    try:
        global carts
        new_carts = [cart for cart in carts if cart["id"] != id]

        if len(new_carts) < len(carts):
            carts = new_carts
            save_to_file(carts, CARTS_FILE)
            return jsonify({"message": "Cart deleted successfully"}), 200
        else:
            return jsonify({"message": "Cart not found"}), 404
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)}), 500

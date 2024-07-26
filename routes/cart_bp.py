from flask import Blueprint, request, jsonify
import requests
import json
import os

carts_bp = Blueprint("carts_bp", __name__)
BASE_URL = "https://fakestoreapi.com/carts/"
CARTS_FILE = "carts.json"

if not os.path.exists(CARTS_FILE):
    with open(CARTS_FILE, "w") as file:
        json.dump([], file)


def fetch_carts():
    response = requests.get(BASE_URL, verify=False)
    api_carts = response.json()

    with open(CARTS_FILE, "r") as file:
        local_carts = json.load(file)

    carts = local_carts + api_carts
    return carts


def save_cart(carts):
    with open(CARTS_FILE, "w") as file:
        json.dump(carts, file)


@carts_bp.route("/", methods=["GET"])
def get_carts():
    carts = fetch_carts()
    return jsonify(carts), 200


@carts_bp.route("/<int:id>", methods=["GET"])
def get_cart_by_id(id):
    carts = fetch_carts()
    filtered_carts = [cart for cart in carts if cart["id"] == id]
    if filtered_carts:
        return jsonify(filtered_carts), 200
    else:
        return jsonify({"message": "Cart not found"}), 404


@carts_bp.route("/", methods=["POST"])
def add_cart():
    try:
        cart_data = request.get_json()
        carts = fetch_carts()

        if carts:
            max_id = max(cart["id"] for cart in carts)
        else:
            max_id = 0

        cart_data["id"] = max_id + 1
        carts.append(cart_data)

        save_cart(carts)
        return jsonify({"message": "Cart added successfully"}), 201
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)}), 500


@carts_bp.route("/<int:id>", methods=["PUT"])
def update_cart(id):
    try:
        updated_data = request.get_json()
        carts = fetch_carts()
        for index, cart in enumerate(carts):
            if cart["id"] == id:
                carts[index] = {**cart, **updated_data}
                save_cart(carts)
                return jsonify({"message": "Cart updated successfully"}), 200
        return jsonify({"message": "Cart not found"}), 404
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)}), 500


@carts_bp.route("/<int:id>", methods=["DELETE"])
def delete_cart(id):
    try:
        carts = fetch_carts()
        new_carts = [cart for cart in carts if cart["id"] != id]
        if len(new_carts) < len(carts):
            save_cart(new_carts)
            return jsonify({"message": "Cart deleted successfully"}), 200
        else:
            return jsonify({"message": "Cart not found"}), 404
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)}), 500

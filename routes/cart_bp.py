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


def save_cart(cart):
    with open(CARTS_FILE, "r") as file:
        carts = json.load(file)

    carts.append(cart)

    with open(CARTS_FILE, "w") as file:
        json.dump(carts, file)


@carts_bp.route("/", methods=["GET"])
def get_carts():
    carts = fetch_carts()
    return jsonify(carts), 200


@carts_bp.route("/<int:id>", methods=["GET"])
def get_user_by_name(name):
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
        save_cart(cart_data)
        return jsonify({"message": "Cart added successfully"}), 201
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)}), 500

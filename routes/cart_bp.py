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

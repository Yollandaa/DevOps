from flask import Blueprint, request, jsonify
import requests

carts_bp = Blueprint("carts_bp", __name__)
BASE_URL = "https://fakestoreapi.com/carts/"


@carts_bp.route("/", methods=["GET"])
def get_carts():
    response = requests.get(BASE_URL, verify=False)
    carts = response.json()
    return jsonify(carts), response.status_code

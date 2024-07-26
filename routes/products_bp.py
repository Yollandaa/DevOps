from flask import Blueprint, request, jsonify
import requests

products_bp = Blueprint("products_bp", __name__)
BASE_URL = "https://fakestoreapi.com/products"


@products_bp.route("/", methods=["GET"])
def get_products():
    response = requests.get(BASE_URL, verify=False)
    products = response.json()
    return jsonify(products), response.status_code


@products_bp.route("/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id):
    response = requests.get(f"{BASE_URL}/{product_id}", verify=False)
    product = response.json()
    return jsonify(product), response.status_code


@products_bp.route("/categories", methods=["GET"])
def get_categories():
    response = requests.get(f"{BASE_URL}/categories", verify=False)
    categories = response.json()
    return jsonify(categories), response.status_code


@products_bp.route("/category/<string:category_name>", methods=["GET"])
def get_products_in_category(category_name):
    response = requests.get(f"{BASE_URL}/category/{category_name}", verify=False)
    products = response.json()
    return jsonify(products), response.status_code

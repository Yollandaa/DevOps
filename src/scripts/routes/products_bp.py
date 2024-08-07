"""
    @authors: Caleb Potts - E1005278, Yolanda Dastile - 
    Summary: Handles CRUD operations for products,
    fetching initial data from an API and a local file, 
    and performing create, read, update, and delete actions 
    on the carts, while saving changes to the local file. 
    Last modufied date: 02/08/2024
    Last modufied usesr: Caleb Potts
"""

from flask import Blueprint, request, jsonify
from scripts.data.data import DataHandler

products_bp = Blueprint("products_bp", __name__)


# Get all products
@products_bp.route("/v1/products", methods=["GET"])
def get_products():
    return jsonify(DataHandler.all_products_api_call), 200


# Get product with id
@products_bp.route("/v1/products/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id):
    product = next(
        (
            prod
            for prod in DataHandler.all_products_api_call
            if prod["id"] == product_id
        ),
        None,
    )
    if product:
        return jsonify(product), 200
    else:
        return jsonify({"error": "Product not found"}), 404


# Gat all categories
@products_bp.route("/v1/products/categories", methods=["GET"])
def get_categories():
    categories = {product["category"] for product in DataHandler.all_products_api_call}
    return jsonify({"categories": list(categories)}), 200


# Get all products in a specific category
@products_bp.route("/v1/products/category/<string:category_name>", methods=["GET"])
def get_products_in_category(category_name):
    category_products = [
        prod
        for prod in DataHandler.all_products_api_call
        if prod["category"] == category_name
    ]
    return jsonify(category_products), 200


# Post new Product
@products_bp.route("/v1/products", methods=["POST"])
def post_product():
    new_product = request.json
    new_product["id"] = (
        max([prod["id"] for prod in DataHandler.all_products_api_call]) + 1
        if DataHandler.all_products_api_call
        else 1
    )
    DataHandler.all_products_api_call.append(new_product)

    return jsonify(new_product), 201


# Delete a product using id
@products_bp.route("/v1/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    product = next(
        (
            prod
            for prod in DataHandler.all_products_api_call
            if prod["id"] == product_id
        ),
        None,
    )
    if product:
        DataHandler.all_products_api_call.remove(product)
        return jsonify({"message": "Product deleted successfully"}), 200
    else:
        return jsonify({"error": "Product not found"}), 404


# Edit product using id
@products_bp.route("/v1/products/<int:product_id>", methods=["PUT"])
def edit_product(product_id):
    edit_product = request.json
    product = next(
        (
            prod
            for prod in DataHandler.all_products_api_call
            if prod["id"] == product_id
        ),
        None,
    )
    if product:
        # Update the product with the new data
        product.update(edit_product)
        return jsonify({"message": "Product updated successfully"}), 200
    else:
        return jsonify({"error": "Product not found"}), 404

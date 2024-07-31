import json
from flask import Blueprint, request, jsonify
from scripts.data.data import fetch_initial_data

products_bp = Blueprint("products_bp", __name__)
BASE_URL = "https://fakestoreapi.com/products"
PRODUCTS_FILE = "products.json"

# Since we can't edit the fakestore api, let's create a local copy of the data
products_data = fetch_initial_data(BASE_URL, PRODUCTS_FILE)


# Get all products
@products_bp.route("/", methods=["GET"])
def get_products():
    return jsonify(products_data), 200


# Get product with id
@products_bp.route("/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id):
    product = next((prod for prod in products_data if prod["id"] == product_id), None)
    if product:
        return jsonify(product), 200
    else:
        return jsonify({"error": "Product not found"}), 404


# Gat all categories
@products_bp.route("/categories", methods=["GET"])
def get_categories():
    categories = {product["category"] for product in products_data}
    return jsonify({"categories": list(categories)}), 200


# Get all products in a specific category
@products_bp.route("/category/<string:category_name>", methods=["GET"])
def get_products_in_category(category_name):
    category_products = [
        prod for prod in products_data if prod["category"] == category_name
    ]
    return jsonify(category_products), 200


# Post new Product
@products_bp.route("/", methods=["POST"])
def post_product():
    new_product = request.json
    new_product["id"] = (
        max([prod["id"] for prod in products_data]) + 1 if products_data else 1
    )
    products_data.append(new_product)

    # Save the new product to the JSON file
    save_product(new_product)

    return jsonify(new_product), 201


def save_product(product):
    with open(PRODUCTS_FILE, "r") as file:
        local_products = json.load(file)

    local_products.append(product)

    with open(PRODUCTS_FILE, "w") as file:
        json.dump(local_products, file)


# Delete a product using id
@products_bp.route("/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    global products_data
    product = next((prod for prod in products_data if prod["id"] == product_id), None)
    if product:
        products_data.remove(product)
        remove_product(product)  # Remove product from JSON file if it is there
        return jsonify({"message": "Product deleted successfully"}), 200
    else:
        return jsonify({"error": "Product not found"}), 404


def remove_product(product):
    with open(PRODUCTS_FILE, "r") as file:
        local_products = json.load(file)

    if product in local_products:
        local_products.remove(product)
        with open(PRODUCTS_FILE, "w") as file:
            json.dump(local_products, file)


# Edit product using id
@products_bp.route("/<int:product_id>", methods=["PUT"])
def edit_product(product_id):
    global products_data
    edit_product = request.json

    product = next((prod for prod in products_data if prod["id"] == product_id), None)

    if product:
        # Update the product with the new data
        product.update(edit_product)

        # Update the local JSON file if data is there
        if update_product(product):
            return jsonify({"message": "Product updated successfully"}), 200
        else:
            return jsonify({"error": "Failed to update JSON file"}), 500
    else:
        return jsonify({"error": "Product not found"}), 404


def update_product(updated_product):
    rtn = False
    with open(PRODUCTS_FILE, "r") as file:
        local_products = json.load(file)

    for index, product in enumerate(local_products):
        if product["id"] == updated_product["id"]:
            local_products[index] = updated_product
            break

    with open(PRODUCTS_FILE, "w") as file:
        json.dump(local_products, file)
        rtn = True
    return rtn

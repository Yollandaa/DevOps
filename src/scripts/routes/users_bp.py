"""
    @authors: Caleb Potts - E1005278, Yolanda Dastile - 
    Summary: Handles CRUD operations for users,
    fetching initial data from an API and a local file, 
    and performing create, read, update, and delete actions 
    on the carts, while saving changes to the local file. 
    Last modufied date: 02/08/2024
    Last modufied usesr: Caleb Potts
"""

from flask import Blueprint, request, jsonify
from scripts.data.data import DataHandler

user_bp = Blueprint("user_bp", __name__)


@user_bp.route("/", methods=["GET"])
def get_users():
    return jsonify(DataHandler.all_users_api_call), 200


@user_bp.route("/<string:name>", methods=["GET"])
def get_user_by_name(name):

    filtered_users = next(
        (
            user
            for user in users
            if user["name"]["firstname"].lower() == name.lower()
            or user["name"]["lastname"].lower() == name.lower()
        ),
        None,
    )
    if filtered_users:
        return jsonify(filtered_users), 200
    else:
        return jsonify({"message": "User not found"}), 404


@user_bp.route("/", methods=["POST"])
def add_user():
    try:
        user_data = request.get_json()

        if users:
            max_id = max(user["id"] for user in users if "id" in user)
        else:
            max_id = 0

        user_data["id"] = max_id + 1
        users.append(user_data)

        DataHandler.save_to_file(user_data, USERS_FILE)
        return jsonify({"message": "User added successfully"}), 201
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)}), 500


@user_bp.route("/<string:name>", methods=["PUT"])
def update_user(name):
    try:
        user_data = request.get_json()
        global users
        user_updated = False
        for user in users:
            if (
                user["name"]["firstname"].lower() == name.lower()
                or user["name"]["lastname"].lower() == name.lower()
            ):
                user.update(user_data)
                user_updated = True
                break

        if user_updated:
            DataHandler.save_to_file(users, USERS_FILE)
            return jsonify({"message": "User updated successfully"}), 200
        else:
            return jsonify({"message": "User not found"}), 404
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)}), 500


@user_bp.route("/<string:name>", methods=["DELETE"])
def delete_user(name):
    try:
        global users
        filtered_users = [
            user
            for user in users
            if user["name"]["firstname"].lower() != name.lower()
            and user["name"]["lastname"].lower() != name.lower()
        ]

        if len(filtered_users) == len(users):
            return jsonify({"message": "User not found"}), 404

        users = filtered_users
        DataHandler.save_to_file(users, USERS_FILE)
        return jsonify({"message": "User deleted successfully"}), 200
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)}), 500

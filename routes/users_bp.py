from flask import Blueprint, request, jsonify
import requests
import json
import os

user_bp = Blueprint("user_bp", __name__)
BASE_URL = "https://fakestoreapi.com/users"
USERS_FILE = "users.json"

if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, "w") as file:
        json.dump([], file)


def fetch_users():
    response = requests.get(BASE_URL, verify=False)
    api_users = response.json()

    with open(USERS_FILE, "r") as file:
        local_users = json.load(file)

    combined_users = local_users + [
        user for user in api_users if user not in local_users
    ]

    with open(USERS_FILE, "w") as file:
        json.dump(combined_users, file)

    return combined_users


def save_users(users):
    with open(USERS_FILE, "w") as file:
        json.dump(users, file)


@user_bp.route("/", methods=["GET"])
def get_users():
    users = fetch_users()
    return jsonify(users), 200


@user_bp.route("/<string:name>", methods=["GET"])
def get_user_by_name(name):
    users = fetch_users()
    filtered_users = [
        user
        for user in users
        if user["name"]["firstname"].lower() == name.lower()
        or user["name"]["lastname"].lower() == name.lower()
    ]
    if filtered_users:
        return jsonify(filtered_users), 200
    else:
        return jsonify({"message": "User not found"}), 404


@user_bp.route("/", methods=["POST"])
def add_user():
    try:
        user_data = request.get_json()
        users = fetch_users()
        users.append(user_data)
        save_users(users)
        return jsonify({"message": "User added successfully"}), 201
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)}), 500


@user_bp.route("/<string:name>", methods=["PUT"])
def update_user(name):
    try:
        user_data = request.get_json()
        users = fetch_users()
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
            save_users(users)
            return jsonify({"message": "User updated successfully"}), 200
        else:
            return jsonify({"message": "User not found"}), 404
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)}), 500


@user_bp.route("/<string:name>", methods=["DELETE"])
def delete_user(name):
    try:
        users = fetch_users()
        filtered_users = [
            user
            for user in users
            if user["name"]["firstname"].lower() != name.lower()
            and user["name"]["lastname"].lower() != name.lower()
        ]

        if len(filtered_users) == len(users):
            return jsonify({"message": "User not found"}), 404

        save_users(filtered_users)
        return jsonify({"message": "User deleted successfully"}), 200
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)}), 500

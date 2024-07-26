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

    users = local_users + api_users
    return users


def save_user(user):
    with open(USERS_FILE, "r") as file:
        users = json.load(file)

    users.append(user)

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
        save_user(user_data)
        return jsonify({"message": "User added successfully"}), 201
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)}), 500

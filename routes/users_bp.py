from flask import Blueprint, request, jsonify
import requests

user_bp = Blueprint("user_bp", __name__)
BASE_URL = "https://fakestoreapi.com/users"


@user_bp.route("/", methods=["GET"])
def get_users():
    response = requests.get(BASE_URL, verify=False)
    users = response.json()
    return jsonify(users), response.status_code

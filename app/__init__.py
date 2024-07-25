from flask import Flask
from routes.users_bp import user_bp


def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(user_bp, url_prefix="/api/users")

    return app

from flask import Flask
from routes.users_bp import user_bp
from routes.cart_bp import carts_bp


def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(user_bp, url_prefix="/api/users")
    app.register_blueprint(carts_bp, url_prefix="/api/carts")

    return app

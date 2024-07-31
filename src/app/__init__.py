from flask import Flask
from scripts.routes.users_bp import user_bp
from scripts.routes.cart_bp import carts_bp
from scripts.routes.products_bp import products_bp


def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(user_bp, url_prefix="/api/users")
    app.register_blueprint(carts_bp, url_prefix="/api/carts")
    app.register_blueprint(products_bp, url_prefix="/api/products")

    return app

import os
from scripts.data.data import DataHandler
from dotenv import load_dotenv
from app import create_app

app = create_app()

if __name__ == "__main__":
    load_dotenv()
    BASE_URL_USERS = os.getenv("DATA.RESOURCE.API.USERS.URL")
    BASE_URL_CARTS = os.getenv("DATA.RESOURCE.API.CARTS.URL")
    BASE_URL_PRODUCTS = os.getenv("DATA.RESOURCE.API.PRODUCTS.URL")

    # Fetch initial data
    DataHandler.fetch_initial_data(BASE_URL_USERS, data_type="users")
    DataHandler.fetch_initial_data(BASE_URL_CARTS, data_type="carts")
    DataHandler.fetch_initial_data(BASE_URL_PRODUCTS, data_type="products")

    app.run(host="0.0.0.0", port=5000, debug=True)

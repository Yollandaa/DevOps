"""
    @authors: Caleb Potts - E1005278, Yolanda Dastile - 
    Summary: Handles fetching initial data from an API 
    and local files, saving items to a file, and managing 
    product data by adding, removing, and updating it in 
    local JSON files. 
    Last modufied date: 02/08/2024
    Last modufied usesr: Caleb Potts
"""

import os
import requests
import json


class DataHandler:
    resources_dir = "./resources"

    @classmethod
    def fetch_initial_data(cls, url, filename):
        """
        Fetch initial data from an API and combine it with local data.

        Args:
            url (str): The URL to fetch data from.
            filename (str): The name of the file to save the combined data.

        Returns:
            List[Dict[str, Any]]: The combined list of API and local data.
        """
        response = requests.get(url, verify=False)
        api_data = response.json()
        local_data = []

        if not os.path.exists(cls.resources_dir):
            os.makedirs(cls.resources_dir)

        filepath = os.path.join(cls.resources_dir, filename)

        if not os.path.exists(filepath):
            with open(filepath, "w") as file:
                json.dump(local_data, file)
        else:
            with open(filepath, "r") as file:
                local_data = json.load(file)
        all_data = api_data + local_data
        return all_data

    @classmethod
    def save_to_file(cls, item, filename):
        """
        Save an item to a local file.

        Args:
            item (Dict[str, Any]): The item to save.
            filename (str): The name of the file to save the item in.
        """
        filepath = os.path.join(cls.resources_dir, filename)

        with open(filepath, "r") as file:
            local_data = json.load(file)

        local_data.append(item)

        with open(filepath, "w") as file:
            json.dump(local_data, file)

    # -------- Product Methods ----------
    @classmethod
    def remove_product_in_file(cls, product, filename):
        """
        Remove a product from a local file.

        Args:
            product (Dict[str, Any]): The product to remove.
            filename (str): The name of the file to remove the product from.
        """
        filepath = os.path.join(cls.resources_dir, filename)
        with open(filepath, "r") as file:
            local_products = json.load(file)

        if product in local_products:
            local_products.remove(product)
            with open(filepath, "w") as file:
                json.dump(local_products, file)

    @classmethod
    def update_product_in_file(cls, updated_product, filename):
        """
        Update a product in a local file.

        Args:
            updated_product (Dict[str, Any]): The updated product.
            filename (str): The name of the file to update the product in.

        Returns:
            bool: True if the product was updated, False otherwise.
        """
        filepath = os.path.join(cls.resources_dir, filename)
        rtn = False
        with open(filepath, "r") as file:
            local_products = json.load(file)

        for index, product in enumerate(local_products):
            if product["id"] == updated_product["id"]:
                local_products[index] = updated_product
                break

        with open(filepath, "w") as file:
            json.dump(local_products, file)
            rtn = True
        return rtn

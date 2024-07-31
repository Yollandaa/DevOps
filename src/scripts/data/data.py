import json
import os
import requests

resources_dir = "./resources"


def fetch_initial_data(url, filename):
    response = requests.get(url, verify=False)
    api_data = response.json()
    local_data = []

    if not os.path.exists(resources_dir):
        os.makedirs(resources_dir)

    filepath = os.path.join(resources_dir, filename)

    if not os.path.exists(filepath):
        with open(filepath, "w") as file:
            json.dump(local_data, file)
    else:
        with open(filepath, "r") as file:
            local_data = json.load(file)
    all_data = api_data + local_data
    return all_data


def save_to_file(item, filename):
    filepath = os.path.join(resources_dir, filename)

    with open(filepath, "r") as file:
        local_data = json.load(file)

    local_data.append(item)

    with open(filepath, "w") as file:
        json.dump(local_data, file)


# -------- Product Functions ----------
def remove_product_in_file(product, filename):
    filepath = os.path.join(resources_dir, filename)
    with open(filepath, "r") as file:
        local_products = json.load(file)

    if product in local_products:
        local_products.remove(product)
        with open(filepath, "w") as file:
            json.dump(local_products, file)


def update_product_in_file(updated_product, filename):
    filepath = os.path.join(resources_dir, filename)
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

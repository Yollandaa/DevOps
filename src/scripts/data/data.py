import json
import os
import requests


def fetch_initial_data(url, filename):
    response = requests.get(url, verify=False)
    api_data = response.json()
    local_data = []

    resources_dir = "./resources"
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
    resources_dir = "./resources"
    filepath = os.path.join(resources_dir, filename)

    with open(filepath, "r") as file:
        local_data = json.load(file)

    local_data.append(item)

    with open(filepath, "w") as file:
        json.dump(local_data, file)

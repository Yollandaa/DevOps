import json
import os
import requests


def fetch_initial_data(url, filename):
    response = requests.get(url, verify=False)
    api_data = response.json()
    local_data = []

    if not os.path.exists(filename):
        with open(filename, "w") as file:
            json.dump(local_data, file)
    else:
        with open(filename, "r") as file:
            local_data = json.load(file)
    all_data = api_data + local_data
    return all_data

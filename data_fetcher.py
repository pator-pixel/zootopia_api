import requests

API_KEY = "lXLWfFAmhsHw47RLE6EINEUA4PNN0wrhv8K9y6gO"

def fetch_data(animal_name):
    url = "https://api.api-ninjas.com/v1/animals"
    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}

    response = requests.get(url, headers=headers, params=params)

    print(response.status_code)
    print(response.json())

    if response.status_code == 200:
        return response.json()

    return []
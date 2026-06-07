import requests

API_KEY = "lXLWfFAmhsHw47RLE6EINEUA4PNN0wrhv8K9y6gO"

animal_name = "lion"

url = "https://api.api-ninjas.com/v1/animals"
headers = {
    "X-Api-Key": API_KEY
}
params = {
    "name": animal_name
}

response = requests.get(url, headers=headers, params=params)

print(response.status_code)
print(response.json())
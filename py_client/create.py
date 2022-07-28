import requests

headers = {'Authorization': 'Bearer 635812bd9ead41dcb46169a629e4f6e7918715e8'}
endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "This field is done",
    "price": 32.00
}

get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())


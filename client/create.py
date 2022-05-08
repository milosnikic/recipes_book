import requests 

# endpoint used for client
endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    "title": "MIXIN!!!",
    "price": 35
}

headers = {'Authorization': 'Bearer 4be49ba77255e4058ebef10cc2a945b08db3be21'}

get_response = requests.post(endpoint, json=data, headers=headers)

print(get_response.json())
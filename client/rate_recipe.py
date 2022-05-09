import requests

# endpoint used for client
endpoint = "http://127.0.0.1:8000/api/recipes/1/rate"

data = {
    'rating': 5,
    'recipe_id': 6,
}

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyMTA4MTAwLCJpYXQiOjE2NTIwODg3NjMsImp0aSI6ImYyNTU3ZjEwZDc4NzQxMjY4YmVmOTRkZjZkZTRhZGFhIiwidXNlcl9pZCI6Mn0.jDrGRU-UEmvJlJZz9VXkH3jdnS-u_mmQW3Y7Gk0Kevs"
headers = {'Authorization': f'Bearer {token}'}

get_response = requests.post(endpoint, json=data, headers=headers)

print(get_response.json())

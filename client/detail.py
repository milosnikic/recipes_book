import requests

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyMTAwOTkyLCJpYXQiOjE2NTIwODg3NjMsImp0aSI6IjUwYjE5YzM0ZGQ3NzQ3ZTA5NmFhNDdmNGZjNWRkZDUwIiwidXNlcl9pZCI6Mn0.rsCOhPbs4hlnWiL9V6Rz6nHsWvH4ohHs9b5CV0GSgnU"
headers = {
    "Authorization": f"Bearer {token}"
}
endpoint = "http://127.0.0.1:8000/api/recipes/1/"

get_response = requests.get(endpoint, headers=headers)

data = get_response.json()

print(data)
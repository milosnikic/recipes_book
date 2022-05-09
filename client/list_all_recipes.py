import requests

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyMTA2NzgyLCJpYXQiOjE2NTIwODg3NjMsImp0aSI6ImQ2NWU3ZGYxY2E2YzRiNjdiZjYzNjFkZWRkN2NlNTVmIiwidXNlcl9pZCI6Mn0.l1CpCstAR93nIa4XgnXmy5ZdSgp49wno3-PjcVDieM8"
headers = {
    "Authorization": f"Bearer {token}"
}
endpoint = "http://127.0.0.1:8000/api/recipes/"

get_response = requests.get(endpoint, headers=headers)

data = get_response.json()

print(data)
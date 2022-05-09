import requests 

# endpoint used for client
endpoint = "http://127.0.0.1:8000/api/recipes/"

data = {
    "name": "Test New recipe",
    "text": "this is new recipe"
}

headers = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyMTA2NzgyLCJpYXQiOjE2NTIwODg3NjMsImp0aSI6ImQ2NWU3ZGYxY2E2YzRiNjdiZjYzNjFkZWRkN2NlNTVmIiwidXNlcl9pZCI6Mn0.l1CpCstAR93nIa4XgnXmy5ZdSgp49wno3-PjcVDieM8'}

get_response = requests.post(endpoint, json=data, headers=headers)

print(get_response.json())
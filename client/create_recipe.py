import requests 

# endpoint used for client
endpoint = "http://127.0.0.1:8000/api/recipes/"

data = {
    "name": "Test New recipe",
    "text": "this is new recipe"
}

headers = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyMDkyMTgxLCJpYXQiOjE2NTIwODg3NjMsImp0aSI6ImY3YjgzZjE2MmMzNjRmZTI5ZTUxYWFjZTc2OWExOGRjIiwidXNlcl9pZCI6Mn0.3ll1Ittn76AKsJk5466ia_iXt-BFPMbtIX2qOFkWJqw'}

get_response = requests.post(endpoint, json=data, headers=headers)

print(get_response.json())
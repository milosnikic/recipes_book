import requests

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyMDkyMTgxLCJpYXQiOjE2NTIwODg3NjMsImp0aSI6ImY3YjgzZjE2MmMzNjRmZTI5ZTUxYWFjZTc2OWExOGRjIiwidXNlcl9pZCI6Mn0.3ll1Ittn76AKsJk5466ia_iXt-BFPMbtIX2qOFkWJqw"
headers = {
    "Authorization": f"Bearer {token}"
}
endpoint = "http://127.0.0.1:8000/api/recipes/"

get_response = requests.get(endpoint, headers=headers)

data = get_response.json()

print(data)
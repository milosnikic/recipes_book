import requests

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyMTIzMjc4LCJpYXQiOjE2NTIxMjI5NzgsImp0aSI6IjJhYTI4NWFmZTI5ODQ5ZDA4MmJhYThhMDRjM2E0NDExIiwidXNlcl9pZCI6NX0.aayMu20xzc3OScOO29vdeNy9bVvQZLAl7hrFX_-vIGU"
headers = {
    "Authorization": f"Bearer {token}"
}
endpoint = "http://127.0.0.1:8000/api/recipes/1/"

get_response = requests.get(endpoint, headers=headers)

data = get_response.json()

print(data)
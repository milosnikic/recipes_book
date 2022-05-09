import requests

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyMDk4NDcwLCJpYXQiOjE2NTIwODg3NjMsImp0aSI6IjY3M2MwNDA2MmEwMDQ3ZDRhZDkwNWFlY2Y4OGRjOTY4IiwidXNlcl9pZCI6Mn0.RBO8ZFMYpXvwOZ_tCHNUNSG18pajjx8ZM7RVGs4-ZAE"
headers = {
    "Authorization": f"Bearer {token}"
}
endpoint = "http://127.0.0.1:8000/api/recipes/"

get_response = requests.get(endpoint, headers=headers)

data = get_response.json()

print(data)
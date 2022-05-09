import requests

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyMTA1Njk2LCJpYXQiOjE2NTIwODg3NjMsImp0aSI6Ijc5N2MxZjExOTllMTQ3NGNhZWEwZWQ1ODUyZjZlZWY2IiwidXNlcl9pZCI6Mn0._7rGGdyYUiruKxvy05wKpIeEYwKJ_M_ZV1-npTXO1U0"
headers = {
    "Authorization": f"Bearer {token}"
}
endpoint = "http://127.0.0.1:8000/api/recipes/"

get_response = requests.get(endpoint, headers=headers)

data = get_response.json()

print(data)
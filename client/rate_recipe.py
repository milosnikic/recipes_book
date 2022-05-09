import requests

# endpoint used for client
endpoint = "http://127.0.0.1:8000/api/recipes/1/rate"

data = {
    'rating': 5,
    'user_id': 3,
    'recipe_id': 1
}

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyMTA1Njk2LCJpYXQiOjE2NTIwODg3NjMsImp0aSI6Ijc5N2MxZjExOTllMTQ3NGNhZWEwZWQ1ODUyZjZlZWY2IiwidXNlcl9pZCI6Mn0._7rGGdyYUiruKxvy05wKpIeEYwKJ_M_ZV1-npTXO1U0"
headers = {'Authorization': f'Bearer {token}'}

get_response = requests.post(endpoint, json=data, headers=headers)

print(get_response.json())

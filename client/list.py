import requests
from auth import get_auth_token

token = get_auth_token()
headers = {
    "Authorization": f"Bearer {token}"
}
endpoint = "http://127.0.0.1:8000/api/products/"

get_response = requests.get(endpoint, headers=headers)

data = get_response.json()
next_url = data['next']
results = data['results']
print(results)

if next_url is not None:
    get_response = requests.get(next_url, headers=headers)
    print(get_response['results'])


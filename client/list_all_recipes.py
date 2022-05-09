import requests
from auth import refresh, get_token

token = get_token()
if token:
    headers = {
        "Authorization": f"Bearer {token}"
    }
    endpoint = "http://127.0.0.1:8000/api/recipes/"
    get_response = requests.get(endpoint, headers=headers)
    if get_response.status_code != 200:
        token = refresh()
        get_response = requests.get(endpoint, headers=headers)
    data = get_response.json()
    print(data)
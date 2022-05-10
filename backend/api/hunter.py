import requests

API_KEY = "85189b90ac8bd74066dbe5b5a3f0ae9139de2734"

def verify_email(email):
    endpoint = f"https://api.hunter.io/v2/email-verifier?email={email}&api_key={API_KEY}"
    get_response = requests.get(endpoint)
    if get_response.status_code == 200:
        if get_response.json()['data']['status'] == "valid":
            return True
    return False
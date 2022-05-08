import requests
from getpass import getpass


def get_auth_token():
    auth_endpoint = "http://127.0.0.1:8000/api/auth/"
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    auth_response = requests.post(auth_endpoint, json={"username": username, "password": password})
    if auth_response.status_code == 200:
        return auth_response.json()['token']
    raise Exception("Bad username/password")
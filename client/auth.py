import json
import os
import requests
from getpass import getpass


FILENAME = 'credentials.json'


def read_credentials():
    if not os.path.exists(FILENAME):
        return (None, None, None, None)
    with open(FILENAME, 'r') as f:
        credentials = json.loads(f.read().rstrip())
        username = credentials['username']
        password = credentials['password']
        access = credentials['access']
        refresh = credentials['refresh']
        return (username, password, access, refresh)


def login():
    auth_endpoint = "http://127.0.0.1:8000/api/login/"

    (username, password, _, _) = read_credentials()

    if not username and not password:
        username = input("Enter your username: ")
        password = getpass("Enter your password: ")

    auth_response = requests.post(
        auth_endpoint, json={"username": username, "password": password})

    token = None

    if auth_response.status_code == 200:
        credentials = {}
        data = auth_response.json()
        with open(FILENAME, 'w') as f:
            credentials['username'] = username
            credentials['password'] = password
            credentials['access'] = data['access']
            credentials['refresh'] = data['refresh']
            token = data['access']
            f.writelines(json.dumps(credentials))

    return token


def logout():
    if os.path.exists(FILENAME):
        os.remove(FILENAME)


def refresh():
    auth_endpoint = "http://127.0.0.1:8000/api/login/refresh/"

    (username, password, _, refresh) = read_credentials()

    auth_response = requests.post(
        auth_endpoint, json={"username": username, "password": password, "refresh": refresh})

    token = None

    if auth_response.status_code == 200:
        data = auth_response.json()
        with open(FILENAME, 'r+') as f:
            credentials = json.loads(f.read().rstrip())
            credentials['access'] = data['access']
            token = data['access']
            f.seek(0)
            f.truncate()
            f.writelines(json.dumps(credentials))
            return token

    return login()


def get_token():
    if not os.path.exists(FILENAME):
        return login()
    (_, _, access, _) = read_credentials()
    return access



def call_api(endpoint, data=None):
    token = get_token()
    endpoint = f"http://127.0.0.1:8000/{endpoint}"
    if token:
        headers = {
            "Authorization": f"Bearer {token}"
        }
        get_response = requests.post(endpoint, json=data, headers=headers) if data is not None else requests.get(endpoint, headers=headers)
        if get_response.status_code not in [200, 201, 400]:
            token = refresh()
            get_response = requests.post(endpoint, json=data, headers=headers) if data is not None else requests.get(endpoint, headers=headers)
        return {'data': get_response.json(), 'status_code': get_response.status_code}
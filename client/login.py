import requests
from getpass import getpass

auth_endpoint = "http://127.0.0.1:8000/api/login/"
username = input("Enter your username: ")
password = getpass("Enter your password: ")

auth_response = requests.post(
auth_endpoint, json={"username": username, "password": password})

print(auth_response.json())
print(auth_response.status_code)

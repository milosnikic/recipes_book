import requests
from getpass import getpass

endpoint = "http://127.0.0.1:8000/api/register/"

first_name = input("Enter your firstname: ")
last_name = input("Enter your lastname: ")
email = input("Enter your email: ")
username = input("Enter your username: ")
password = getpass("Enter your password: ")
confirm_password = getpass("Enter your password again: ")

auth_response = requests.post(endpoint, json={'first_name': first_name, 'last_name': last_name, 'password': password,
                                              'confirm_password': confirm_password, 'email': email, 'username': username})
print(auth_response.json())
print(auth_response.status_code)

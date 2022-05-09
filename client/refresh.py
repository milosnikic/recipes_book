import requests
from getpass import getpass

auth_endpoint = "http://127.0.0.1:8000/api/login/refresh/"
username = input("Enter your username: ")
password = getpass("Enter your password: ")

refresh_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1MjE3NTE2MywiaWF0IjoxNjUyMDg4NzYzLCJqdGkiOiJlZTFiMGMxMDJiMjE0MjI5OWQ5ODc5NzUzYWRlYWEwYiIsInVzZXJfaWQiOjJ9.UiGXJUnmcOUr2nqk2PNmiZ_3Zpdg0-_M9Y9-pH8ghiY"

auth_response = requests.post(
    auth_endpoint, json={"username": username, "password": password, "refresh": refresh_token})

print(auth_response.json())
print(auth_response.status_code)

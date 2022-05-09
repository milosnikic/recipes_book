from auth import call_api


endpoint = "api/ingridients/"
response = call_api(endpoint, data={"name": "Lemon"})
print(response['data'])
print(response['status_code'])

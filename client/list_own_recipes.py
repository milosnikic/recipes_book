from auth import call_api


endpoint = "api/recipes/own"
response = call_api(endpoint)
print(response['data'])
print(response['status_code'])

from auth import call_api


endpoint = "api/recipes/6/"
response = call_api(endpoint)
print(response['data'])
print(response['status_code'])

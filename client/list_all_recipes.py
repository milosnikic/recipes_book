from auth import call_api


endpoint = "api/recipes/"
response = call_api(endpoint)
print(response)
from auth import call_api


endpoint = "api/recipes/1/rate/"
response = call_api(endpoint, data={'rating': 5,'recipe_id': 6,})
print(response)

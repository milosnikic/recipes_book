from auth import call_api


endpoint = "api/recipes/"
response = call_api(endpoint, data={"name": "Latest asdadsa","text": "this is new recipe"})
print(response)
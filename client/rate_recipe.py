from auth import call_api, save_result


endpoint = "api/recipes/rate/"
response = call_api(endpoint, data={'rating': 5,'recipe_id': 7,})
print(response['data'])
print(response['status_code'])
filename = f"{__file__.split('/')[-1].split('.')[0]}.json"
save_result(response['data'], filename)
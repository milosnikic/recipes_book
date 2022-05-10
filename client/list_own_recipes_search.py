from auth import call_api, save_result


endpoint = "api/recipes/own/?q=Milk"
response = call_api(endpoint)
print(response['data'])
print(response['status_code'])
filename = f"{__file__.split('/')[-1].split('.')[0]}.json"
save_result(response['data'], filename)

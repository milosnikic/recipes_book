from auth import call_api, save_result

endpoint = "api/recipes/"
response = call_api(endpoint, data={"name": "Asdasd","text": "this is new recipe", "ingridients": [ 'Milk','asdadsa', 'Ovo je novi ingridient', 'Water','Pet' ]})
print(response['data'])
print(response['status_code'])
filename = f"{__file__.split('/')[-1].split('.')[0]}.json"
save_result(response['data'], filename)
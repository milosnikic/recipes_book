import requests 

# endpoint used for client
endpoint = "http://127.0.0.1:8000/api/products/21312321/"

get_response = requests.get(endpoint)

print(get_response.json())
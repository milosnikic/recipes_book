import requests 

# endpoint used for client
endpoint = "http://127.0.0.1:8000/api/"

# getting response from specified endpoint
get_response = requests.post(endpoint, json={"title": "abc", "content": "Hello World", "price":1})

# status code
print(get_response.status_code)

# response as json
print(get_response.json())
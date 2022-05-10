import requests

API_KEY = "sk_f5525a85dd8bb117ad3c3744a53aba38"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
}


def get_additional_user_data(email):
    endpoint = f"https://person.clearbit.com/v2/combined/find?email={email}"
    get_response = requests.get(endpoint, headers=HEADERS)
    if get_response.status_code == 200:
        data = get_response.json()
        if data['person'] is not None:
            print(data['person']['location'], data['person']['github']['handle'], data['person']['linkedin']['handle'])
            return data['person']['location'], data['person']['github']['handle'], data['person']['linkedin']['handle']
    print((None, None, None))
    return (None, None, None)
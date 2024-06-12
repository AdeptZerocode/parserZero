import requests
import pprint

params = {

    'userId' : 1
}

response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)

print(response.status_code)

responce_json = response.json()

pprint.pprint(responce_json)
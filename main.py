import requests
import pprint

params = {

    'q' : 'html'
}

response = requests.get('https://api.github.com/search/repositories', params=params)

print(response.status_code)

responce_json = response.json()

pprint.pprint(responce_json)

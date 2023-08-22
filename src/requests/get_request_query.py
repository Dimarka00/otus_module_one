import json

import requests

query = {
    'lang': 'rus',
    'id': 3
}

r = requests.get('https://meowfacts.herokuapp.com/', params=query)
print(r.json())

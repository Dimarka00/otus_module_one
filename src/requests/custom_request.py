import requests

r = requests.request('GET', 'https://run.mocky.io/v3/3020a9de-4158-4d9e-8ed4-6fd37a10e0b8')
print(r.text)
print(r.headers)
import requests

from src.requests.test_data import DOG_FILE_PATH

headers = {'api_key': 'special-key'}

json = {
  "id": 5757,
  "category": {
    "id": 5757,
    "name": "garfield"
  },
  "name": "garfield",
  "photoUrls": [
    "https://thumbs.dreamstime.com/b/golden-retriever-dog-21668976.jpg"
  ],
  "tags": [
    {
      "id": 5757,
      "name": "garfield"
    }
  ],
  "status": "available"
}

r = requests.post(url='https://petstore.swagger.io/v2/pet',
                  headers=headers,
                  json=json)

print(r.json())
dog_id = r.json()['id']

with open(DOG_FILE_PATH, 'rb') as f:
    files = {'file': f,
             'type': 'image/jpeg'}

    file_headers = {'api_key': "special-key"}

    r_upload = requests.post(url='https://petstore.swagger.io/v2/pet/{}/uploadImage'.format(dog_id),
                             headers=headers,
                             files=files)
    print(r_upload.json())

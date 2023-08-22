import pytest
import requests
from jsonschema import validate


def test_get_all_breeds(base_url):
    r = requests.get(url=f'{base_url}/breeds/list/all')
    req_json = r.json()
    assert r.status_code == 200
    assert req_json['message']['spitz'] == ['japanese']


def test_get_random_image(base_url):
    schema = {
        'type': 'object',
        'properties': {
            'message': {'type': 'string'},
            'status': {'type': 'string'}
        },
        'required': ['message', 'status']
    }
    r = requests.get(url=f'{base_url}/breeds/image/random')
    req_json = r.json()
    assert r.status_code == 200
    validate(instance=req_json, schema=schema)


def test_get_random_image_max_value(base_url):
    r = requests.get(url=f'{base_url}/breeds/image/random/52').json()
    assert len(r.get('message')) <= 50


@pytest.mark.parametrize('number', [1, 2, 3, 4, 5, 6, 49, 50])
def test_get_random_multiple_images(base_url, number):
    r = requests.get(url=f'{base_url}/breeds/image/random/{number}')
    req_json = r.json()
    assert r.status_code == 200
    assert len(req_json.get('message')) == number


@pytest.mark.parametrize('breed', ['bulldog', 'corgi', 'dane', 'elkhound', 'finnish'])
def test_get_images_by_breed(base_url, breed):
    r = requests.get(url=f'{base_url}/breed/{breed}/images')
    req_json = r.json()
    assert r.status_code == 200
    for b in req_json.get('message'):
        assert breed in b

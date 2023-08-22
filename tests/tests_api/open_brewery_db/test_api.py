import pytest
import requests


def test_get_all_breweries(base_url):
    request = requests.get(url=f'{base_url}/v1/breweries',
                           params={'per_page': 1})
    assert request.status_code == 200


@pytest.mark.parametrize('city', ['San Diego', 'Weiz', 'Leoben', 'Schladming', 'Macroom', 'Alexandria'])
def test_find_breweries_by_city(base_url, city):
    request = requests.get(url=f'{base_url}/v1/breweries',
                           params={'by_city': city.replace(" ", "_").lower(),
                                   'per_page': 3})
    response_json = request.json()
    assert request.status_code == 200
    for brewery in response_json:
        assert brewery.get('city') == city


@pytest.mark.parametrize('id', ['9c5a66c8-cc13-416f-a5d9-0a769c87d318', '1988eb86-f0a2-4674-ba04-02454efa0d31',
                                '0faa0fb2-fffa-416d-9eab-46f67477c8ef'])
def test_find_breweries_by_ids(base_url, id):
    request = requests.get(url=f'{base_url}/v1/breweries',
                           params={'by_ids': id})
    response_json = request.json()
    assert request.status_code == 200
    for brewery in response_json:
        assert brewery.get('id') == id


@pytest.mark.parametrize('type', [
    'micro',
    'nano',
    'regional',
    'brewpub',
    'large',
    'planning',
    'bar',
    'contract',
    'proprietor',
    'closed',
])
def test_find_breweries_by_type(base_url, type):
    request = requests.get(url=f'{base_url}/v1/breweries',
                           params={'by_type': type,
                                   'per_page': 3})
    assert request.status_code == 200


@pytest.mark.parametrize('size', [1, 2, 5, 10, 15])
def test_get_random_breweries_with_size(base_url, size):
    request = requests.get(url=f'{base_url}/v1/breweries/random',
                           params={'size': size})
    response_json = request.json()
    assert request.status_code == 200
    assert len(response_json) == size

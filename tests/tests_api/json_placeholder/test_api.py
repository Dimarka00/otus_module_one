import json

import pytest
import requests
from jsonschema.validators import validate

schema = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "title": {"type": "string"},
        "body": {"type": "string"},
        "userId": {"type": "number"},
    }
}


def test_get_all_posts(base_url):
    request = requests.get(url=f'{base_url}/posts')
    assert request.status_code == 200


@pytest.mark.parametrize('id', [1, 2, 3, 4, 5, 10, 15, 20])
def test_get_post_by_id(base_url, id):
    request = requests.get(url=f'{base_url}/posts/{id}')
    response_json = request.json()
    assert request.status_code == 200
    assert response_json.get('id') == id
    validate(instance=response_json, schema=schema)


def test_create_post(base_url):
    user = requests.post(url=f'{base_url}/posts',
                         json={'title': 'test',
                               'body': 'body text',
                               'userId': 333}).json()
    validate(instance=user, schema=schema)


@pytest.mark.parametrize('routes', [
    '/posts/1/comments',
    '/albums/1/photos',
    '/users/1/albums',
    '/users/1/todos',
    '/users/1/posts',
])
def test_nested_data(base_url, routes):
    response = requests.get(url=f'{base_url}{routes}')
    assert response.status_code == 200


@pytest.mark.parametrize('start_routes, end_routes, expected_count', [
    ('/posts/', '/comments', 5),
    ('/albums/', '/photos', 50),
    ('/users/', '/albums', 10),
    ('/users/', '/todos', 20),
    ('/users/', '/posts', 10),
])
def test_users_nested(base_url, start_routes, end_routes, expected_count):
    for page_id in range(1, 11):
        request = requests.get(
            url=f'{base_url}{start_routes}{page_id}{end_routes}',
        ).json()
        assert len(request) == expected_count
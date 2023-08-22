import pytest
import requests


@pytest.mark.parametrize('param', [1, 2, 3, 4])
def test_one(param):
    assert param % 2 == 0


@pytest.mark.parametrize('param1, param2', [
    (1, 2),
    (3, 4),
    (5, 6),
    (7, 8)
])
def test_two(param1, param2):
    assert (param1 + param2) % 2 == 0


@pytest.mark.parametrize('param1', [1, 2, 3, 4, 5])
@pytest.mark.parametrize('param2', [6, 7, 8, 9, 0])
def test_three_nested(param1, param2):
    assert (param1 + param2) % 2 == 0


@pytest.mark.parametrize('userId', [-1, 0, 'a', 11, 9],
                         ids=['negative', 'zero', 'letter', 'out_of_range', 'valid_value'])
def test_api_empty_response_on_user_id(userId, base_url):
    assert requests.get(base_url + '/posts', params={'userId': userId}).json() == []

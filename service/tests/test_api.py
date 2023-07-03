import pytest
import requests


@pytest.fixture
def api_url():
    return "http://0.0.0.0:8000/houses"


def test_status_code():
    url = "http://0.0.0.0:8000/"
    response = requests.get(url)
    assert response.status_code == 200


def test_post_request(api_url):
    data = {
        "bedrooms": 4,
        "bathrooms": 2.0,
        "floors": 2.0,
        "zipcode": 22769,
        "price": 5000,
        "last_change": 2025,
    }
    response = requests.post(api_url, json=data)
    assert response.status_code == 200
    new_data = response.json()
    assert new_data["zipcode"] == 22769
    assert new_data["last_change"] == 2025


def test_response_data(api_url):
    response = requests.get(api_url)
    data = response.json()
    assert "zipcode" in data[0]
    assert "price" in data[0]


def test_data_integrity(api_url):
    response = requests.get(api_url)
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

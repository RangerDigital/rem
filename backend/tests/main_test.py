import pytest
import requests


def test_valid_usage(URL):
    # Post clipboard content.
    payload = {"clipboard": "Hello World"}

    response = requests.post(URL + "/clipboard", json=payload)
    json = response.json()

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert json["clipboard"] == "Hello World"

    # Retrieve clipboard content.
    response = requests.get(URL + "/clipboard/{}".format(json["code"]))
    json = response.json()

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert json["clipboard"] == "Hello World"


def test_invalid_get(URL):
    # Retrieve clipboard content with invalid Id.
    response = requests.get(URL + "/clipboard/test123")
    json = response.json()

    assert response.status_code == 400
    assert response.headers["Content-Type"] == "application/json"
    assert json["status"] == "error"
    assert json["msg"] == "Invalid Code!"


def test_invalid_post(URL):
    # Post clipboard content with invalid request.
    payload = {"msg": "Hello World"}

    response = requests.post(URL + "/clipboard", json=payload)
    json = response.json()

    assert response.status_code == 400
    assert response.headers["Content-Type"] == "application/json"
    assert json["status"] == "error"


def test_small_traffic(URL):
    # Test app with small batch traffic.
    for i in range(1000):
        payload = {"clipboard": "Count: {}".format(i)}

        response = requests.post(URL + "/clipboard", json=payload)
        json = response.json()

        assert response.status_code == 200
        assert json["clipboard"] == "Count: {}".format(i)

        response = requests.get(URL + "/clipboard/{}".format(json["code"]))
        json = response.json()

        assert response.status_code == 200
        assert json["clipboard"] == "Count: {}".format(i)

        assert response.elapsed.total_seconds() < 1


def test_status(URL):
    # Get system status.
    response = requests.get(URL + "/status")

    assert response.status_code == 200

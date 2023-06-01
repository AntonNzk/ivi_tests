import json
import requests

from services.schema import headers, test_data, body_expected_post
from services.urls import POST_CHARACTER
from test_data.auth import auth


def test_post_character():
    res = requests.post(url=POST_CHARACTER, data=test_data, auth=auth, headers=headers)
    print(res.json())
    assert res.status_code == 200
    assert res.json() == body_expected_post


def test_try_create_double_character(create_character):
    res = requests.post(url=POST_CHARACTER, data=test_data, auth=auth, headers=headers)
    assert res.status_code == 400
    assert res.json()["error"] == "Hawkeye124 is already exists"


def test_try_post_character_without_auth():
    res = requests.post(url=POST_CHARACTER, data=test_data, headers=headers)
    assert res.status_code == 401
    assert res.json()["error"] == 'You have to login with proper credentials'


def test_try_post_character_without_name():
    body_without_name = {"universe": "Marvel Universe8",
            "education": "High school", "weight": 104,
            "height": 1.90, "identity": "Publicly known"}
    headers = {'Content-type': 'application/json'}
    test_data = json.dumps(body_without_name)
    res = requests.post(url=POST_CHARACTER, data=test_data, headers=headers, auth=auth)
    assert res.status_code == 400
    assert res.json()["error"] == "name: ['Missing data for required field.']"

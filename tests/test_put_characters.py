import requests
from requests.auth import HTTPBasicAuth

from services.schema import test_data_put, headers
from services.urls import PUT_CHARACTER
from test_data.auth import auth


def test_put_character(create_character):
    res = requests.put(PUT_CHARACTER, auth=auth, data=test_data_put, headers=headers)
    assert res.status_code == 200
    assert res.json()["result"]["universe"] == "Hollywood Universe"
    assert res.json()["result"]["education"] == "High School (unfinished)"


def test_try_put_character_empty(create_character):
    res = requests.put(PUT_CHARACTER, auth=auth, data=None, headers=headers)
    assert res.status_code == 400
    assert res.json()["error"] == "Payload must be a valid json"

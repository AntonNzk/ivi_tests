import requests

from services.urls import GET_CHARACTERS, GET_CHARACTER_BY_NAME
from test_data.auth import auth


def test_get_characters():
    res = requests.get(url=GET_CHARACTERS, auth=auth)
    assert res.status_code == 200


def test_get_character_by_name(create_character):
    res = requests.get(url=GET_CHARACTER_BY_NAME, auth=auth)
    assert res.status_code == 200
    assert res.json()["result"]["name"] == "Hawkeye124"

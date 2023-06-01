import requests
from requests.auth import HTTPBasicAuth

from services.urls import DEL_CHARACTER, DEL_UNEXISTED_CHARACTER
from test_data.auth import auth


def test_del_character(create_character):
    res = requests.delete(url=DEL_CHARACTER, auth=auth)
    assert res.status_code == 200
    assert res.json()["result"] == "Hero Hawkeye124 is deleted"


def test_try_del_unexisted_character():
    res = requests.delete(url=DEL_UNEXISTED_CHARACTER, auth=auth)
    assert res.status_code == 400
    assert res.json()["error"] == "No such name"

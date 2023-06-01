import pytest
import requests
from services.schema import headers, test_data
from services.urls import POST_CHARACTER
from test_data.auth import auth


@pytest.fixture()
def create_character():
    res = requests.post(url=POST_CHARACTER, data=test_data, auth=auth, headers=headers)
    assert res.status_code == 200


@pytest.fixture(autouse=True)
def reset_characters():
    res = requests.post('http://rest.test.ivi.ru/v2/reset', auth=auth)
    assert res.status_code == 200


import pytest
from ml_api.app import flask_app

@pytest.fixture
def input_value():
    return 4

@pytest.fixture
def client():
    return flask_app.test_client()

@pytest.fixture
def input_dict():
    dictionary = dict()
    dictionary['number'] = 2
    return dictionary


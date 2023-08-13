import pytest

from fastapi.testclient import TestClient
from http import HTTPStatus
from colors_api.api import app


@pytest.fixture
def client():
    return TestClient(app)

def test_on_verify_integrity_should_return_status_200(client):
    response = client.get('/healthcheck')
    assert response.status_code == HTTPStatus.OK

def test_on_verify_integrity_return_should_be_of_type_json(client):
    response = client.get('/healthcheck')
    assert response.headers['Content-Type'] == 'application/json'

def test_on_verify_integrity_should_return_body_content(client):
    response = client.get('/healthcheck')
    assert response.json() == { "status": "ok" }

import json
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

def test_on_upload_image_should_return_status_200(client):
    response = client.post('/colors')
    assert response.status_code == HTTPStatus.OK

def test_on_upload_image_return_should_be_of_type_json(client):
    response = client.post('/colors')
    files = {
        "file": ("test_image.jpg", open("./tests/utils/sky-7622960_1280.jpg", "rb"), "image/jpg")
    }

    response = client.post('/colors', files=files, data={
        'data': json.dumps({"n_colors": 4})
    }, headers={})
    assert response.headers['Content-Type'] == 'application/json'

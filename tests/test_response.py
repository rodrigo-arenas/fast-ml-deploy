from fastapi.testclient import TestClient
from app import app


def test_success_prediction():
    endpoint = '/predict'
    body = {"data": [[4.8, 3, 1.4, 0.3], [2, 1, 3.2, 1.1]]}

    with TestClient(app) as client:
        response = client.post(endpoint, json=body)
        response_json = response.json()
        assert response.status_code == 200
        assert 'prediction' in response_json

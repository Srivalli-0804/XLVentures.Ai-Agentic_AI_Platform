from fastapi.testclient import TestClient

from backend.api.main import app


client = TestClient(app)


def test_workflows_endpoint_returns_list():
    response = client.get("/api/workflows")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

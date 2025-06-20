from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_auth_no_token():
    resp = client.get("/api/v1/cloud/aws/instances")
    assert resp.status_code == 401
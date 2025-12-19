from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200

def test_predict_any_payload():
    r = client.post("/predict", json={"url": "https://example.com"})
    assert r.status_code == 200

def test_predict_empty_body():
    r = client.post("/predict", json={})
    assert r.status_code == 400
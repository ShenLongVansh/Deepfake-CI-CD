from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200


def test_predict_valid_payload():
    r = client.post(
        "/predict",
        json={"image_url": "https://via.placeholder.com/256"}
    )
    # In CI, external HTTP may fail → allow 400
    assert r.status_code in [200, 400]


def test_predict_invalid_payload():
    r = client.post("/predict", json={"url": "https://example.com"})
    assert r.status_code == 422


def test_predict_empty_body():
    r = client.post("/predict", json={})
    assert r.status_code == 422

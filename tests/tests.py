from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_get():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}

def test_root_post():
    response = client.post("/")
    assert response.status_code == 200
    assert response.json() == {"message":"OK"}

def test_health_check():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"health":"OK"}

def test_ready_check():
    response = client.get("/readyz")
    assert response.status_code == 200
    assert response.json() == {"ready":"true"}

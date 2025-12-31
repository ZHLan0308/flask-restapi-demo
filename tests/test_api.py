import pytest
from app import create_app

@pytest.fixture()
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()

def test_health(client):
    r = client.get("/api/health")
    assert r.status_code == 200
    body = r.get_json()
    assert body["success"] is True
    assert body["data"]["status"] == "up"

def test_create_and_get_user(client):
    r = client.post("/api/users", json={"username": "alex"})
    assert r.status_code == 201
    user_id = r.get_json()["data"]["id"]

    r2 = client.get(f"/api/users/{user_id}")
    assert r2.status_code == 200
    assert r2.get_json()["data"]["username"] == "alex"
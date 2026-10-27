import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.repository import MenuRepository
from app.routers import menu


@pytest.fixture()
def client(monkeypatch):
    monkeypatch.setattr(menu, "repo", MenuRepository())
    with TestClient(app) as test_client:
        yield test_client


def test_crud(client):
    assert client.get("/health").status_code == 200
    assert len(client.get("/menu").json()) == 3
    assert len(client.get("/menu?category=Do%20uong").json()) == 1
    assert client.get("/menu/1").json()["name"] == "Cơm gà"
    assert client.get("/menu/99999").status_code == 404

    payload = {"code": "CT099", "name": "Bún bò", "category": "Mon chinh", "price": 42000, "quantity": 10, "available": True}
    response = client.post("/menu", json=payload)
    assert response.status_code == 201
    item_id = response.json()["id"]
    assert client.post("/menu", json=payload).status_code == 409
    assert client.post("/menu", json={**payload, "code": "CT100", "price": -2}).status_code == 422
    assert client.put(f"/menu/{item_id}", json={**payload, "price": 45000}).json()["price"] == 45000
    assert client.patch(f"/menu/{item_id}", json={"quantity": 5}).json()["quantity"] == 5
    assert client.delete(f"/menu/{item_id}").status_code == 204
    assert client.get(f"/menu/{item_id}").status_code == 404


def test_reject_null_and_invalid_filters(client):
    assert client.patch("/menu/1", json={"price": None}).status_code == 422
    assert client.get("/menu?limit=0").status_code == 422

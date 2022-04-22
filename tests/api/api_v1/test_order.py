"""Test /orders endpoint"""
from fastapi.testclient import TestClient


def test_create_buy_order(client: TestClient) -> None:
    """Test API POST order/buy endpoint"""
    data = {"instrument": "AAPL", "qty": 10, "side": "BUY"}
    response = client.post(
        "/api/v1/exchange/orders",
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["instrument"] == data["instrument"]
    assert content["quantity"] == data["qty"]


def test_create_sell_order(client: TestClient) -> None:
    """Test API POST order/sell endpoint"""
    data = {"instrument": "AAPL", "qty": 10, "side": "SELL"}
    response = client.post(
        "/api/v1/exchange/orders",
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["instrument"] == data["instrument"]
    assert content["quantity"] == data["qty"]

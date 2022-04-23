from fastapi.testclient import TestClient


def test_get_positions(client: TestClient) -> None:
    """Test API POST order/buy endpoint"""
    data = {"instrument": "AAPL", "qty": 10, "side": "BUY"}

    client.post(
        "/api/v1/exchange/orders",
        json=data,
    )

    response = client.get(
        "/api/v1/exchange/openPositions",
    )

    assert response.status_code == 200
    content = response.json()
    assert content[0]["held_shares"] == data["qty"]

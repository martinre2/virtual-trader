from fastapi.testclient import TestClient
from sqlalchemy.orm import Session


def test_get_ticker_price(client: TestClient, db: Session) -> None:
    """Test API GET ticker/price/ endpoint"""
    symbol = "MSFT"

    response = client.get(
        f"/api/v1/ticker/price/{symbol}",
    )

    assert response.status_code == 200
    content = response.json()
    assert len(content) > 0
    assert content[-1]["price"]
    assert content[-1]["time"]

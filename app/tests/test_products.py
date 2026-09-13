from fastapi.testclient import TestClient
from app.main import app

def test_list_products(client: TestClient):
    response = client.get("/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_product(client: TestClient):
    product_data = {
        "name": "Wireless Mouse",
        "price": 29.99,
        "description": "Ergonomic 2.4GHz wireless mouse"
    }
    response = client.post("/products", json=product_data)
    assert response.status_code == 201  
    data = response.json()
    assert data["name"] == product_data["name"]
    assert "id" in data  


def test_delete_product(client: TestClient):
    product_id = 1 
    response = client.delete(f"/products/{product_id}")
    assert response.status_code in [200, 204] 

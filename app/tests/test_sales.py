import pytest
from fastapi.testclient import TestClient
from decimal import Decimal
from app.main import app
from app.database import Base, engine 

import app.models.customers
import app.models.sales

Base.metadata.create_all(bind=engine)

client = TestClient(app)


def test_create_sale():
    customer_payload = {
        "first_name": "Transaction",
        "last_name": "Buyer",
        "email": "buyer@example.com",
        "phone": "555-0100",
        "address": "123 Main St"
    }
    customer_res = client.post("/customers", json=customer_payload)
    assert customer_res.status_code in [200, 201]
    customer_id = customer_res.json()["customer_id"]
    
    new_sale = {
        "customer_id": customer_id,
        "total_amount": "150.50"
    }
    
    response = client.post("/sales", json=new_sale)
    assert response.status_code in [200, 201]
    data = response.json()
    assert data["customer_id"] == customer_id
    assert "sale_id" in data
    assert "sale_date" in data


def test_get_sale_by_id():
    customer_payload = {"first_name": "Read", "last_name": "User", "email": "read@example.com", "phone": "555-0200", "address": "123 Main St"}
    customer_id = client.post("/customers", json=customer_payload).json()["customer_id"]
    
    sale_payload = {"customer_id": customer_id, "total_amount": "99.99"}
    sale_res = client.post("/sales", json=sale_payload)
    sale_id = sale_res.json()["sale_id"]
    
    response = client.get(f"/sales/{sale_id}")
    assert response.status_code == 200
    assert response.json()["sale_id"] == sale_id
    
    
def test_list_all_sales():
    response = client.get("/sales")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_sale():
    customer_payload = {"first_name": "Update", "last_name": "User", "email": "update@example.com", "phone": "555-0300", "address": "123 Main St"}
    customer_id = client.post("/customers", json=customer_payload).json()["customer_id"]
    
    sale_payload = {"customer_id": customer_id, "total_amount": "50.00"}
    sale_id = client.post("/sales", json=sale_payload).json()["sale_id"]
    
    updated_fields = {
        "total_amount": "75.25"  
    }
    response = client.put(f"/sales/{sale_id}", json=updated_fields)
    assert response.status_code == 200
    assert float(response.json()["total_amount"]) == 75.25


def test_delete_sale():
    customer_payload = {"first_name": "Delete", "last_name": "User", "email": "delete@example.com", "phone": "555-0400", "address": "123 Main St"}
    customer_id = client.post("/customers", json=customer_payload).json()["customer_id"]
    
    sale_payload = {"customer_id": customer_id, "total_amount": "10.00"}
    sale_id = client.post("/sales", json=sale_payload).json()["sale_id"]
    
    delete_response = client.delete(f"/sales/{sale_id}")
    assert delete_response.status_code in [200, 204]
    
    get_response = client.get(f"/sales/{sale_id}")
    assert get_response.status_code == 404

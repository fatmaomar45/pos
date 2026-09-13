import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine 

from app.models.customers import Customer  

Base.metadata.create_all(bind=engine)

client = TestClient(app)


def test_create_customer():
    new_customer = {
        "first_name": "Alice",
        "last_name": "Johnson",
        "email": "alice.johnson@example.com",
        "phone": "+1-555-0144",
        "address": "789 Maple St"
    }
    response = client.post("/customers", json=new_customer) 
    assert response.status_code in [200, 201]
    data = response.json()
    assert data["first_name"] == "Alice"
    assert "customer_id" in data


def test_get_customer_by_id():
    new_customer = {
        "first_name": "Bob",
        "last_name": "Smith",
        "email": "bob.smith@example.com",
        "phone": "+1-555-0155",
        "address": "456 Oak Ave"
    }
    create_res = client.post("/customers", json=new_customer)
    assert create_res.status_code in [200, 201]
    customer_id = create_res.json()["customer_id"]
    response = client.get(f"/customers/{customer_id}")
    assert response.status_code == 200
    assert response.json()["customer_id"] == customer_id
    assert response.json()["first_name"] == "Bob"


def test_list_all_customers():
    response = client.get("/customers")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_customer():
    new_customer = {
        "first_name": "Charlie",
        "last_name": "Brown",
        "email": "charlie@example.com",
        "phone": "+1-555-0166",
        "address": "123 Pine Rd"
    }
    create_res = client.post("/customers", json=new_customer)
    customer_id = create_res.json()["customer_id"]
    updated_fields = {
        "first_name": "Charles",       
        "points_balance": 150          
    }
    response = client.put(f"/customers/{customer_id}", json=updated_fields)
    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == "Charles"
    assert data["points_balance"] == 150


def test_delete_customer():
    mock_customer = {
        "first_name": "Temporary",
        "last_name": "User",
        "email": "temp.user@example.com",
        "phone": "000-000-0000",
        "address": "999 Ghost Lane"
    }
    create_response = client.post("/customers", json=mock_customer)
    assert create_response.status_code in [200, 201]
    customer_id = create_response.json()["customer_id"]
    delete_response = client.delete(f"/customers/{customer_id}")
    assert delete_response.status_code in [200, 204]
    get_response = client.get(f"/customers/{customer_id}")
    assert get_response.status_code == 404 

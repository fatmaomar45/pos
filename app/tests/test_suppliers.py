import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine 


import app.models.suppliers as supplier_models
Base.metadata.create_all(bind=engine)
client = TestClient(app)
shared_supplier_id = None

def test_create_supplier():
    global shared_supplier_id
    new_supplier = {
        "supplier_name": "Acme Industrial Logistics",
        "contact_person": "John Doe",
        "email": "contact@acme.com",
        "phone_number": "+1-555-0199",
        "address": "123 Main St",
        "password": "securepassword",
        "role": "supplier"
    }
    response = client.post("/suppliers", json=new_supplier)
    if response.status_code != 201 and response.status_code != 200:
        print("\nDEBUG ERROR PAYLOAD:", response.json())   
    assert response.status_code in [200, 201]   
    data = response.json()
    shared_supplier_id = data.get("supplier_id") or data.get("id")


def test_get_supplier_by_id():
    assert shared_supplier_id is not None
    response = client.get(f"/suppliers/{shared_supplier_id}")
    assert response.status_code == 200


def test_list_all_suppliers():
    response = client.get("/suppliers")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_supplier():
    assert shared_supplier_id is not None
    updated_data = {
        "supplier_name": "Acme Global Logistics",
        "contact_person": "Jane Doe",
        "email": "contact@acme.com",
        "phone_number": "+1-555-9999"
    }
    response = client.put(f"/suppliers/{shared_supplier_id}", json=updated_data)
    assert response.status_code == 200


def test_delete_supplier():
    mock_supplier = {
        "supplier_name": "Small Project Vendor",
        "contact_person": "Jane Smith",
        "email": "vendor@example.com",
        "phone_number": "123-456-7890",
        "address": "456 Vendor Lane",
        "password": "anotherpassword",
        "role": "supplier"
    }
    create_response = client.post("/suppliers", json=mock_supplier)
    assert create_response.status_code in [200, 201]  
    
    data = create_response.json()
    supplier_id = data.get("supplier_id") or data.get("id")
    
    delete_response = client.delete(f"/suppliers/{supplier_id}")
    assert delete_response.status_code in [200, 204] 
    
    get_response = client.get(f"/suppliers/{supplier_id}")
    assert get_response.status_code == 404 

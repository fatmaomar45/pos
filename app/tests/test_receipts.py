import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine 


import app.models.customers
import app.models.sales
import app.models.receipts  


Base.metadata.create_all(bind=engine)

client = TestClient(app)


def seed_sale_dependency():

    customer_payload = {
        "first_name": "Receipt", "last_name": "Customer", "email": "receipt.cust@example.com", "phone": "555-0800", "address": "123 Main St"
    }
    customer_res = client.post("/customers", json=customer_payload)
    customer_id = customer_res.json()["customer_id"]
    sale_payload = {"customer_id": customer_id, "total_amount": "250.75"}
    sale_res = client.post("/sales", json=sale_payload)
    return sale_res.json()["sale_id"]


def test_create_receipt():
    sale_id = seed_sale_dependency()
    new_receipt = {
        "sale_id": sale_id,
        "receipt_number": "REC-2026-0001"
    }
    
   
    response = client.post("/receipts", json=new_receipt)
    assert response.status_code in [200, 201]
    
    data = response.json()
    assert data["sale_id"] == sale_id
    assert data["receipt_number"] == "REC-2026-0001"
    assert "receipt_id" in data
    assert "issue_date" in data


def test_get_receipt_by_id():
    sale_id = seed_sale_dependency()
    receipt_payload = {"sale_id": sale_id, "receipt_number": "REC-2026-0002"}
    create_res = client.post("/receipts", json=receipt_payload)
    receipt_id = create_res.json()["receipt_id"]
    response = client.get(f"/receipts/{receipt_id}")
    assert response.status_code == 200
    assert response.json()["receipt_id"] == receipt_id


def test_list_all_receipts():
    response = client.get("/receipts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_receipt():
   
    sale_id = seed_sale_dependency()
    receipt_payload = {"sale_id": sale_id, "receipt_number": "REC-2026-0003"}
    receipt_id = client.post("/receipts", json=receipt_payload).json()["receipt_id"]

   
    updated_fields = {
        "receipt_number": "REC-2026-0003-REV"  
    }
    response = client.put(f"/receipts/{receipt_id}", json=updated_fields)
    assert response.status_code == 200
    assert response.json()["receipt_number"] == "REC-2026-0003-REV"


def test_delete_receipt():
    sale_id = seed_sale_dependency()
    receipt_payload = {"sale_id": sale_id, "receipt_number": "REC-2026-0004"}
    receipt_id = client.post("/receipts", json=receipt_payload).json()["receipt_id"]
    delete_response = client.delete(f"/receipts/{receipt_id}")
    assert delete_response.status_code in [200, 204]
    get_response = client.get(f"/receipts/{receipt_id}")
    assert get_response.status_code == 404

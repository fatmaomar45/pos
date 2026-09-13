import pytest
from fastapi.testclient import TestClient
from decimal import Decimal
from app.main import app
from app.database import Base, engine 

import app.models.customers
import app.models.sales
import app.models.products 
import app.models.sale_items 


Base.metadata.create_all(bind=engine)

client = TestClient(app)


def seed_dependencies():
    """Helper utility to generate valid IDs for customer, sale, and product relation loops"""
  
    cust_res = client.post("/customers", json={
        "first_name": "Item", "last_name": "Buyer", "email": "ibuyer@example.com", "phone": "555-9000", "address": "123 Street"
    })
    customer_id = cust_res.json()["customer_id"]
    
  
    sale_res = client.post("/sales", json={"customer_id": customer_id, "total_amount": "500.00"})
    sale_id = sale_res.json()["sale_id"]
    
   
    prod_res = client.post("/products", json={
        "product_name": "Premium Gadget", 
        "price": "45.00", 
        "stock": 100
    })
   
    product_id = prod_res.json().get("product_id") or prod_res.json().get("id") or 1
    
    return sale_id, product_id


def test_create_sale_item():
    
    sale_id, product_id = seed_dependencies()


    new_item = {
        "sale_id": sale_id,
        "product_id": product_id,
        "quantity": 2,
        "item_type": "retail",
        "unit_price": "45.00"
    }
    
    response = client.post("/sale-items", json=new_item) 
    assert response.status_code in [200, 201]
    
    data = response.json()
    assert data["sale_id"] == sale_id
    assert "sale_item_id" in data


def test_get_sale_item_by_id():
    sale_id, product_id = seed_dependencies()
    item_payload = {"sale_id": sale_id, "product_id": product_id, "quantity": 1, "item_type": "wholesale", "unit_price": "40.00"}
    
    create_res = client.post("/sale-items", json=item_payload)
    sale_item_id = create_res.json()["sale_item_id"]

    response = client.get(f"/sale-items/{sale_item_id}")
    assert response.status_code == 200
    assert response.json()["sale_item_id"] == sale_item_id


def test_list_all_sale_items():
    response = client.get("/sale-items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_sale_item():
    sale_id, product_id = seed_dependencies()
    item_payload = {"sale_id": sale_id, "product_id": product_id, "quantity": 5, "item_type": "retail", "unit_price": "20.00"}
    sale_item_id = client.post("/sale-items", json=item_payload).json()["sale_item_id"]

   
    updated_fields = {
        "quantity": 10,
        "unit_price": "18.50"
    }
    response = client.put(f"/sale-items/{sale_item_id}", json=updated_fields)
    assert response.status_code == 200
    
    data = response.json()
    assert data["quantity"] == 10
    assert float(data["unit_price"]) == 18.50


def test_delete_sale_item():
    sale_id, product_id = seed_dependencies()
    item_payload = {"sale_id": sale_id, "product_id": product_id, "quantity": 1, "item_type": "standard", "unit_price": "100.00"}
    sale_item_id = client.post("/sale-items", json=item_payload).json()["sale_item_id"]
    
    delete_response = client.delete(f"/sale-items/{sale_item_id}")
    assert delete_response.status_code in [200, 204]
    
    get_response = client.get(f"/sale-items/{sale_item_id}")
    assert get_response.status_code == 404

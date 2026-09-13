import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine 


import app.models.users as user_models  


Base.metadata.create_all(bind=engine)

client = TestClient(app)


def test_create_user():
    new_user = {
        "username": "johndoe_admin",
        "password": "supersecurepassword123",
        "role": "admin",
        "phone_number": "+1-555-9876",
        "is_active": True
    }
    
    response = client.post("/users", json=new_user)
    assert response.status_code in [200, 201]
    
    data = response.json()
    assert data["username"] == "johndoe_admin"
    assert "user_id" in data
    assert "created_at" in data


def test_get_user_by_id():
    new_user = {
        "username": "janedoe_manager",
        "password": "anothersecurepass!",
        "role": "manager"
    }
    create_res = client.post("/users", json=new_user)
    assert create_res.status_code in [200, 201]
    user_id = create_res.json()["user_id"]
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["user_id"] == user_id
    assert response.json()["username"] == "janedoe_manager"


def test_list_all_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_user():
  
    new_user = {
        "username": "cashier_test",
        "password": "cashierpassword",
        "role": "cashier"
    }
    create_res = client.post("/users", json=new_user)
    user_id = create_res.json()["user_id"]

  
    updated_fields = {
        "username": "cashier_updated",  
        "is_active": False              
    }
    response = client.put(f"/users/{user_id}", json=updated_fields)
    
    
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "cashier_updated"
    assert data["is_active"] is False
    assert data["role"] == "cashier"  


def test_delete_user():
    mock_user = {
        "username": "temp_user_wiped",
        "password": "passwordtobedeleted",
        "role": "guest"
    }
    create_response = client.post("/users", json=mock_user)
    assert create_response.status_code in [200, 201]
    user_id = create_response.json()["user_id"]
    delete_response = client.delete(f"/users/{user_id}")
    assert delete_response.status_code in [200, 204]
    get_response = client.get(f"/users/{user_id}")
    assert get_response.status_code == 404

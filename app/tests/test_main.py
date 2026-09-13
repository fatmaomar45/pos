from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    print("\n--- Response Headers ---")
    print(response.headers)
    print("------------------------")
    assert "content-type" in response.headers
    assert "application/json" in response.headers["content-type"]
    
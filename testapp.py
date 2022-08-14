from fastapi.testclient import TestClient
from main import app
# Test Client
client = TestClient(app)


def test_create_user():
    """
    test create user method
    """
    response = client.post("/user/create",json={
        'username':'test',
        'password':'test',
        'email':'test'
    })
    assert response.status_code == 201
    assert response.json() == {'msg': 'user created'}

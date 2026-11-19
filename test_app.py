from app import app

def test_home() :
    client = app.test_client()
    reponse = client.get('/')
    assert reponse.status_code == 200
    assert b"Hello, DevOps World! V1" in reponse.data
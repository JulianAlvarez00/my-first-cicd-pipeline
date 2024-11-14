from app import app

def test_hello_world():
    response = app.test_client().get('/api/hello')
    assert response.status_code == 200
    assert 'message' in response.get_json()
    assert '¡Hola Mundo!' in response.get_json()['message']

def test_index_page():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b'Mi Primera Pipeline DevOps' in response.data
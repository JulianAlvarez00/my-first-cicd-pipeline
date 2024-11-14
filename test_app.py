from app import app
import json

def test_hello_world():
    response = app.test_client().get('/api/hello')
    assert response.status_code == 200
    assert 'message' in response.get_json()
    assert '¡Hola Mundo!' in response.get_json()['message']

def test_index_page():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b'Mi Primera Pipeline DevOps' in response.data

def test_contact_form_missing_fields():
    response = app.test_client().post('/api/contact',
        json={
            'name': 'Test User'
            # Missing email and message
        }
    )
    assert response.status_code == 400
    assert b'Missing required fields' in response.data
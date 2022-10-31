import pytest
import json
from app import app

@pytest.mark.get_request
def test_book_resource():
    response = app.test_client().get('/books/test')

    data = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert data['id'] == 'test'

@pytest.mark.get_request
def test_non_exitent_book():
    response = app.test_client().get('/books/undefined')

    assert response.status_code == 404
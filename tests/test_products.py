import requests
from utilities.config import BASE_URL
def test_get_products():
    response = requests.get(f'{BASE_URL}/products')
    data = response.json()
    assert response.status_code == 200
    assert 'products' in data
    assert type(data['products']) == list

def test_single_product():
    response = requests.get(f'{BASE_URL}/products/1')
    data = response.json()
    assert response.status_code == 200
    assert 'id' in data
    assert data['id'] == 1
    assert 'title' in data

def test_add_product():
    response = requests.post(f'{BASE_URL}/products/add', json = {'title': 'Test Product','price': 100})
    data = response.json()
    assert response.status_code == 201
    assert 'id' in data
    assert data['title'] == 'Test Product'

def test_update_product():
    response = requests.put(f'{BASE_URL}/products/1',json = {'title': 'Updated Test Product'})
    data = response.json()
    assert response.status_code == 200
    assert data['id'] == 1
    assert data['title'] == 'Updated Test Product'

def test_delete_product():
    response = requests.delete(f'{BASE_URL}/products/1')
    data = response.json()
    assert response.status_code == 200
    assert 'id' in data
    assert data['isDeleted'] == True
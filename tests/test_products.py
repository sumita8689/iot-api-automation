import requests,pytest
from utilities.config import BASE_URL
from api.product_api import ProductAPI
from test_data.products import products

def test_get_products(product_api):
    response = product_api.get_products()
    data = response.json()
    assert response.status_code == 200
    assert 'products' in data
    assert type(data['products']) == list

def test_single_product(product_api):
    response = product_api.get_product(1)
    data = response.json()
    assert response.status_code == 200
    assert 'id' in data
    assert data['id'] == 1
    assert 'title' in data

def test_single_product_negative(product_api):
    response = product_api.get_product(99999)
    data = response.json()
    assert response.status_code == 404

@pytest.mark.parametrize('product',products)
def test_add_product(product_api,product):
    response = product_api.add_product(product)
    data = response.json()
    assert response.status_code == 201
    assert 'id' in data
    assert data['title'] == product['title']
    assert data['price'] == product['price']

def test_add_product_negative(product_api):
    response = product_api.add_product(-1)
    data = response.json()
    assert response.status_code == 400

def test_update_product(product_api):
    response = product_api.update_product(1,{'title': 'Updated Test Product'})
    data = response.json()
    assert response.status_code == 200
    assert data['id'] == 1
    assert data['title'] == 'Updated Test Product'

def test_delete_product(product_api):
    response = product_api.delete_product(1)
    data = response.json()
    assert response.status_code == 200
    assert 'id' in data
    assert data['isDeleted'] == True
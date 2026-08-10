import requests
def test_products():
    response = requests.get('https://dummyjson.com/products')
    print(response.json())
    assert response.status_code == 200
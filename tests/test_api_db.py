from database.db_utils import fetch_all
def test_product_api_matches_database(product_api):
    response = product_api.get_product(1)
    data = response.json()
    out= fetch_all('SELECT id, title, price FROM products WHERE id=1')
    assert data['id'] == out[0][0]
    assert data['title'] == out[0][1]
    assert data['price'] == out[0][2]
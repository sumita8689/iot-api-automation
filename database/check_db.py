from database.db_utils import fetch_all
data = fetch_all('SELECT * FROM products')
print(data)
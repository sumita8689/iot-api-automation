##contains all https requests to isolate from test file
import requests
from utilities.config import BASE_URL
from utilities.logger import get_logger
logger = get_logger(__name__)
class ProductAPI:
    def get_products(self):
        logger.info('getting products')
        return requests.get(f'{BASE_URL}/products')
    def get_product(self, product_id):
        logger.info('getting product')
        return requests.get(f'{BASE_URL}/products/{product_id}')
    def add_product(self, product):
        logger.info('adding product')
        return requests.post(f'{BASE_URL}/products/add', json=product)
    def update_product(self, product_id, product):
        logger.info('updating product')
        return requests.put(f'{BASE_URL}/products/{product_id}', json=product)
    def delete_product(self, product_id):
        logger.info('deleting product')
        return requests.delete(f'{BASE_URL}/products/{product_id}')
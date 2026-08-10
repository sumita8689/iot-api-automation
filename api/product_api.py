##contains all https requests to isolate from test file
import requests
from utilities.config import BASE_URL
from utilities.logger import get_logger
logger = get_logger(__name__)
class ProductAPI:
    def get_products(self):
        logger.info('GET products')
        response= requests.get(f'{BASE_URL}/products')
        logger.info(f'Response status: {response.status_code}')
        return response
    def get_product(self, product_id):
        logger.info(f'GET /products/{product_id}')
        response= requests.get(f'{BASE_URL}/products/{product_id}')
        logger.info(f'Response status: {response.status_code}')
        return response
    def add_product(self, product):
        logger.info('POST /products/add')
        response= requests.post(f'{BASE_URL}/products/add', json=product)
        logger.info(f'Response status: {response.status_code}')
        return response
    def update_product(self, product_id, product):
        logger.info(f'PUT /products/{product_id}')
        response= requests.put(f'{BASE_URL}/products/{product_id}', json=product)
        logger.info(f'Response status: {response.status_code}')
        return response
    def delete_product(self, product_id):
        logger.info(f'DELETE /products/{product_id}')
        response= requests.delete(f'{BASE_URL}/products/{product_id}')
        logger.info(f'Response status: {response.status_code}')
        return response
##contains setup and teardown features
import pytest
from api.product_api import ProductAPI

@pytest.fixture(scope='function')
def product_api():
    return ProductAPI()


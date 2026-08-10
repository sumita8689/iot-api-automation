from api.product_api import ProductAPI

def before_scenario(context, scenario):
    context.product_api = ProductAPI()

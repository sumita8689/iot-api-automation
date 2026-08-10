from behave import *

@given('I have a product ID {product_id:d}')
def step_impl_given(context,product_id):
    context.product_id=product_id

@when('I request a product')
def step_impl_when(context):
    context.response = context.product_api.get_product(context.product_id)

@then('The response status code should be 200')
def step_impl_then(context):
    assert context.response.status_code == 200
    assert context.response.json()['id'] == context.product_id

@given('I have product data "{title}" and price {price:d}')
def step_impl_given (context,title,price):
    context.prod_data = {"title": title,"price": price}

@when('I create a product')
def step_impl_when(context):
    context.response = context.product_api.add_product(context.prod_data)

@then('The response status code should be 201')
def step_impl_then_post(context):
    assert context.response.status_code == 201

@then('the product title should match')
def step_impl_then_title(context):
    assert context.response.json()['title'] == context.prod_data['title']

@given('I have the following product data')
def step_impl_given_table(context):
    context.products=[]
    for row in context.table.rows:
        dictout = {'title':row['title'],'price':int(row['price'])}
        context.products.append(dictout)

@when('I create the products')
def step_impl_when_table(context):
    context.responses= []
    for product in context.products:
        response = context.product_api.add_product(product)
        context.responses.append(response)

@then('The response status codes should be 201')
def step_impl_then_table(context):
    for resp in context.responses:
        assert resp.status_code == 201

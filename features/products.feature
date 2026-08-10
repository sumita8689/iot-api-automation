
Feature: Get and modify products
  Scenario Outline: Get a Product
    Given I have a product ID <product_id>
    When I request a product
    Then The response status code should be 200
    Examples:
      | product_id |
      | 1          |
      | 2          |
      | 3          |

  Scenario Outline: Create a Product
    Given I have product data "<title>" and price <price>
    When I create a product
    Then The response status code should be 201
    And the product title should match
    Examples:
      | title              | price |
      | Test BCC Product   | 200|
      | Test BCD Product   | 300|
      | Test BDE Product   | 500|

  Scenario: Create products using a data table
    Given I have the following product data
      | title              | price |
      | Data Table Test 1  | 250   |
      | Data Table Test 2  | 350   |
      | Data Table Test 3  | 450   |
    When I create the products
    Then The response status codes should be 201


'''
This script file is designed to call Product and sales module.
Generate the sales report
'''
# Import Product and Sales classes from Product_Sales module.
from Product_Sales import Product, Sales
import random

# Product data is passed as tuples to list
product_data = [("widgetA", 5.99, 100), ("widgetB", 10.99, 100),
            ("widgetC",14.99 , 200), ("widgetD", 16.99, 50),
            ("widgetE",14.99 , 125), ("widgetF", 11.99, 75),
            ("widgetG",4.99 , 200), ("widgetH", 17.99, 200),
            ("widgetI",1.99 , 300), ("widgetJ", 13.99, 50)]

def create_product_objects(data):
    # initializing list to hold Product objects.
    products = []
    #iterate through product data and populate Product object.
    for product in product_data:
        # un-pack from tuple product
        name, price, quant = product
        # create Product object and add to Products list
        products.append(Product(name, price, quant))
    return products

# Using random to generate sales only for even numbered products
# in product list.
def report_sales(product_list):
    sales = Sales()
    for index_pos, product in enumerate(product_list):
        if (index_pos % 2 == 0):
            random_quantity = random.randint(1, 40)
            sales.add_sale(product, random_quantity)
    return sales.generate_sales_report()

# Test classes function for testing
if __name__ == '__main__':
    batch1 = create_product_objects(product_data)
    print(report_sales(batch1))



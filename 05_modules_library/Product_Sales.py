"""
This module contains classes for tracking 
product and sales data. create a Product class with a constructor
method that takes name, price, and inventory as arguments. 
Add a __str__ method() that returns the name of 
the object with the price in parentheses.
"""
class Product:
    # Constructor method.
    def __init__(self, name, price, inventory):
        self.name = name
        self.price = price
        self.inventory = inventory

    # Product to string method.
    def __str__(self):
        return f"{self.name} (${self.price})"

'''
Create a sales class with a constructor method that takes no 
additional arguments and instantiates an object with an empty 
list named "sales_data"
'''  
class Sales:

    def __init__(self):
        self.sales_data = []

    # method to add sales data. This method is used to record sale
    # and to generate report.
    def add_sale(self, product, quantity):
        sale_dict = {
            "product" : product,
            "quantity" : quantity
        }
        self.sales_data.append(sale_dict)

    '''
    Generate sale report returns a full report on the object's 
    sales data including the total value of all sales and 
    information about the products and quantities sold.
    * Loop through the sales_data list to accumulate the 
        total value of all sales in the list
    * Initialize an empty string that will hold the final report.
    * Create a collection that holds the unique products from the sales_data list. 
        Loop through that collection and the associated sales
        data to determine to quantity of each product sold
    * As you loop through the set of unique products, use the price 
        and quantity to calculate the total revenue from each product.
        Round revenue to the nearest cent.
    * Report each product and quantity on a new line of the report.
      Use the "\n" newline character and the "+=" operator to add
      new lines to the report.
    '''
    def generate_sales_report(self):

        # Gnerate the total sales value
        total_sale_value = 0
        for sale_dict in self.sales_data:
            total_sale_value += sale_dict["product"].price * sale_dict["quantity"]
        # round the total sale value to two decimal cents.
        round(total_sale_value, 2)

        # Report string
        final_report = ""

        # Create unique product set using comprehension
        product_set = set( [sale["product"] for sale in self.sales_data] )

        # Iterate through product and sales_data to generate report
        for product in product_set:
            quants = [sale['quantity'] for sale in self.sales_data if sale['product'] == product]
            print(product)
            quantity_sold = sum(quants)

            #calculate revenue
            revenue = round(product.price * quantity_sold, 2)
            final_report += f"{product.name} : {quantity_sold} for a total revenue of : ${revenue}\n"
        final_report += f"Total sales is : ${total_sale_value}"

        return final_report
    
    # create a iterator on Sales object
    def __iter__(self):
        self.index = 0
        return self
    
    # create a next() method for Sales object
    def __next__(self):
        if self.index >= len(self.sales_data):
            raise StopIteration
        product_name = self.sales_data[self.index]['product'].name
        product_quantity = self.sales_data[self.index]['quantity']

        sale = f"You sold {product_quantity} of {product_name}"

        # increment to next element
        self.index += 1
        return sale

# Test methods encapsulated in class    
def test_classes():
    prod1 = Product("WidgetA", 10.99, 100)
    prod2 = Product("WidgetB", 19.99, 50)
    prod3 = Product("WidgetC", 7.99, 150)
    prod4 = Product("WidgetD", 3.99, 500)

    sales = Sales()
    sales.add_sale(prod1, 15)
    sales.add_sale(prod2, 30)
    sales.add_sale(prod3, 45)
    sales.add_sale(prod1, 30)
    sales.add_sale(prod4, 100)
    
    print (sales.generate_sales_report())

    print("*" * 50)
    # Use the iterator object on sales class
    sales_iter = iter(sales)
    for sale_string in sales_iter:
        print(sale_string)

if __name__ == '__main__':
    test_classes()



'''
Python is frequently used to process data. In this file,
we will build a function that parses and validates 
incoming JSON data. Then, you will write another 
function to store the parsed data in a file. 
You will need to implement some basic error handling and 
log errors to a file.
'''
import json
import logging

#log declaration
logging.basicConfig(filename="/Users/kader8/learning/python_basics/07_logging_error_handling/product_prasing.log", 
                    format="%(asctime)s %(levelname)s %(message)s", 
                    level=logging.INFO)

'''
function to read from product json file. Then apply following rules
    - Open the file object and load into python object
    - Iterate through the loaded list of dictionary object
    - log error if product attributes are missing and 
        continue to next iteration.
'''
def parse_products(file_path):
    try:
        # When we use with open method for file reading
        # it takes care of open() and file close() method.
        with  open(file_path) as f:
            #This object is a list of dictionaries.
            python_obj = json.load(f)

            logging.info("loaded obj : ", python_obj)
    except FileNotFoundError:
        logging.error("File no found at passed over path")
        return []
    except IOError as e:
        logging.error(e)
        return []

    # Initialize a empty product list.
    products = []
    '''
    Iterate through the python_obj list and check if product dictionary
    object has all product attributes.
    If not log an error and use "continue" keyword to move to next iteration.
    '''
    for product_dict in python_obj:
        if ( "name" not in product_dict ):
            logging.error("Product missing required field : name")
            continue
        if ( "price" not in product_dict):
            logging.error("Product missing required field : price")
            continue
        
        #add product_dict that has all mandatory attributes to list.
        products.append(product_dict)
        logging.info(f"Added product to inventory : {product_dict['name']}")

    return products

parse_products("/Users/kader8/learning/python_basics/07_logging_error_handling/prod_sample.json")


    

'''
Python provides built-in support for working with JSON data through 
the json module. The json module is included in the standard 
Python package. Python's json module has many utilities for 
encoding and decoding data in JSON format. The mapping between Python
and JSON objects is available 
in the following table.
jsonschema 
- You will have to use pip install jsonschema

Python  <-----> JSON
dict        - object
list, tuple - array
str         - string
int, float  - number
True        - true
False       - false
None        - null
'''
import json

'''
Example of reading a JSON formatted string into Python object
Use the json.loads() method.
'''
# json string that is in key value pair.
json_string = '{"first_name" : "John", "last_name" : " Styles", "city" : "seattle"}'
json_to_dict = json.loads(json_string)

print("json_to_dict type is : ", type(json_to_dict))

# retrieve key value pair using dict items method.
for key, value in json_to_dict.items():
    print(f" key is : {key} , value is : {value}")

'''
Example to load data from a json file and load into object.
Use json.load() method
Below is the content of the json file.
{
    "name" : "Dilawar shah",
    "age" : 48,
    "hobbies" : ["gardening", "gymming", "cricket", "movies"]
}
'''
# Accessing personal_details_json.json file and load to python object.
json_file = open("/Users/kader8/learning/python_basics/json_file_handling/personal_details_json.json", "r")

#Load into python object
python_dict = json.load(json_file)
json_file.close()

# print the type of json object.
print(type(python_dict))

# retrieve the elements.
for key, value in python_dict.items():
    print(f" key is : {key} , value is : {value}")
    print(type(key), " : ", type(value))

'''
Example to convert a json object to json formatted string.
Use the json.dumps(<python object>)
'''
# Define a dictionary with three key-value pairs.
x = {
  "dog": "Jack",
  "breed": "Golden Retriever",
  "city": "Albuquerque"
}

# Convert dictionary into a JSON string using json.dumps().
y = json.dumps(x, indent = 4)

# Print output.
print(y)

'''
Example to convert custom class object into json formatted string.
'''
class Book:
    # initialize constructor
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Create book object
book = Book("Thirukural", "Thiruvalluvar")

# create the json formatted string
book_json_formatted_str = json.dumps({"title" : book.title, "author" : book.author}, 
                                     indent = 4)
# print the json formatted string
print(book_json_formatted_str)

    


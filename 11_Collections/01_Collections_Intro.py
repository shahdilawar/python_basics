'''
Python’s collections module provides a rich set of specialized container
data types carefully designed to approach specific programming problems
in a Pythonic and efficient way. 
The module also provides wrapper classes that make it safer to create 
custom classes that behave similar to the built-in types dict, list, 
and str.
'''
from collections import namedtuple, defaultdict

'''
namedtuple is represented by its own class, created by using the 
namedtuple() factory function. 
    * The arguments are the name of the new class and a string 
      containing the names of the elements.
    * This helps in readability and access as class.attribute rather
      than accessing them via index.
'''
def named_tuple_demo(*args) -> namedtuple:
    Dog = namedtuple( "Dog", ["age", "breed", "name"] )
    dog_detail = args[0]
    #instantiating object's of named tuple
    jimmy = Dog( age = dog_detail[0], breed = dog_detail[1], name = dog_detail[2])

    print ( f" Jimmy name is : {jimmy.name}" )
    print( f" Jimmy age is : {jimmy.age}" )
    print ( f" Jimmy breed is : {jimmy.breed}" )

    #create a new namedtuple from existing
    roger = jimmy._replace(breed = "alsatian")
    print ( f" roger breed after update is : {roger}" )

    print( f" Type of Jimmy : {type(jimmy)} ")

    return jimmy

#convert a namedtuple to dictionary object
def convert_tuple_to_dict(tuple_obj : namedtuple) -> dict:
    if (tuple_obj == None):
        raise ValueError(" Tuple object can't be null ")   
    return tuple_obj._asdict()

#create a custom DivMod namedtuple object that provides both the
#qoutient and remainder in readable form
def custom_divmod(x : int, y : int) -> namedtuple:
    DivMod = namedtuple("DivMod", "qoutient remainder") 
    custom_divmod_obj = DivMod(*divmod(x, y))
    return custom_divmod_obj

'''
The Python defaultdict type is similar to a regular dictionary, but it
 automatically creates and assigns a default value to any missing keys 
 when they are accessed or modified. This feature makes defaultdict 
 useful for managing missing keys in dictionaries.
    * Grouping the items in a collection
    * Counting the items in a collection
    * Accumulating the values in a collection

Here are three use cases to take into account:

    * If your code is heavily base on dictionaries and you’re dealing 
        with missing keys all the time.
    * If your dictionary items need to be initialized with a constant 
        default value.
    * If your code relies on dictionaries for aggregating, accumulating,
      counting, or grouping values, and performance is a concern.
'''     
#demo of defaultdict
def default_dict_demo() -> defaultdict:
    #initialize defaultdict with list 
    # 1. Call list() to create a new empty list
    # 2. Insert the empty list into the dictionary using 
    # the missing key as key
    # Return a reference to that list
    ddict = defaultdict(list)
    ddict['key'].append(1)
    ddict['key'].append(2)
    ddict['key'].append(12)
    ddict['name'] = "Test"

    return ddict

#Grouping of values from Tuples.
def group_to_defaultdict():
    # The below data is retreived as Tuples from a dataset
    # fed into list

    dep = [('Sales', 'John Doe'), 
           ('Sales', 'Andy Doe'),
           ('Marketing', 'Nasser K'), 
           ('Marketing', 'Parveen B'),
           ('HR', 'Anosha B')
    ]

    dep_dd = defaultdict(list)

    #unpack tuples from dep list and save as key value pair to defaultdict
    #the department keys are initialized to the passed on empty list
    for department, employee in dep:
        dep_dd[department].append(employee)
    
    return dep_dd

#Demo for counting of items
def count_defaultdict_demo() -> defaultdict:
    dep = [('Sales', 'John Doe'), 
           ('Sales', 'Andy Doe'),
           ('Marketing', 'Nasser K'), 
           ('Marketing', 'Parveen B'),
           ('HR', 'Anosha B')]   
    #initialize defaultdict object with int as default value
    ddict = defaultdict(int)

    # unpack the tuples and storeonly department.
    # use _ convention to ignore the second element.
    for department, _ in dep:
       #increment no of employees in a department.
       ddict[department] += 1
       
    return ddict

def test_classes():
   #seek dog age
   age = int ( input("Please enter dog age : ") )
   #seek dog breed
   breed = input("Please enter dog breed : ")
   #seek dog name
   name = input("Please enter dog name : ")
   dog_details = age, breed, name
   # create the named tuple
   jimmy = named_tuple_demo(dog_details)

   #Pass the resultant namedtuple obj for conversion
   tuple_dict_obj = convert_tuple_to_dict(jimmy)
   for k , v in tuple_dict_obj.items():
       print(f"key is : {k} and value is : {v}")

   #Call the custom divmod function
   #seek number to be divided
   x = int ( input ("Enter number to be divided : ") )
   y = int ( input ("Enter divisor : ") )

   result_obj = custom_divmod(x, y)
   print(f"Custom divmod obj is : {result_obj}")

   #Test the defaultdict obj
   ddict = default_dict_demo()
   print(f"Default dict obj : {ddict}")

   #Test the grouping aspect of defaultdict
   grouped_ddict = group_to_defaultdict()
   print(f"Grouped default dict is : {grouped_ddict}")
   #add an employee to grouped_ddict and see if its gouped
   grouped_ddict['HR'].append("Aashik")
   #add a new dept and employee
   grouped_ddict['engg'].append('Dilawar S')
   grouped_ddict['engg'].append('Dhamu P')
   print(f"modified grouped ddict is : {grouped_ddict}")

   #test the counter function
   ddict_count = count_defaultdict_demo()
   print(f"Counted data dictionary is : {ddict_count}")

if __name__ == "__main__":
    test_classes()
 
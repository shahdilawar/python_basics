import modules_library_basics 
#from modules_library_basics import *

# Call the add_numbers utility method from module
total = modules_library_basics.add_numbers(1,2,3,4,8)
print(f"total is : {total}")
# Call the Person object from module
person = modules_library_basics.Person("Mary")
# Call the greeting utility from module and pass person name attribute
modules_library_basics.greeting(person.name)

# Test the math functions 



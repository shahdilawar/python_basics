'''
Errors detected during runtime are called exceptions. Instead of 
runtime errors unconditionally causing your program to crash, you can 
build logic that expects and handles certain exceptions.

Handling exceptions
The most basic form of exception handling uses something called 
try-except blocks. The try statement wraps around the code you want 
to run, but if that leads to errors, we have the except statement 
that wraps around code to handle the error thrown.
'''

#Below function provides a example of try - except block.
def add_numbers(x, y):
    try:
        return x + y
    except:
        return (f" Cannot add {type(x)} with {type(y)}")
# Test if it runs without error
print("Total value is : ", add_numbers(2, 3))
#separator block
print("-" * 50)
# Below should run with error
print(add_numbers(2, "string"))

'''
Planning for exceptions.
For professional software development, it can be very useful to collect 
data about the specific type of exceptions that are raised as your 
program runs. Then, you can use that data to inform changes to the 
code. Let's explore an example where you use your program to learn 
about the specific exceptions that can occur when a piece of code runs.  

* Below function uses the user input to performa division program
* Following errors can happen
    - User enters a string and type mismatch can result in error. We 
      need to use ValueError exception and plan
    - User can enter zero as divisor. We will use ZeroDivisor exception 
      and handle it.
    - If there is other unknown exceptions we can use Exception error
      and handle it. 
'''

#Function to demo the planned exception handling.
# use user input for dividend and divisor argument.
def divide_numbers():
    #Separator block
    print("-" * 50)
    print("Start of divide_numbers() function")

    try:
        #seek user input for dividend
        dividend = int( input("Enter the integer to be divided : ") )
        #seek user input for divisor
        divisor = int( input("Enter the integer to divide by : ") )
        #perform the divison operation and assign value to result variable.
        result =  (dividend / divisor)
    except ValueError:
        print("Please enter an integer : ")
    except ZeroDivisionError:
        print(" divisor cannot be 0 ")
    except Exception as e:
        print(e)
    else:
        return result
    

#call the function
print( divide_numbers() )

'''
Finally block :
When specified, the finally block runs whether or not an exception 
has been raised.

below demo function involves file handling exceptions and use of finally 
block.
    * FileNotFoundError - not finding the file by name
    * IOError - Not being about to read the file. 
    * An else block provides program instructions that run after the
      try block has run and after the exceptions have been cleared. 
    * The finally block checks to see if the file object 
        was successfully created, and then closes it if so. 
'''
def handle_file_exceptions():
    #Separator block
    print("-" * 50)
    print("start of handle_file_exceptions() function:")
    print("-" * 50)
    #seek user input for file_name
    file_name = input(" Please provide file_name : ")

    try:
        file_obj = open(file_name, "r")
        #perform operations on the file
    except FileNotFoundError:
        print("File cannot be found")
    except IOError:
        print("IO error occured during file read operation")
    else:
        print("file contents : ", file_obj.read())
    finally:
        if 'file_obj' in locals():
            file_obj.close()
            print(" File is closed ")

#Calling the function
handle_file_exceptions()

'''
Raising exceptions : 
You can also choose to raise an exception if a certain 
condition occurs. The keyword raise is used to raise an 
exception. 

The following code raises an exception when age
less than 13 is passed into to the create_profile 
function. 
syntax is raise <Exception> you can also use pre-defined
exception like ValueError
'''
# Function to create a dictionary of profiles.
# Raise error when age is < 13.
def create_profile():
    #Separator block
    print("-" * 50)
    print("start of create_profile() function:")
    print("-" * 50)

    #seek user input for name and age
    name  = input (" Please enter your name : ")
    age = int (input ("please enter your age in numericals : ") )

    try:
        #check if age is lesser than 13
        if (age < 13):
            raise ValueError("Account holders should be greater than 13")
        user_dict = {
            "name" : name,
            "age" : age
        }
        print(user_dict)
    except Exception as e:
        print(type(e))
        print(e)

# call create_profile() function
create_profile()

    






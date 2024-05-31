'''
Functions are blocks of code that perform a specific task. 
Functions give you the option to break your code into reusable, 
smaller pieces, and they make your code easier to read and maintain. 
If you need to perform a task multiple times, 
you can use functions to avoid having to repeat the same code.
'''
# Syntax
    # You define functions in Python using the def keyword followed 
    # by the function name, parenthesis, and a colon.
    # You indent the body of the function below the function definition. 

# Basic function
def my_function():
    # print welcome message
    print("Welcome to learning functions module")

# call the function
my_function()

# Function with positional arguments
def function_with_args(name, city):
    print(f"{name} lives in {city}")

# call the function by passing arguments
function_with_args("Dilawar", "Dublin")

# call the function with keyword arguments
function_with_args(city = "Dublin", name = "Dilawar")

# demo for return 
def add_numbers(x, y):
    sum = x + y
    return sum

result = add_numbers(10, 43)
print("sum of add_number function", result)

## Demo for default math functions. we don't need to use def function.
numbers = [2, 3, 5, 6, 7, 8, 9]

min_val = min(numbers)
max_val = max(numbers)
print(f" minimum of numbers list : {min_val} and maximum is : {max_val}")

#Using math pow function
# syntax is pow<base number, exponential value>
pow_of_max_val = pow(max_val, min_val)
print("pow is : ", pow_of_max_val)

# Demo for using arbitrary arguments using *args.
# You use *args to send a non-keyvalue variable length argument 
# tuple to a function.
def burger_condiments(*args):
    '''
    Receive a list of burger condiments and print the toppings.
    '''
    for topping in args:
        print(topping)

# Call burger_condiments function
burger_condiments("ketchup", "mayo", "pickle")

# **kwargs lets you provide argumnents as dictionary.
def user_info(**kwargs): 
	"""
    Take in keyword arguments as inputs and print 
    out the key-value pairs.
    """
	for key, value in kwargs.items(): 
		print(f"{key}: {value}") 

user_info(Name="Jane", Age=33, City="Paris", Language="French")

# Using custom functions as sort key in tuples.
def my_key(employee):
    """Return the tenure of a given employee tuple. 
    """
    return employee[1]

# Below code is to demo sort using custom key.
employees = [('Alicia', 7.2, 40), ('Jackie', 3.5, 33), ('Gary', 9.1, 55)]

# Passing the list the sort key defined by custom function my_key
employees.sort(key=my_key)
print(employees)

# Lambda functions. These are anonymous functions.
def my_function(n):
	"""
	Returns a lambda function that multiplies its 
    argument by n.
	"""
	return lambda a : a * n
#Set the parameter n is 4
quadruple = my_function(4)
#Call the anonymous function by passing argument a is 10
print(quadruple(10))
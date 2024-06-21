'''
Decorators can be thought of as functions which modify the functionality 
of another function. They help to make your code shorter and more 
"Pythonic".
    *   They work on the concept of functional programming, whereby which 
        functions can be passed as first class objects.
    *   Inner functions is the concept.
'''
import functools as ft

#Inner function sample
def parent(num : int) -> callable:

    def first_child():
        print("First child method is called")
    def second_child():
        print("Second child method is called")
    def not_in_list():
        print(f"Child number {num} not in list :-) ")
 

    if (num == 1):
        return first_child
    elif (num == 2):
        return second_child
    else:
        return not_in_list

#Demo of decorator
def new_decorator(func : callable) -> callable:
    ft.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Before function {func.__name__} being called")
        value = func(*args, **kwargs)
        print(f"After Function  {func.__name__} called")
        return value
    return wrapper

#Greet message utility
@new_decorator
def greet( message : str) -> str:
    if (message == ""):
        return "Hello World"
    else:
        return f"Hello {message}"

# Calling another function as an argument
def call_another_function(greet : callable) -> str:
    return greet


#wrapping the function within say_whoo module.
@new_decorator
def say_whoo_decorated(msg : str):
    print(f"Whoooooooo {msg}")


def test_classes():
    num = int( input("Enter the first or second child : ") )
    parent_func_result = parent(num)
    parent_func_result()

    # Calling another function.
    name = input("Enter your name : ")
    res = greet(name)
    print(res)

    # Calling the decorated function
    say_whoo_decorated(name)

if __name__ == "__main__":
    test_classes()

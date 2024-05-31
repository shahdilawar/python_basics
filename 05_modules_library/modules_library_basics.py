'''
This file will serve as a module where we will define functions that
can be called from other files/programs.
'''
import math 

# Define a utility function for greeting
def greeting(message = "world"):
    print(f" Hello : {message}")

# Define a utility function to add numbers
def add_numbers(*args):
    sum_total = 0
    # iterate through variable arguments args list.
    for n in args:
        sum_total += n
    return sum_total

# Define a class Person that has a attribute name.
class Person:
    def __init__(self, name):
        '''
        Constructor to initialize Person object with name attribute.
        '''
        self.name = name

# Calculate the surface area of sphere.
# return the value to 4 digits.
def calculate_surfac_area(radius):
    surface_area = 4 * math.pi * pow(radius, 2)
    return round(surface_area, 4)
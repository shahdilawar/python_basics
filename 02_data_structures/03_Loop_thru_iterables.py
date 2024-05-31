'''
Lists, sets, dictionaries, and tuples are all iterables, 
meaning that you can traverse over each element
they contain one at a time. This is useful for when you want 
to perform the same action, or set of actions, on each item
'''
# Loop through names and print in title case.
names = ["Alejandro", "Ana", "carlos", "john", "Jane", "Paulo"]
for name in names:
    print(f"Name in title case : {name.title()}")

# Using enumerate() method to get index and value.
# Enumerate method unpacks list with index and actual item in List.
for i, name in enumerate(names):
    index = i + 1
    print(f"Name in position {index} : {name}")

# Looping through Dictionaries
sales_wk1 = {
    "Monday" : 10,
    "Tuesday" : 14,
    "Wednesday" : 17,
    "Thursday" : 22,
    "Friday" : 45,
    "Saturday" : 22,
    "Sunday" : 31
}

# Iterate through loop using keys() method. 
# This will return all keys.
for key in sales_wk1.keys():
    print(key)

# Iterate through loop using values() method. 
# This will return all values.
for value in sales_wk1.values():
    print(value)

# Use items() method to access key and value.
# items method returns a tuple and we can unpack to key, value.
for key, value in sales_wk1.items():
    print(f" Key is : {key} and value is : {value}")

# Find the total sales of the week. 
# access values by key and calculate total sales.
total_sales = 0
for key in sales_wk1.keys():
    total_sales += sales_wk1.get(key)

print(f"Total sale is : {total_sales}")

'''
Write a program that uses a loop to iterate through a 
dictionary of sales data. The keys are dates (as a string) 
and the values are the total sales for each day. 
Print the average sales for the week and also print the 
date of the highest sale. 
'''
sales_dict = {
    '2022-03-01': 100,
    '2022-03-02': 200, '2022-03-03': 150, 
    '2022-03-04': 300, '2022-03-05': 250,
    '2022-03-06': 175, '2022-03-07': 225
    }

total_sales = 0
max_sale = 0
max_sale_date = "2022-03-01"
no_of_days = len(sales_dict.keys())
print(f"No of days : {no_of_days}")

for sale_date, sale_value in sales_dict.items():
    total_sales += sale_value
    if (sale_value > max_sale):
        max_sale_date = sale_date
        max_sale = sale_value

average_sale = total_sales / no_of_days
print(f"Average sale is : {average_sale}")
print(f"Maximum sale happened on : {max_sale_date}")

# Demo of nested loops and using sum() and round() functiom
# Calculate the average of grades and add them as new key, value pair
# back to students dictionary.
students = [
    {'name': 'Alice', 'age': 20, 'grades': [90, 85, 95]},
    {'name': 'Bob', 'age': 21, 'grades': [80, 75, 70]},
    {'name': 'Charlie', 'age': 19, 'grades': [95, 90, 92]},
]
# Iterate through students dictionary and access grades.
for student in students:
    grades = student['grades']
    # Use sum(Iterable) function to get total value.
    avg_grades = sum(grades) / len(grades)
    print(f"Average grades is : {avg_grades}")
    student["average_grade"] = round(avg_grades, 2)
print(students)

'''
List and Dictionary Comprehensions. Create a new List / Disctionary 
from other Iterables. 
Use case - mathematical functions, adding tax or discount.
'''
# List Comprehension demo
# Syntax [<each element n> <for n in original iterable>
#                                       <test condition if needed>]
numbers = [1, 2, 3, 4 , 4, 6, 7, 8]
doubled_numbers = [ n * 2 for n in numbers]
print("Doubled numbers list is : ", doubled_numbers)

# create a list containing numbers only post doubling is >= 20
numbers = [4, 15, 12, 16, 2, 6, 10, 2, 7, 11]
doubled_highs = [ n * 2 for n in numbers if n * 2 >= 20]
print("Doubled highs : ", doubled_highs)

'''
A popular way to use dictionary comprehensions is to create a
new dictionary from two lists of data. This example uses 
a zip() function to create a tuple from two lists. 
The key, value syntax unpacks the tuples by that function. 
'''
names = ["Alice", "Mary", "Raja", "Dev"]
ages = [22, 45, 52, 32]

name_age = { key : value for key, value in zip(names, ages)}
print(" created Name age dict ", name_age)
"""
Mary and Martha went on a fishing trip and caught several fish. 
The data below contains a record of their day. 
The weight of the fish is in ounces, and the length of the 
fish is in inches.

Write a program to perform the following tasks:
* Add an item to each dictionary that indicates who caught the fish.
* Merge the two lists together into a single list
* Display the average weight of the fish from both catches.
* Display the average length of the fish from both catches.
* Print the angler, id, and weight of any fish caught that 
* weighed 24 ounces or more.
"""

marys_catch = [
{"id": 1, "length": 17.0, "weight": 18.2},
{"id": 2, "length": 22.0, "weight": 27.1},
{"id": 3, "length": 20.25, "weight": 21.9},
{"id": 4, "length": 12.5, "weight": 11.5},
{"id": 5, "length": 25.75, "weight": 33.4},
]

marthas_catch = [
{"id": 1, "length": 24.75, "weight": 29.3},
{"id": 2, "length": 9.25, "weight": 6.0},
{"id": 3, "length": 12.0, "weight": 16.8},
{"id": 4, "length": 22.5, "weight": 28.6},
{"id": 5, "length": 23.0, "weight": 29.7},
]

# Add an item to each dictionary that indicates who caught the fish.
for catch in marys_catch:
    catch['angler_name'] = "Mary"
print("Mary's list : ", marys_catch)

for catch in marthas_catch:
    catch['angler_name'] = "Martha"
print("Martha's list : ", marthas_catch)

# Merge the two lists together into a single list
catches_of_the_day = marys_catch + marthas_catch
print("Appended List : ", catches_of_the_day)

# Display the average weight and length of the fish from both catches.
total_weight = 0
total_length = 0
catch_length = len(catches_of_the_day)
for catch_data in catches_of_the_day:
    total_weight += catch_data["weight"]
    total_length += catch_data["length"]

avg_weight = round(total_weight / catch_length, 2)
avg_length = round(total_length / catch_length, 2)
print(f"Average weight is : {avg_weight} and average length is : {avg_length}")

# Print the angler, id, and weight of any fish caught that 
# weighed 24 ounces or more. Use List comprehension
larger_fishes = [fish for fish in catches_of_the_day
                             if fish['weight'] >= 24]

for catch_data in larger_fishes:
    print(" Angler name is : ", catch_data['angler_name'])
    print(" ID is : ", catch_data['id'])
    print(" Fish weight is : ", catch_data['weight'])


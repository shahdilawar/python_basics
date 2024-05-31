#### Data types - List, Set, Tuples and Dictionaries ---- #######
### List 
    # - Ordered, Mutable, Duplicates allowed and indexed.
    # - Syntax is square brackets

new_list = ["Dilsath", "Anosha", "Aashik", "Nadheer", "Basheer"]

#positive index
print(new_list[2])

#negative index
print(new_list[-1])

## Use the len() function to find the positive index 

## associated with the last number on this list.
num_list = [68, 64, 88, 54, 17, 28, 35, 76, 68, 8, 27, 
    50, 53, 39, 5, 43, 58, 33, 38, 30, 76, 38, 22, 60,
    79, 23, 39, 5, 22, 66, 37, 49, 5, 66, 32, 89, 46, 
    82, 80, 84, 14, 22, 46, 100, 72, 22, 51, 83, 47]

length = len(num_list)
# Either use str() method for string concatenation
print("Length of list : " + str(length))
# or use <f""">
print(f"Length of list using formatter f : {length}")
print("Number at last index: " + str(num_list[length-1]))

#Remove an element from List using pop method.
    # Pop without index removes the last element.
    # Pop with index removes the element at that index.
pop_list = [1, 2, 3, 4, 5, 6]
print(pop_list.pop())

#after pop remove
print(pop_list)
#Add element
pop_list.append(6)
print(pop_list)

#add another list  to list.
addToList = [7,8,9,10]
pop_list.extend(addToList)
print(pop_list)

#insert a element in between the list, use inset<index, value>
pop_list.insert(3,33)
print("post index addition lis is : ", pop_list)

# sort alphanumeric string
my_list = ["car", "boat", "truck", "1", "Car"]
my_list.sort()
print("Mixed case alphanumeric sort:", my_list)

# sort with optional reverse argument
my_list.sort(reverse=True)
print("Sort with optional reverse argument:", my_list)

# sort using reverse method
groceries = ["apples", "berries", "cabbage"]
groceries.reverse()
print("groceries after reverse()", groceries)

#Challenge questiom
    # Write a short program that performs the following tasks. 
        # Asks the user for an item to add to a grocery list.
        # Asks the user if they have more items to add to the list.
        # Ends the program when the user has no more items to add.
        # Prints the grocery list sorted in alphabetical order.

#initialize empty grocery list.
grocery_list = []
# Asking users to enter items via input. Use a while loop and 
# conditional statement to break.
askForGrocery = True
while(askForGrocery):
    item = input("Enter grocery item to be added : ")
    grocery_list.append(item)

    # ask user if more items need to be added.
    moreItemsNeeded = input("Do you need more items to be added y/n : ")

    # If user keys in n, then break the loop.
    if(moreItemsNeeded == "n"):
        break

#print the list sorted in alphabetical order
grocery_list.sort()
print("Grocery list items are : ", grocery_list)


### Set
    # - Un-Ordered, Mutable, Duplicates not allowed
    # - Syntax is Curly brackets
    # - Based on mathematical Set theory.
'''
    Main benefits of working with sets in Python is using the 
    built-in mathematical set operations to understand 
    the relationship and overlap between collections of data.
'''

#Initializing a set with Curly brackets
setInit = {"ant", "monkey", "dog"}
print("set is : ", setInit)

# creating a Set from constructor and removing duplicates 
# from a collection demo
listOfDuplicates = [1,2,3,4,1,2,3,4]
print("List containing Duplicates : ", listOfDuplicates)

# Removing duplicates
setFromList = set(listOfDuplicates)
print("Set after removing duplicates", setFromList)

# Check if animals set is considered superset of wildAnimals set
animalsSet = {"dog", "cat", "leopard", "bear", "tiger", "snake", "cow"}
wildAnimalsSet = {"leopard", "bear", "tiger", "snake"}
print("is animalsSet super set of wildAnimalsSet : ", animalsSet.issuperset(wildAnimalsSet))

# check if wildAnimals is considered subset of animalsSet
print("is wildAnimalsSet sub set of animalsSet : ", wildAnimalsSet.issubset(wildAnimalsSet))

# Demo for disjointed. isDisjointed checks if there are no common 
# elements between two sets.
setA = {1, 2, 3, 4}
setB = {7, 8, 9, 10}
print("Set A and Set B are disjointed : ", setA.isdisjoint(setB))

# Demo for intersection. intersection checks if there are common 
# elements between two sets.
setA1 = {1, 2, 3, 4}
setB1 = {7, 4, 9, 10, 2}
print("Set A1 and Set B1 have intersection : ", setA1.intersection(setB1))

# create a new set containing intersection of the elements
intersectedSet = setA1.intersection(setB1)
print("intersectedSet is : ", setA1.intersection(setB1))

#update existing set with common elements.
grocerySet1 = {"egg", "milk", "bread", "butter"}
grocerySet2 = {"flour", "milk", "bread", "egg", "rice"}

grocerySet1.intersection_update(grocerySet2)
print("grocerySet1 after intersection update : ", grocerySet1)

# check for Symmetric differene. This is opposite of intersection. 
# This retreives elemets that are not common.
animalsSetA = {"dog", "cat", "leopard", "bear", "tiger", "snake", "cow"}
animalsSetB = {"leopard", "bear", "tiger", "snake", "goat", "buffalo"}

symmetricAnimals = animalsSetA.symmetric_difference(animalsSetB)
print("Symmetric animals set : " , symmetricAnimals)

# update existing animalsSetA with elements that are not common using 
# symmetric_difference_update method.
animalsSetA.symmetric_difference_update(animalsSetB)
print("animalsSetA post symmetric update : ", animalsSetA)

# Union method
setA = {"Python", "JavaScript", "PHP"}
setB = {"Python", "JavaScript", "Java", "C++"}
all_elems= setB.union(setA)
print(all_elems)

# Removing elements from Set using discard and remove method
insects = {"ant", "bee", "cricket", "dragonfly"}

# discard()
insects.discard("ant")
print ('After discard("ant"), the insects sets is:', insects)

# remove()
# remove raises an error if the specified element is not in the set
insects.remove("bee")  
print("After remove(), the insects set includes:", insects)

# pop removes a random element and returns that value
removed_item = insects.pop()
print ("The removed element is", removed_item)
print ("The remaining set includes", insects)

'''
write a program that selects a random winner from the collection of 
email address that appear on both starter lists. 
The collection from which the winner is 
drawn should not include any duplicate entries.
'''
email_list = ['jane@amazondomains.com', 'kwaku@example.com',
                'john@example.py', 'alejandro@example.net', 
                'mary@example.net', 'shirley@example.tv', 
                'jorge@example.py', 'ana@example.org', 
                'alejandro@example.tv', 'paulo@example.com',
                'nikki@example.tv', 'shirley@amazondomains.com',
                'kwaku@example.com', 'john@example.com', 
                'diego@example.tv', 'wang@amazondomains.com',
                'ana@example.org', 'richard@example.io',
                'carlos@amazondomains.com', 'ana@example.org',
                'jorge@example.tv', 'diego@example.tv', 
                'jane@example.net', 'shirley@example.com', 'jane@example.net']
purchases_list = ['shirley@amazondomains.com', 'kwaku@example.net',
                'mary@example.com', 'richard@example.io',
                'diego@example.py', 'ana@example.net', 
                'kwaku@example.py', 'carlos@example.net',
                'carlos@example.tv', 'richard@example.tv',
                'jane@example.com', 'paulo@example.tv',
                'li@example.com', 'jorge@example.io',
                'nikki@example.io', 'mary@example.com',
                'carlos@example.tv', 'diego@example.org',
                'saanvi@example.tv', 'paulo@example.com',
                'paulo@example.tv', 'diego@example.org', 
                'kwaku@example.com', 'jorge@example.tv', 'nikki@example.net']


# Find the common email in both sets by using intersection method and create a new set.
# Then use the pop() method which will get a random member.

winner_set = set(email_list).intersection(set(purchases_list))
print("Winner is : ", winner_set.pop())


### Dictionary
    # - Key - Value pairs, Ordered, Mutable, Duplicates allowed and indexed
    # - Syntax - Key, value pairs are delimited by colon. Each key-value pair separated by comma and
        # whole collection surrounded by curly brackets.
inventory = {
    "apples" : 9,
    "oranges" : 5,
    "bananas" : 8,
    "kiwi" : 4
}
print("inventory dictionary is : ", inventory)

# Items can be accessed by their keys as below.
num_apples = inventory["apples"]
num_bananas = inventory["bananas"]
print(f"There are {num_apples} apples and {num_bananas} bananas")

#adding an element to the inventory
inventory["elderberries"] = 22
print("Post adding element inventory dictionary is : ", inventory)

#accessing items through get method.
print(inventory.get("apples"))

#Adding items through update method.
inventory.update({"gooseberries" : 20})
print("inventory post adding gooesberries : " , inventory)

#Copying dictionary to a new one using fromKeys() method.
# It takes two values. name of dictionary and initial value.
copiedInventory = inventory.fromkeys(inventory.keys(), 0)
print("Copied inventory is : " , copiedInventory)

# Nested dictionaries
    # Dictionary containing employee details nested.

employeeData = {
    "001" : {
        "Name" : "Parveen Bobby", 
        "Age"  : 41,
        "Position" : "Teaching Assistant", 
        "Dept" : "Teaching", 
        "address" : {
            "Street" : "3050 Finnian way, apt 440", 
            "City" : "Dublin", 
            "zipCode" : 94568,
            "State" : "California"
        }
    }, 
    "002" : {
        "Name" : "Dilawar Shah", 
        "Age"  : 48,
        "Position" : "Senior Manager", 
        "Dept" : "IT" ,
       "address" : {
            "Street" : "3050 Finnian way, apt 440", 
            "City" : "Dublin", 
            "zipCode" : 94568,
            "State" : "California"
        }
                
    }
}

#Print the sub dictionary of employee based on user input.
empNo = input("Please enter the employee number to see details : ")
print("Employee details is : ", employeeData.get(empNo))

#accessing name 
print("Employee name : ", employeeData.get(empNo).get("Name"))

#accessing address
print("Employee address : ", employeeData.get(empNo).get("address"))

### Tuples
    # - Ordered, Im - Mutable and indexed.
    # - Syntax is round paranthesis. You can use round and no brackets.
tuple_w_brackets = (1, 2, 3, 4, 1)
print(tuple_w_brackets)

tuple_no_brackets = 6, 7, 3, 9
print(tuple_no_brackets)

"""
Each transaction record includes:
item name (str)
quantity (int)
date (str)
price (float)
""" 
#un-packing tuple with single statement
item, quantity, date, price = ("product-1", 2, "6-1-2023", 5.99)
print(item)
print(quantity)
print(date)
print(price)

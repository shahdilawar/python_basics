'''
Below file covers the basics of python. This deals with String, int, 
bool and basic operations.
'''
#Sample string
introString = "Hello world, to the life of Python"

# print first 5 chars:
# tempString = introString[:7]
# separator block
print ("-" * 50)
print("First 5 characters : " + introString[:7])

# print world alone:
# separator block
print ("-" * 50)
print("print world alone : " + introString[6:11])

'''
positive index starts at 0......n
negative index starts at -1 .... 0
'''

#print the rest of string after Hello
# separator block
print ("-" * 50)
print("rest of string after Hello " + introString[6:])

#Print lower and upper
# separator block
print ("-" * 50)
print(" upper case of sample string : " + introString.upper())

# Format
temperature = "Dublin is hot at : {}"
temp = 99
# separator block
print ("-" * 50)
print(temperature.format(temp))
#formatted string
# separator block
print ("-" * 50)
print(f"temparature is : {temp}")

#Getting user input
customername = input("What's your name? : ")
# separator block
print ("-" * 50)
print("Welcome " + customername)

#Using if statements
# separator block
print ("-" * 50)
birthDate = input("What's your birth year : ")

#if (birthDate is not None or birthDate.strip() != ""):
birthDate = int(birthDate)

if (birthDate > 2002):
    print("True")
else:
    print("False")

# Conditional if statements
# separator block
print ("-" * 50)
x = int(input("Enter value of X: "))
y = int(input("Enter value of Y: "))

if(x == y):
    print("X is equal to Y")
elif(x > y):
    print("X is greater than Y")
else:
    print("X is lesser than Y")

# For loop
numbers = [1, 2, 3, 4, 5]
# separator block
print ("-" * 50)
for number in numbers:
    print(number)

# Generating array using range
for number in range(1, 10):
    print(number)

# While loop
count = 1
while count <= 5:
    print(count)
    count += 1

#break statement
fruits = ["Apple", "Orange", "Kiwi", "Guava"]
# separator block
print ("-" * 50)
for fruit in fruits:
    
    if(fruit == "Kiwi"):
        print(fruit + "was found")
        break
    print(fruit)

# Checking type of objects
x = 25
y = 4.3
z = 8j
bool_value = True
# separator block
print ("-" * 50)
print(f"{x} is of : ", type(x))
print(f"{y} is of : ", type(y))
print(f"{z} is of : ", type(z))
print(f"{bool_value} is of : ", type(bool_value))

#Comparing objects using is operator.
x = [1, 2, 3, 4]
y = x
z = range(1, 5)

print(x is y)
print(y is x)

print(x is not z)




'''
Create two number-checker functions, isEven and isOdd.
The isEven function should return True if the argument passed into it 
is an even number, and False if the argument is an odd number. 
The isOdd function should return True if the argument passed into 
it is odd, and False if the argument is even. Test each function by 
using a loop to evaluate numbers zero through nine.
'''

# Define isEven function. it takes int as value and returns boolean.
def isEven(num):
    flag = False
    if (isinstance(num, int)):
        if (num % 2 == 0):
            flag = True 
    else:
        print("provide a integer value")
    return flag

# Define isOdd function. it takes int as value and returns boolean.
def isOdd(num):
    flag = False
    if (isinstance(num, int)):
        if (num % 2 != 0):
            flag = True 
    else:
        print("provide a integer value")
    return flag

# Check the range of numbers against isEven function  
# and print the result.
for i in range(0, 10):
    # check value of i is even number
    flag = isEven(i)
    print(f"{i} is Even : ", flag)
 
# Check the range of numbers against isOdd function  
#  and print the result.
for i in range(0, 10):
    # check value of i is Odd number
    flag = isOdd(i)
    print(f"{i} is Odd : ", flag)

'''
Function annotations are completely optional metadata information about 
the types used by user-defined functions.
    * Annotations are stored in the __annotations__ attribute of the 
      function as a dictionary and have no effect on any other part of the 
      function. 
    * Parameter annotations are defined by a colon after the parameter
      name, followed by an expression evaluating to the value of the
      annotation. 
    * Return annotations are defined by a literal ->, followed by an 
      expression, between the parameter list and the colon denoting 
      the end of the def statement. 
    * The following example has a required argument, an optional 
      argument, and the return value annotated:
'''

def meat_and_eggs(meat : str, eggs : str = "organic eggs") -> str:
    print("-" * 50)
    #print the associated annotations dictionary.
    print("function annotations are : \n", meat_and_eggs.__annotations__)
    print("Argumnets : " , meat, eggs)
    return meat + " and " + eggs
#call the function
print("Function return is : ", meat_and_eggs("mutton"))

#another example with list
def iterate_over_list(num : list[int]) -> list[int]:
    target_list = []
    print("-" * 50)
    print("function annotations are : \n", iterate_over_list.__annotations__)
    print("arguments : ", num)
    for i in num:
        target_list.append(i)
    return target_list
#call the function
print("Function return is : ", iterate_over_list([1, 2, 3, 5]))

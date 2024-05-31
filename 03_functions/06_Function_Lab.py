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

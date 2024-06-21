'''
* Generator functions in Python allow us to create a function that can 
    return a value and later resume from where it left off, 
    enabling the generation of a sequence of values over time.
* The main difference in syntax will be the use of a yield statement.
    * The main advantage is that, rather than calculating an entire 
        series of values all at once, the generator calculates one 
        value and then pauses, waiting for the next instruction.
    *  Generators are best for calculating large sets of results 
        (particularly in calculations that involve loops themselves) 
        in cases where we don’t want to allocate the memory for all 
        of the results at the same time.
'''
import random as rd
# Generator function for the cube of numbers (power of 3)
def gen_cubes(n : int):
    for num in range(n):
        yield pow(num, 3)

# Generate fibonacci series function
def gen_fibonacci_series(n : int):
    a = 1
    b = 1
    for num in range(n):
        yield a
        a, b = b, a+b

# Create a generator that yields "n" random numbers between a low and
#  high number (that are inputs). 
def gen_random_numbers(min_num : int, max_num : int):
        
        # generating a random step number.
        for i in range(min_num, max_num):
            yield rd.randint(min_num, max_num)

def test_classes():
    #seek input
    range_num = int( input ( "Enter range number : " ) )

    for i in gen_cubes(range_num):
        print(i)

    # generating fibonacci series
    #seek input
    fib_range_num = int( input ( "Enter fibonacci range number : " ) )
    for j in gen_fibonacci_series(fib_range_num):
        print(j)
    
    #generating random numbers between range
    #seek range min
    range_min = int( input ( "Enter minimun of range number : " ) )
   #seek range max
    range_max = int( input ( "Enter max of range number : " ) )
    for n in gen_random_numbers(range_min, range_max):
        print(n)


if __name__ == "__main__":
    test_classes()



'''
Building generators with generator expressions
* Generator expressions allow you to quickly create a generator object 
  in just a few lines of code.
* you can create them without building and holding the entire object 
    in memory before iteration.
* If speed is an issue and memory isn’t, then a list comprehension is 
    likely a better tool for the job
'''
import sys
# Method to define geerator expressions.
def generate_squares(n : int):
    nums_squared_gc = ( i**2 for i in range(n) )
    return nums_squared_gc

# Returns a list of squares
def list_of_squares(n : int) -> list:
    nums_squared_lc = [ i**2 for i in range(n) ]
    return nums_squared_lc

# Method to test the memory occupation between generator comprehension
# and list comprehension.
def test_memory_optimization(n : int):
    gen_comp = generate_squares(n)
    lc_comp = list_of_squares(n)

    gen_comp_mem_util = sys.getsizeof(gen_comp)
    lc_comp_mem_util = sys.getsizeof(lc_comp)

    print(f" gen_comp memory utilization is : {gen_comp_mem_util}")
    print(f" List comp memory utilization is : {lc_comp_mem_util}")


def test_classes():
    # Test generate squares method.
    #seek input
    no_of_squares = int (input ("Enter the range of numbers to be squared : ") )    
    for i in generate_squares(no_of_squares):
        print(i)

    #Compare mem util
    test_memory_optimization(no_of_squares)

if __name__ == "__main__" :
    test_classes()
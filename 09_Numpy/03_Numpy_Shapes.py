'''
An array has a shape given by the number of elements along each axis:
The shape of an array can be changed with various commands. Note that 

The following three commands all return a modified array, but do not 
change the original array:
    * ravel() returns the flattened array.
    * reshape(x, y)  - reshapes the array to specified index.
    * array.T - This transposes the array.
The following command modifies the existing array shape
    #array.resize(x, y)
'''
import numpy as np
from numpy import random as rg
from numpy import newaxis as na

# Utility function to print a separator line
def separator_block():
    print("-" * 50)

#Initialize an array using random
arr_1 = np.floor( ( 10 * rg.random( (3, 4) )) )
separator_block()
print(f"Array is : {arr_1}")
print(f"Array arr_1 shape is : {arr_1.shape}")

#Flatten the array using ravel() method.
flattened_array = arr_1.ravel()
separator_block()
print(f"Flattened Array is : {flattened_array}")

#reshape the flattened array to 6,2 dimension
reshaped_array = flattened_array.reshape( 6, 2 )
separator_block()
print(f"re shaped array is : {reshaped_array}")

#Transpose arrays using Array.T
transposed_array = reshaped_array.T
separator_block()
print(f"Transposed array is : {transposed_array}")
print(f"Transposed array shape is : {transposed_array.shape}")

#Resized arrays on existing array
transposed_array.resize(2, 6)
separator_block()
print(f"Resized array is : {transposed_array}")
print(f"Resized array shape is : {transposed_array.shape}")

'''
Stacking together different arrays. They can be acheived via 
following methods
    * vstack(arr1, arr2) - This vertically stacks the two arrays.
    * hstack(arr1, arr) - This horizontally stacks two arrays.
    * The function column_stack stacks 1D arrays as columns into a 
        2D array. It is equivalent to hstack only for 2D arrays:
'''
#array 1
arr_a1 = np.floor( ( 10 * rg.random((3, 2)) ) )
#array 2
arr_a2 = np.floor( ( 5 * rg.random((3, 2)) ) )

separator_block()
print(f"Array a1 is : {arr_a1}")
print(f"Array a2 is : {arr_a2}")

#Array post vstack() operation
vstack_res_array = np.vstack( (arr_a1, arr_a2) )
separator_block()
print(f"resultant array post vstack is : {vstack_res_array}")

#Array post hstack() operation
hstack_res_array = np.hstack( (arr_a1, arr_a2) )
separator_block()
print(f"resultant array post hstack is : {hstack_res_array}")

'''
column stack example
The function column_stack stacks 1D arrays as columns into a 2D array. 
It is equivalent to hstack only for 2D arrays:
'''
#Array post column stack operation
colstack_res_array = np.column_stack( (arr_a1, arr_a2) )
separator_block()
print(f"resultant array post column_stack is : {colstack_res_array}")

#column stack involving two 1D arrays will result in 2D array
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

oneD_2D_arr = np.column_stack ( (a, b) )
separator_block()
print(f"resultant 2D array post column_stack is : {oneD_2D_arr}")

#using newaxis to populate the arrays
# populate a into columnar 2D array
col_2D_arr = a[:, na]
separator_block()
print(f"resultant col_2D_arr array post newaxis is : {col_2D_arr}")

'''
Splitting arrays into smaller arrays
    * - hsplit
    * - vsplit
'''
large_array = np.floor(10 * rg.random((2, 12)))
separator_block()
print(f"Large array is : {large_array}")
# Split `large_array` into 3
split_arr1 = np.hsplit(large_array, 3)
separator_block()
for row in split_arr1:
    print(f"individual arrays is : {row}")

# Split `large_array` after the third and the fourth column
split_arr2 = np.hsplit(large_array, (3, 4) )
separator_block()
for row in split_arr2:
    print(f"individual arrays is : {row}")



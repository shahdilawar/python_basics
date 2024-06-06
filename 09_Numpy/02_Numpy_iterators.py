'''
* One-dimensional arrays can be indexed, sliced and iterated over, 
much like lists and other Python sequences.
* Multidimensional arrays can have one index per axis. These indices are
given in a tuple separated by commas:
'''
import numpy as np

# Utility function to print a separator line
def separator_block():
    print("-" * 50)

# Below examples for 1D array indexing, slicing and iteration.
one_d_arr = np.arange(10) ** 3

separator_block()
print("1D array is : ", one_d_arr)

#retrieve the third element in array
third_element = one_d_arr[2]
print(f"Third element of 1D array is : {third_element}")

#retrieve a range
sub_range = one_d_arr[2:5]
print(f"sub range of 1D array is between [2:5] is : {sub_range}")

#From start to every second elemet till 6th position
#update the value to 1000
one_d_arr[:6:2] = 1000
print(f"1D array post setting value to 1000 using [:6:2] is : {one_d_arr}")

#reverse the array
reversed_arr = one_d_arr[::-1]
print(f"1D array post reverse is : {reversed_arr}")

#iterate through all elements of the array. it iterates by axis 1.
for ele in reversed_arr:
    print(f" 1/3rd of value is : { (ele ** (1/3.) ) }")

# Below examples for multi dimensional array indexing, slicing 
# and iteration.
separator_block()
print("Multi Array indexing, slicing and iteration examples")
separator_block()
# initialize a multi dim array from a function using 
# ndArray.fromfunction(<function), (shape), dtype)
#populate array function
def populate_array(x, y):
    return 10*x + y

# This function creates the array using the function
multi_D_array = np.fromfunction(populate_array,
                                 (5, 4),
                                   dtype = np.int64)
print(f"multi_D_array initialized is : {multi_D_array}")

# Retreive value in 2nd row 3rd column
secondrow_3rdcol_element = multi_D_array[1 , 2]
separator_block()
print(f"value in 2nd row 3rd column is : {secondrow_3rdcol_element}")
print(type(secondrow_3rdcol_element))

#retreive 2nd column values in first 4 rows 
result_arr = multi_D_array[0:4, 1]
separator_block()
print(f"2nd column values in first 4 rows is : {result_arr}")
print(type(result_arr))

#retreive each column in second and third row
result_arr1 = multi_D_array[1:3, :]
separator_block()
print(f"Each column value in second and third row : {result_arr1}")

'''
Examples of 3 dimensional arrays.
The expression within brackets in b[i] is treated as an i followed by
 as many instances of : as needed to represent the remaining axes. 
 NumPy also allows you to write this using dots as b[i, ...].

The dots (...) represent as many colons as needed to produce a 
complete indexing tuple. For example, if x is an array with 5 axes, 
then
x[1, 2, ...] is equivalent to x[1, 2, :, :, :],
x[..., 3] to x[:, :, :, :, 3] and
x[4, ..., 5, :] to x[4, :, :, 5, :].
'''
three_D_array = np.array([
    [
        [0, 1, 2],
        [10, 11, 12]
    ],
    [
        [100, 101, 102],
        [110, 111, 112]
    ]
])

separator_block()
print(f"3D array is : {three_D_array}")

#shape of the array is
arr_shape = three_D_array.shape
separator_block()
print(f"Array shape is : {arr_shape}")

#retreive the elements in the second axes.
# same as three_D_array[1, :, :] or three_D_array[1]
second_axis_array = three_D_array[1, ...]
separator_block()
print(f"elements in the second axes : {second_axis_array}")

#retreive all the elements in the last column
# same as three_D_array[:, :, 2]
last_col_elements = three_D_array[..., 2]
separator_block()
print(f"elements in the last column : {second_axis_array}")

#Iterating over multiple arrays is done over the rows
separator_block()
for row in three_D_array:
    print(f"Array value is : {row}")

#If you need to do elementwise operation, use ndarray.flat attribute
for element in three_D_array.flat:
    print(f"element is : {element}")







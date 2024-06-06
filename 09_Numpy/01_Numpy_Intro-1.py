'''
NumPy is the fundamental package for scientific computing in Python. 
It is a Python library that provides a multidimensional array object, 
various derived objects (such as masked arrays and matrices), and an 
assortment of routines for fast operations on arrays, including 
mathematical, logical, shape manipulation, sorting, selecting, I/O, 
discrete Fourier transforms, basic linear algebra, basic statistical 
operations, random simulation and much more.
    - NumPy’s main object is the homogeneous multidimensional array 
    [ndarray].  It is a table of elements (usually numbers), all of 
    the same type, indexed by a tuple of non-negative integers. 
    In NumPy dimensions are called axes.
    - NumPy arrays have a fixed size at creation. Changing the size of 
    an ndarray will create a new array and delete the original.
    - The elements in a NumPy array are all required to be of the same 
    data type, and thus will be the same size in memory. 
    - The exception: one can have arrays of (Python, including NumPy) 
    objects, thereby allowing for arrays of different sized elements.
'''
import numpy as np
# Initialize ndarray with values starting from 20 t0 34.
# reshape it to 3 rows an 5 columns.
numpy_array = np.arange(20, 35).reshape(3, 5)

# Utility function to print a separator line
def separator_block():
    print("-" * 50)

separator_block()
# print the values of the array
print(" Array is \n : ", numpy_array)
# find the shape of the array.
numpy_array_shape = numpy_array.shape
print(f"numpy array shape is : {numpy_array_shape}")
# find the dim of the array, the number of
# axes (dimensions) of the array.
print(f"Number of axes : {numpy_array.ndim}")
# Total number of elements can be found using size attribute.
print(f"Total number of elements : {numpy_array.size}")
# Retrieve the data type of the object's using dtype.
print(f"Data type of objects in numpy array : {numpy_array.dtype}")

'''
NumPy offers several functions to create arrays with initial placeholder 
content. These minimize the necessity of growing arrays, an expensive 
operation.
The function zeros creates an array full of zeros, the function ones 
creates an array full of ones, and the function empty creates an array 
whose initial content is random and depends on the state of the memory. 
By default, the dtype of the created array is float64, 
but it can be specified via the key word argument dtype.
'''
# create an array from list
data_list = [1, 2, 3, 5, 7]
dyn_arr_from_list = np.array(data_list)
#call separator block
separator_block()
print(dyn_arr_from_list)

#create an array of 3 rows and 2 columns from zeroes.
dyn_arr_from_zeroes = np.zeros((3, 2))
#call separator block
separator_block()
print("ndarray populated using zeroes function", dyn_arr_from_zeroes)

#create an array of 3 rows and 2 columns from ones
dyn_arr_from_ones = np.ones((3,2), dtype = np.int64)
#call separator block
separator_block()
print("ndarray populated using ones function", dyn_arr_from_ones)

#create an array of 3 rows and 2 columns of random numbers.
#create the empty array.
empty_array = np.empty((3, 2), dtype = np.float64)
#Fill it with random numbers.
empty_array[:] = np.random.random((3, 2))
#call separator block
separator_block()
print(" Empty array : ", empty_array)

'''
To create sequences of numbers, NumPy provides the arange function which 
is analogous to the Python built-in range, but returns an array.
'''
#Below code will generate an array in a range of 5s
seq_array1 = np.arange(0, 30, 5)
separator_block()
print("array1 with sequence of numbers [0 to 30] : ", seq_array1)
seq_array2 = np.arange(0, 2, 0.3)
print("array2 with sequence of numbers [0 to 2] : ", seq_array2)

#Using linspace method to define the number 
seq_array3 = np.linspace(0, 2, 4)
print("array2 with sequence of numbers defined by linspace : ", seq_array3)

'''
Printing of arrays or saving to file.
One-dimensional arrays are then printed as rows, bidimensionals as 
matrices and tridimensionals as lists of matrices.
'''
one_d_array = np.arange(10)
separator_block()
print("one dimernsional arry print : ", one_d_array)
# Initialize an array and covert it to 2d using reshape
two_d_array = np.arange(9).reshape(3,3)
separator_block()
print("Two dimensional array is : ", two_d_array)
# Initialize an array and convert it to 3d using reshape
three_d_array = np.arange(27).reshape(3, 3, 3)
separator_block()
print("Three dimensional array is : ", three_d_array)

'''
Basic operations
Arithmetic operators on arrays apply elementwise. A new array is
created and filled with the result.
'''
arr_1 = np.array([20, 25, 32, 44])
arr_2 = np.arange(4)

#perform subtraction that creates a new array
arr_3 = arr_1 - arr_2
separator_block()
print("resultant array after subtraction operation is : ", arr_3)

#perform multiplication that creates a new array
arr_4 = arr_1 * arr_2
separator_block()
print("resultant array after multiplation operation is : ", arr_4)

#Applying ufunc likes sin and cosine
arr_to = np.array([15, 20, 22, 36])
arr_to_be_sin = 10 * np.sin(arr_to)
separator_block()
print("resultant array after sin operation is : ", arr_to_be_sin)

#cosine function to be applied
arr_to_be_cosine = 10 * np.cos(arr_to)
separator_block()
print("resultant array after cosine operation is : ", arr_to_be_cosine)

#check boolean values on array
bool_check_values = arr_to < 22
separator_block()
print("resultant array after cosine operation is : ", bool_check_values)

'''
Matrix multiplication
* operator is used for elementwise product.
@ matrix product
dot is used for dot product of two arrays.
'''
A = np.array([
            [1, 1], 
            [0, 1]
            ])

B = np.array([
            [2, 0], 
            [3, 4]
            ])

#element wise multiplication
ele_wise_mult_res_array = A * B
separator_block()
print(" element wise resultant array : ", ele_wise_mult_res_array)


#Dot product using @ symbol
ele_wise_dot_res_array = A @ B
separator_block()
print(" dot product resultant array using @ operator : ", ele_wise_dot_res_array)

#Dot product using dot symbol
ele_wise_dot_res_array = A.dot(B)
separator_block()
print(" dot product resultant array : ", ele_wise_dot_res_array)

'''
Some operations, such as += and *=, act in place to modify an 
existing array rather than create a new one.
'''
# below example is to multiply an existing array elements.
arr_a1 = np.ones((2, 3), dtype = np.int64)
#multiply by 3
arr_a1 *= 3
separator_block()
print(" modified array * 3 : ", arr_a1)

arr_a2 = np.empty((2, 3))
arr_a2 = np.random.random()
#add with arr_a1
arr_a2 += arr_a1
separator_block()
print(" modified array + arr_a1 : ", arr_a2)

# using sum() method that applies to all elemets across axes
arr_a4 = np.empty((3, 3))
#sum
sum_of_arr_a4 = arr_a4.sum()
#min
min_of_arr_a4 = arr_a4.min()
#max
max_of_arr_a4 = arr_a4.max()
separator_block()
print("Array a4 is : ", arr_a4)
print(" sum of arr_a4 : ", sum_of_arr_a4)
print(" min of arr_a4 : ", min_of_arr_a4)
print(" max of arr_a4 : ", max_of_arr_a4)

'''
By default, these operations apply to the array as though it were a 
list of numbers, regardless of its shape. However, by specifying 
the "axis" parameter you can apply an operation along the specified 
axis of an array:
    * axis(0) --> column wise operation
    * axis(1) --> row wise operation
'''
b = np.arange(12).reshape(3, 4)
separator_block()
print("array is : ", b)

# sum by each column 
sum_by_axes_0 = b.sum( axis=0 )
print("resultant column wise sum array is : ", sum_by_axes_0)

# sum by each row
sum_by_axes_1 = b.sum( axis = 1 )
print("resultant row wise sum array is : ", sum_by_axes_1)

#Cumulative sum that is store in the last row  of the column
cumulative_sum_axes_0 = b.cumsum( axis = 0 )
print("resultant column wise cumsum array is : ", cumulative_sum_axes_0)

#Cumulative sum that is store in the last column  of the row
cumulative_sum_axes_1 = b.cumsum( axis = 1 )
print("resultant row wise cumsum array is : ", cumulative_sum_axes_1)






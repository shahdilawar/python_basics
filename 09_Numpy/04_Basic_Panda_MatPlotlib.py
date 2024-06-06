import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

'''
File read operations using Panda
'''

# Utility function to print a separator line
def separator_block():
    print("-" * 50)

file_path = "/Users/kader8/learning/python_basics/09_Numpy/music.csv"

# read all contents from csv file
def read_all_data_from_csv():
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist")

    #read from the music.csv all the data into ndarray object
    try:
        x = pd.read_csv(file_path, header = 0).values
        separator_block()
        print(f"CSV contents is : {x}")
        print(f"Type of x is : {type(x)}")
    except Exception as e:
        print(f"error occured : {e}")

# You can also simply select the columns you need:
def read_specific_columns():
    separator_block()
    try:
        y = pd.read_csv(file_path, usecols=['Artist', 'Plays']).values
        print(f"CSV contents containing Artist and Plays : \n {y}")
    except Exception as e1:
        print(e1)

# Use the Panda dataframe to build a csv report


'''
Plotting arrays with MatPlotlib
'''
#initializing array
def plot_1D_array():
    a = np.array([2, 1, 5, 7, 4, 6, 8, 14, 10, 9, 18, 20, 22])
    #plotting the values
    plt.plot(a)
    #use show method to display
    plt.show()


def test_methods():
    read_all_data_from_csv()
    read_specific_columns()
    plot_1D_array()

if __name__ == "__main__":
    test_methods()
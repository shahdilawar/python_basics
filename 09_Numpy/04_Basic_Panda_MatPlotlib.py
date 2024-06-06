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
def panda_dataframe_demo():
    panda_df_arr = np.array([[-2.58289208,  0.43014843, -1.24082018, 1.59572603],
                [ 0.99027828, 1.17150989,  0.94125714, -0.14692469],
                [ 0.76989341,  0.81299683, -0.95068423, 0.11769564],
                [ 0.20484034,  0.34784527,  1.96979195, 0.51992837]])

    data_frame = pd.DataFrame(panda_df_arr)
    separator_block()
    print(f"Data frame object is : {data_frame}")

    try:
        data_frame.to_csv('/Users/kader8/learning/python_basics/09_Numpy/pd_generated.csv' , header=True)
    except Exception as e:
        print(e)

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

#plot timeseries data of two 1D arrays
def plot_timeseries_data():
    x = np.linspace(0, 10, 5)
    y = np.linspace(0, 20, 5)

    #plotting the values
    #purple line
    plt.plot(x, y, 'purple')
    #dots
    plt.plot(x, y, 'o')
    plt.show()



def test_methods():
    read_all_data_from_csv()
    read_specific_columns()
    panda_dataframe_demo()
    plot_1D_array()
    plot_timeseries_data()

if __name__ == "__main__":
    test_methods()
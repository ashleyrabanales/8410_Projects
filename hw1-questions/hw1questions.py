#%%
import numpy as np
#%%
if __name__ == "__main__":

#%%
# Takes two integer parameters as rows and columns, 
# and returns a numpy array with specified rows and columns of the value of 1
# HINT: Look at the np.ones function in the NumPy documentaion
  def q1_part1(rows:int, cols:int):
    a = np.ones((rows, cols))
    return a
    
#%%
# Takes two integer parameters as start and end,
# and returns a 1-d numpy array starting from "start" parameter, and ends with "end" parameter 
# IMPORTANT: the "end" value should be included in the range. 
# For example, if start=1, and end=3, the result should be [1,2,3]
# HINT: Look at the arange function in the NumPy documentaion
def q1_part2(start:int, end:int):
  np.arrange(1,4) #chage the parameters of functions

#%%
# Takes a numpy array as input,
# and returns an integer number with the value of max - min
def q1_part3(arr:np.ndarray):
  pass


#%%
# Takes a numpy array as input, and creates a new flat array with same values but with two modifications:
# 1. all numbers greater than 100 should become 100.
# 2. all negative numbers should become 0.
# then return the new modified array
# HINT: Look at the flatten function in the NumPy documentaion
def q2(arr: np.ndarray):
    pass


#%%
# Takes two numpy arrays "a1", and "a2" as input, and returns a number "c" 
# "c" is the minimum number of the element-wise sum of a1 and a2, if not negative, otherwise it should be 0
def q3(a1:np.ndarray, a2:np.ndarray):
    pass

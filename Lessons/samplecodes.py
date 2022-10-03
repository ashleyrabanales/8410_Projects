import numpy as np

# Creating a numpy array of zeros with 4 rows and 2 columns

arr1 = np.zeros((4,2))
print(arr1)
#[[0. 0.]
 #[0. 0.]
 #[0. 0.]]

 # Creating a numpy array of ones with 2 rows and 3 columns
arr2 = np.ones((2,3))
print(arr2)
#[[1. 1. 1.]
 #[1. 1. 1.]]

# Creating a 1-D numpy array ranging from 1 to 10
arr3 = np.arange(1,11)
print(arr3)
#[ 1  2  3  4  5  6  7  8  9 10]

# Getting minimum and maximum values of an array (for example, arr3)
min_val = np.min(arr3)
print(min_val)
#1
max_val = np.max(arr3)
print(max_val)
#10

# Flattening an array (for example, arr2)
flat_arr = arr2.flatten()
print(flat_arr)
#[10 10 10 10  5  6  7  8  9 10]

# Another example, consider the following array:
arr4 = np.array([[2.2,0.5],[-2.1,8],[0.1,-9]])

# change the values that are less than 1, but not negative to 0
arr4[(arr4<1) & (arr4>0)] = 0
print(arr4)

# Another example, consider the following array:
arr4 = np.array([[2.2,0.5],[-2.1,8],[0.1,-9]])

# change the values that are less than 1, but not negative to 0
arr4[(arr4<1) & (arr4>0)] = 0
print(arr4)
#[[ 2.2  0. ]
 #[-2.1  8. ]
 #[ 0.  -9. ]]




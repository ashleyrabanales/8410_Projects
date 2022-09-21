#%%
#Quiz Review
#show values of C only if C is not zero
c = 2 
if c! = 0:  #! not 
print (c)

#NUMPY
# - each arrays have some attributes
    #Size; TOTAL # of elements in an array
    #Shape: shape of an array
    #NDIM: dimension of tank of an array
    #Dtype: data type of elements in the array
#%%

import numpy as np
#%%
a = np.array ([[10, 4, 6], [2, 20, 1], [-2, 5, 1]])
print (a)

#%%
print("Size:", a.size, 
      "n\Shape:", a.shape,
      "n\Dimesnsion:", a.ndim,
      "n\Data Type:", a.dtype)
# %%
def array1(): ...

def array2():
    nums = np.array([5,6, 10, 18, 29])
    print("n\mean", np.mean(nums),
            "n\maximum". np.max(nums),
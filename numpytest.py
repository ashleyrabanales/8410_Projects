#%%
import pandas as pd  
import numpy as np

# %%
nums = np.array([5, 6, 10, 18, 29]) #one dimension numpy arrary, in a list []
print(np.mean(nums))
print(np.max(nums))
print(np.std(nums))
# %%
print("The 2d arrary")
nums2 = np.array( 
    [
        [5, 6, 10, 18, 29], #each row is a list
        [1,2,5,30,23],
        [13,2,5,-3,2],
        [15,23,53,20,0],
    ] 
    ) 
print(np.mean(nums2))
print(np.max(nums2))
print(np.median(nums2))
print(np.std(nums2))

# %%

#%%
import numpy as np
import hw1questions as hw1
#%%
if __name__ == "__main__":
#%%
    ## IMPORTANT: 
    #   I will use tools that detects similar answers, then I will manually check similar submissions. 
    #   If excessive similarities found, I will report the documents to the department.
    #   Please refer to the Plagirasm section on the syllabus for more information.

    # an array of 3 rows, and 2 columns with values of 1.
a = hw1.q1_part1(1,2) 
print("Q1. part1:\n", a)
#%%
    # a one dimensional array starting from 1 to 9
b = hw1.q1_part2(2,5)
print("Q1. part 2:\n", b)
#%%
    # "c" should be 23, which is the max (25) - the min (2), in other words: 25-2=23
d = hw1.q1_part3(np.array([5,2,10,25,11,2])) 
print("Q1. part 3:\n", c)
#%%
    # "d" should be a 1-d numpy array of [0,2,0,90,99,100,100,0]
d = hw1.q2(np.array([[-5,2,0,90],[99,100,101,-3]]))
print("Q2.:\n", d) 

    # "e" should  be 9
a1 = np.array([[20,21,22],[10,24,18]])
a2 = np.array([[2,0,-2],[-1,-1,-3]])
e = hw1.q3(a1, a2)
print("Q3. (test 1):\n", e) 

    # "f" should  be 0
a1 = np.array([[20,21,22],[23,24,25]])
a2 = np.array([[2,0,-25],[-1,-1,-3]])
f = hw1.q3(a1, a2)
print("Q3. (test 2):\n", f) 
# %%

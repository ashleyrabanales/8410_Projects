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

def array1():
    a = np.array([[10,4,6],
                    [2,20,1],
                    [-2,5,1]])
    print("Size:", a.size, 
        "\nShape:", a.shape, 
        "\nDimensions:", a.ndim, 
        "\nData Type:", a.dtype,
        "\nMinimum:", np.min(a),
        "\nMaximum:", np.max(a),
        "\nAverage:", np.mean(a),
        "\nMedian:", np.median(a),
        "\nStd:", np.std(a),
        )

def array2():
    nums = np.array([5,6,10,18,29])
    print("Mean:", np.mean(nums))
    print("Median:", np.median(nums))
    print("Std:", np.std(nums))

def matrix_operations():
    A = np.array([[1,2,3],[4,5,6],[7,8,9]])
    B = np.array([[1,-2,13],[14,52,16], [27,58,-9]])

    C = A + B # element-wise
    D = A * B # element-wise
    Ta = np.transpose(A)
    Fa = A.flatten()
    return C, D, Ta, Fa

def numpy_functions():
    A = np.array([[10,-2,3],
                    [40,5,-6],
                    [7,8,90]])
    A_sorted = np.sort(A) # sorts each row separately (row-wise) default: axis=1
    A_sorted2 = np.sort(A,axis=0) # column-wise
    A_sorted3 = -np.sort(-A,axis=1) # row-wise descending sort
    return A_sorted, A_sorted2, A_sorted3

if __name__ == "__main__":
    # array1()
    # array2()
    # c,d,ta,fa = matrix_operations()
    # print("Summation is \n", c)
    # print("Multiplication is \n", d)
    # print("Transpose of A is \n", ta)
    # print("A flatten is \n", fa)
    a,b,c = numpy_functions()
    print(c)
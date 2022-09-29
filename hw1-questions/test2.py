#%%
def avg(a, b, c):
    """

"""
    average = (a + b + c) / 3
    return average


def avg2(*args): #*argu many number as one wants
    length = len(args) #argu is a list or tuple cannot be divide by
    sum = 0
    for a in args:
        sum = sum + a
    average = sum / length #[] used to be ble to divide them
    return average          
#%%
#integers will return an integers
if __name__ == "__main__": #only run the following if test.py is executed directly, 
    print("taking average of 3 numbers=", avg(2, 3, 4))
  #  print("taking average of 3 numbers=", avg(2, 3,)
  #AVG function wotn work for another greater or less than the parameteres

    print ("Average=", avg2(2, 23, 34, 34, 42)) #can have many int

# %%

#%%
import numpy as np
#%%
if __name__ == "__main__":
    data = np.loadtxt("/Users/ashleyrabanales/8410_Projects/Lessons/inflammation-01.csv")
    print(data)
    print(f"Data has a shape of {data.shape}.") #60
    print(f"#Patients={data.shape[0]}, #Days = {data.shape[1]}") #P:59 #40days
#%%
    print("The first row patient's data:")
    print(data[0]) #prints the dirst row
# %%
    print("The first two patient's data:")
    print(data[0:2]) #data from index o to idex 2, excluding 2
#%%
    print("The first three patient's data:")
    print(data[:3]) #

#%%
    print("The first 3 days (columns) of the first 2 patients:")
    print(data[:2,:3])
#%%
    print("Inflammation of patient index 1, of day 4(index #3):")
    print(data[:2,:])

    print("Inflammation of the first patient in the first day:")
    print(data[0,0]) #Using the exact position
    print(data[:1,:1]) #Using the range in the index

    print("summation of the inflammation for all 40 days:")
    print(np.sum(data, axis = 0)) #Axis 0 is for days are columns

    print("the avg of the inflammation for all 40 days:")
    print(np.mean(data, axis = 0)) #max, std, min, mean, stats 

    print("the avg of the inflammation for each patient:")
    print(np.mean(data, axis = 1)) #axis 1 is rows



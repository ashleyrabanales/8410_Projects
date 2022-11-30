
import pandas as pd
import numpy as np
import finalproject as f

df = pd.read_csv('/Users/ashleyrabanales/8410_Projects/Final project/Coffee Chain.csv')

#converting date dtype:'object' to an datatime
df['Ddate'] = pd.to_datetime(df['Ddate'], errors='coerce')

#making the data decribe = 0 and have no negatives
df2 = df._get_numeric_data()
df2[df2 < 0] = 0

df=df.drop("Number of Records", axis=1)

if __name__ == "__main__":

#Quesion 1
    print("\n----Q1----")
a = f.q1(np.array(df.columns))
print("Q1.(Test 1):\n", a) 

#Question 2
print("\n----Q2----")
print(f.range_Coffee_Sales)


#Question 3
print("\n----Q3----")
    #c = 
pass

#Question 4
print("\n----Q4----")
    #d = 
pass

#Question 5
print("\n----Q5----")
    #e = 
pass

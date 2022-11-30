
import pandas as pd
import numpy as np
import final as ff

df = pd.read_csv('/Users/ashleyrabanales/8410_Projects/Final project/Coffee Chain.csv')

#converting date dtype:'object' to an datatime
df['Ddate'] = pd.to_datetime(df['Ddate'], errors='coerce')
df=df.drop("Number of Records", axis=1)

#making the data decribe = 0 and have no negatives
df2 = df._get_numeric_data()
df2[df2 < 0] = 0

if __name__ == "__main__":
#Quesion 1
    a = ff.q1(df)
    print("Q1.(Q1):\n", a) 

# #Question 2
    b = ff.q1(df)
    print("Q1.(Q1):\n", b) 

# #Question 3
# #print("\n----Q3----")
#     #c = 
# pass

# #Question 4
# #print("\n----Q4----")
#     #d = 
# pass

# #Question 5
# #print("\n----Q5----")
#     #e = 
# pass

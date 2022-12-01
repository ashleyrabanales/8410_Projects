
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

#getting the mean, max, min, std,
df.describe()

if __name__ == "__main__":
#Quesion 1
    a = ff.get_product_types(df)
    print("Q1.(Q1):\n", a) 

# #Question 2



# #Question 4
    b = ff.low(df,5)
    print("Q4.(Q4):\n", b)

# #Question 3
df['range_Coffee_Sales'] = df.apply(lambda b: ff.categories(b), axis=1)
print(df.range_Coffee_Sales)

# #Question 4






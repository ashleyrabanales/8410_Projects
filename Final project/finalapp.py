
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

#Method 1
    a=ff.method1(df)
    print("Method 1.\n", a)

#Method 2
    b= ff.method2(df)
    print("Method2.Area Code with Max profit:", b)

#Method 3
    c = df['range_Coffee_Sales'] = df.apply(lambda b: ff.method3(b), axis=1)
    print(df.range_Coffee_Sales)

#Method 4
    d= ff.method4(df,5)
    print("Method4.(Q4):\n", d)

#Method 5
    e=ff.method5(df)
    print("Method5.\n", e)






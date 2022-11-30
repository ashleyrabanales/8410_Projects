
import pandas as pd
import numpy as np

df = pd.read_csv('/Users/ashleyrabanales/8410_Projects/Final project/Coffee Chain.csv')
print('coffee imported!')

# iterating the columns and the number of columns 
#df.shape[1] 
#number of rows in df
#len(df.index)

# or
#df.shape[0] #4248

#getting infol of each columns dtype & nulls if present
#df.info(verbose=True)

#df.describe() #max, min, count, mean, std

#converting date dtype:'object' to an datatime
df['Ddate'] = pd.to_datetime(df['Ddate'], errors='coerce')

#df.Ddate.describe() #checking types for date

#df.describe()

#cleaning negative minimum to equal only 0s, i didint feel the need to use a loop
df2 = df._get_numeric_data()

df2[df2 < 0] = 0

#df.describe() #check if there is no negative numbers

#Data Cleaning 
df=df.drop("Number of Records", axis=1)
df["Ddate"].astype({'Ddate': 'datetime64[ns]'})
#df["Budget Sales"].astype(int)

if __name__ == "__main__":

#Questions 1 - Loops (for, or while)
def q1(df):
    d_avg = df[0]

    for x in df:
        d_avg = d_avg + x[df]
        d_avg = d_avg / len(df)
    return(+float(d_avg))
    #    columns = df.columns
    #    for col in columns:
    #        return (col)
   #df.shape[1] #21


products = [] #Dict of unique products 
for x in df["Profit"]: 
        for y in df["Product Type"]:
            if x >100:
                products.append(y)'''
pas

#Question 2 - Conditions with if statements
'''area_profit = {} # dict for storing profit of each area code
for areacode in df['Area Code'].unique(): # looping through area codes
    if areacode not in area_profit.keys():
        area_profit[areacode]=df[df['Area Code'] == areacode]['Profit'].sum() # storing total profit of particular area code in key value pair
v = list(area_profit.values()) # listing values
k = list(area_profit.keys()) # listing keys
print("Area Code with Max profit:",k[v.index(max(v))]) # getting key (area code) with maximum value'''
pass

#Question 4 - String functions (such as split, join, and lower)
#Getting 25%, 50%, and 75% of the column Coffee Sales to 
def categorise(b):  
    if b['Coffee Sales'] <= 100:
        return str('25%').strip().split() 
    elif b['Coffee Sales'] > 100 and b['Coffee Sales'] <= 138:
        return str('50%').strip().split() 
    elif b['Coffee Sales'] > 138:
        return str('75%').strip().split() 
df['range_Coffee_Sales'] = df.apply(lambda b: categorise(b), axis=1)
print(df.range_Coffee_Sales)

df.range_Coffee_Sales.head()
#Question 3 - Dictionaries
sales = {}
for i in df['range_Coffee_Sales']:
    for p in i == '75':
        print(str(i["range_Coffee_Sales"]))

df.range_Coffee_Sales.dtypes
    


#Question 5 - Error handling with try except blocks
'''for i in df["Area Code"].unique():
    for p in df["Inventory"]:
        for j in df["Budget Cogs"]:
            try:
                cal=(j/p)
                print(i , cal)
                break
            except Exception as e:
                print("Not Inventory Turnover:", e)
                break
    print(i)'''
pass
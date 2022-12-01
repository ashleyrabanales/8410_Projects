
import pandas as pd 
import numpy as np
import dateutil.parser as parser
import sys

df = pd.read_csv('/Users/ashleyrabanales/8410_Projects/Final project/Coffee Chain.csv')
print('coffee imported!')

#converting date dtype:'object' to an datatime
df['Ddate'] = pd.to_datetime(df['Ddate'], errors='coerce')
df=df.drop("Number of Records", axis=1)

#making the data decribe = 0 and have no negatives
df2 = df._get_numeric_data()
df2[df2 < 0] = 0

#getting the mean, max, min, std,sum, and count
df.head()

df.iloc[1,5]

len(df['Type'])


####Questions 1 - Loops (for, or while) 
#1 Use a For Loop to identify the product types out of coffee ,tea , etc with profit over $50
def get_product_types(df):
    products=[] #Dict of unique products 
    for x in df['Profit']: #Did a for loop in to the profit column 
        for y in df['Product Type']: #Another for loop into the diffrent types of coffee ,tea, etc
            if x >= 50: 
                products.append(y)                   # If profits are greater than or equal to $100
    return pd.unique(products)                  #Apped the names to the products dictionary 


####Question 2 - Conditions with if statements


#Question 3 - Dictionaries
# def q2(df):
#     area_profit = {} # dict for storing profit of each area code
#     for areacode in df['Area Code'].unique(): # looping through area codes
#         if areacode not in area_profit.keys():
#             area_profit[areacode]=df[df['Area Code'] == areacode]['Profit'].sum() # storing total profit of particular area code in key value pair
#     v = list(area_profit.values()) # listing values
#     k = list(area_profit.keys()) # listing keys
#     print("Area Code with Max profit:",k[v.index(max(v))]) # getting key (area code) with maximum value
# pass

#Question 4 -String functions (such as split, join, and lower)
def low(df, e):
    df['type2'] = df.iloc[:,e].str.lower()
    return df['type2']
    #df['type2'] = df['Type'].lower()



#Getting 25%, 50%, and 75% of the column Coffee Sales from df.describe
def categories(b):  
    if b['Coffee Sales'] <= 100:
        return ('low')
    elif b['Coffee Sales'] > 100 and b['Coffee Sales'] <= 138:
        return 'medium'
    elif b['Coffee Sales'] > 138:
        return 'high'

#Question 5 - Error handling with try except blocks
# for i in df["Area Code"].unique():
#     for p in df["Inventory"]:
#         for j in df["Budget Cogs"]:
#             try:
#                 cal=(j/p)
#                 print(i , cal)
#                 break
#             except Exception as e:
#                 print("Not Inventory Turnover:", e)
#                 break
#     print(i)
# pass
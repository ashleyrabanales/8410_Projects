#if __name__ == "__main__":
import pandas as pd 
import numpy as np
import dateutil.parser as parser
import sys

coffee=pd.read_csv("/Users/jonathancruz/Desktop/VS Code Workspace/Data programming /Coffee Chain.csv",parse_dates=['Ddate'])

#print(coffee.dtypes)


#Data Cleaning 
coffee=coffee.drop("Number of Records", axis=1)
coffee["Ddate"].astype({'Ddate': 'datetime64[ns]'})
coffee["Budget Sales"].astype(int)
#coffee["Area Code"].astype(str)


c2 = coffee._get_numeric_data()
c2[c2 < 0] = 0


# print(c2.describe())
# print(c2.dtypes)
# print(c2.head())

products=[] #Dict of unique products 
for x in coffee["Profit"]: 
    for y in coffee["Product Type"]:
        if x >100:
            products.append(y)
print("Names of unique product types with profit over $100:", pd.unique(products))


area_profit = {} # dict for storing profit of each area code
for areacode in coffee['Area Code'].unique(): # looping through area codes
    if areacode not in area_profit.keys():
        area_profit[areacode]=coffee[coffee['Area Code'] == areacode]['Profit'].sum() # storing total profit of particular area code in key value pair
v = list(area_profit.values()) # listing values
k = list(area_profit.keys()) # listing keys
print("Area Code with Max profit:",k[v.index(max(v))]) # getting key (area code) with maximum value


print(coffee.describe())


for i in coffee["Area Code"].unique():
    for p in coffee["Inventory"]:
        for j in coffee["Budget Cogs"]:
            try:
                cal=(j/p)
                print(i , cal)
                break
            except Exception as e:
                    print("Not Inventory Turnover:", e)
                    break
print(i)


        











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


def method1(coffee):
    products=[]
    for x in coffee["Profit"]:
        for y in coffee["Product Type"]:
            if x >= 50 :
                products.append(y)
    return pd.unique(products)


def method2(df):
    area_profit = {} # dict for storing profit of each area code
    for areacode in df['Area Code'].unique(): # looping through area codes
        if areacode not in area_profit.keys():
            area_profit[areacode]=df[df['Area Code'] == areacode]['Profit'].sum() # storing total profit of particular area code in key value pair
    v = list(area_profit.values()) # listing values
    k = list(area_profit.keys()) # listing keys
    return k[v.index(max(v))]
    #print("Area Code with Max profit:",k[v.index(max(v))]) # getting key (area code) with maximum value


#Getting 25%, 50%, and 75% of the column Coffee Sales from df.describe
def method3(b):  
    if b['Coffee Sales'] <= 100:
        return ('low')
    elif b['Coffee Sales'] > 100 and b['Coffee Sales'] <= 138:
        return 'medium'
    elif b['Coffee Sales'] > 138:
        return 'high'

def method4(df, e):
    df['type2'] = df.iloc[:,e].str.lower()
    return df['type2']
    #df['type2'] = df['Type'].lower()


def method5(df):
    #Question 5 - Produce an error if 
    qoutes=[]
    for i in df["Area Code"].unique(): 
        for cal in df["Inventory"]:
            for j in df["Budget Cogs"]:
                try:
                    qoutes.append([i,cal/j])
                except Exception as e:
                    return("Error",e)
    return pd.DataFrame(qoutes)
      
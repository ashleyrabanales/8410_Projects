# https://raw.githubusercontent.com/noghte/datasets/main/apartments.csv

import pandas as pd

# df1 = pd.read_csv("https://raw.githubusercontent.com/noghte/datasets/main/apartments.csv")
# print(len(df1))

df2 = pd.read_csv("apartments.csv")
print(len(df2))

# print(len(df1) == len(df2))

print(df2)

# Build year of the first row as an integer
print(int(df2.loc[0]["build_year"]))
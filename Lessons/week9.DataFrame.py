#%%
import pandas as pd 
# %%
if __name__ == '__main__':
    print(pd.__version__)
    states = pd.Series(['Georgia', 'North Carolina', 'Florida'])
    population = pd.Series([9000000, 7000000, 13000000])
    df = pd.DataFrame ({'State': states, 'Population': population})
    print(df)
# %%
print("------")
# A CSV File hosted online:
# https://raw.githubusercontent.com/noghte/datasets/mainapartment.csv
url = "https://github.com/noghte/datasets/blob/main/apartments.csv?raw=True"
df = pd.read_csv(url)
print(len(df))
# %%


 


# ILOC FOR INT
#lov for any int, list, etc

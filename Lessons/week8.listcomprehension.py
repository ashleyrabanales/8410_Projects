#%%
fruits =['apple', 'mango', 'strawberry', 'kiwi', 'melon']
    
  #%%  
#Get a list of fruits that start with a letter m
#Method 1
mfruits = []
for f in fruits:
    if f[0].lower() == "m":
        mfruits.append(f)

print (mfruits)

#%%
#Method 2
mfruits2 = [f for f in fruits if f[0].lower() == "m"]
print(mfruits2)

#Answer for last two questions
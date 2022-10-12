#Iterable - an obj. (adj to describe an obj) that can iterated over.
    #Includes string, list, set, dictionary, tuple, DataFrame, range, and NumpyArray
#%%
#Nested loops - requires more than one loop are nested loop op.
    #EX. syntax for an operation(op) w/ two for loop:
if __name__ == "__main__":
    fruits =['apple', 'mango', 'strawberry', 'kiwi']
    for f in fruits:
        print(f)


colors = [['red'], ['green', 'blue'], ['black', 'pink', 'blue']]
for c in colors:
    print (c)
    #list of lists
        #0 - red 
        #1 - green, blue
        #2 - black, pink, blue


#example of not printing
colors = [['red'], ['green', 'blue'], ['black', 'pink', 'blue']]
for c in colors:
    for i in c:
        if i != 'blue':  #!= does not equal blue
            print (i)

#%% #example of printing different capital by using lower() for lowercase
colors = [['red'], ['green', 'Blue'], ['black', 'pink', 'BLUE']]
for c in colors:
    for i in c:
        if i.lower() != 'blue':  #similar to: if i.upper() != 'BLUE'
            print (i)     
 #%%   

sold_items = [['C1', 'D1'], ['C1', 'D2'], ['C1']]
# How to get the unique list of the sold products?
products = []
for i in sold_items:
    for p in i:
        if p not in products:
            products.append(p)
            
print(products)
# %%

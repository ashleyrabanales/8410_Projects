for i in range(5):
    print(i)

#%%
for i in range(1, 10, 2):
    print(i)
# %%
#range is class that can print out 3 types of paramenter
#Indexing, Method 1
fruits =['apple', 'mango', 'strawberry', 'kiwi']
index = 0
for f in fruits:
    print(index, f)
    index = index + 1 


#Indexing, Method 2 (preferred)
for i in range(len(fruits)):
    print(i, fruits[i])
# %%

###### WHILE ###########
fruits =['apple', 'mango', 'strawberry', 'kiwi']

index = 0
while index < len(fruits): # while the condition is TRUE do that
    print(fruits[index])
    index = index + 1

# %%
while 1 == 1: #or TRUE
    print("hello") #infinite loop

#%%
i = 0
while True:
    print("hello")
    i = i + 1
    if i == 10:
         break
# %%

######### WHILE 2 ############
import datetime

c1 = datetime.datetime.now()
#for i in range(1000000):
#    a = i + 2

#c2 = datetime.datetime.now()

#print(c2 - c1)
while True:
    c1 = datetime.datetime.now()
    print(f"{c1:hour}:{c2:minutes}:{c3:seconds}")
    

# %%

#INTRO TO PYTHON

##Numeic Types: int (1,0,2), float
    #integer - whole #, positive and neg w/o decim.
    #float - character e or E by neg/pos int. specify scientific notation


#Text Type: str
    #str - seq of charac data
        #- '' or " " (delimited)
        #- an escape charac is a backlash\ followed by the charac you want to insert
        #-special meaning to charac print ('abc\)
        #-example: 'hello'.capitalize(), 'hello'.count("l"), 'hello'.endswith("o"), 'hello'.isalpha(), 'HeLLo'.lower(),
        #'Hello'.upper(), "  hello  ".strip()
#%%
"hello".count("l")
    #output: 2
#%%

#Boolean Type: bool (sequence)
    #bool is type that has one of two pissible values: T/F
    #use bool to check condition
#%%
a = 10
b = 4
if b > a:  
    print("b is greater than a") #true:if
else:
    print("b is not greater than a") #false:else

    #if else - allows to execute a block of code only if cond is true
    #elif - means if the "previous cond were not true, then try this condition"


#Sequence types: -immutable ( tuples and string)
                #- Mutable ( lists and sets)
        #LISTS to store multi item in a single vari.
#%%
myList = [1, 3, 'four', 5, 'six', 7]
#%%
myList [5]
myList [-3]
#%%
        #TUPLE - is a fixed length, immutable seq. Ordered and unchangeable!!
#%%
tup1 = (4, 6, 7)
tup2 = 4, 6 ,7 
tup = tuple('hello')
print(tup[0])
#%%


#Mapping: dict (ß)
    #DICT are used to store data values in KEY and VALUE pairs (CANNOT HAVE TWO ITEMS W/ SMAE KEY)
#%%
mycar = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print (mycar)
#%%

#Binary: bytes, bytearray
#None: NoneType

# %%
#FLOAT
x = 4.2 
y = .2 
a_large_number = 1.79e108
print(a_large_number)
print("{: 20e}".format(a_large_number))
print(format(a_large_number, 'f'))
#%%
#STRING
print('abc\tdef') #
print('abc\ndef') 
print(r'abc\tdef')

# %%

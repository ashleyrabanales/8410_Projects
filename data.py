#%%
def get_data():
    students = []

    st1 = {"FirstName": "Adel", "LastName": "Jordan", "Quiz1": 10}
    st2 = {"FirstName": "John", "LastName": "Rosa", "Quiz1": 8}
    students.append(st1) #.append Adds a Single Item. . extend() takes an iterable as an
    # argument, unpacks its items, and adds them to the end of your target list.
    students.append(st2)

    return students
if __name__ == "__main__": #to run blocks of code only if our program is the main program executed. 
    s = get_data() #This allows our program to be executable by itself, but friendly to other Python modules who may want to import some functionality without having to run the code.
    print (s)        
#%%


# %%

# def <function_name> (<parameters>):
#statement(s)>
#%%
from symbol import return_stmt


def f():
    s = "Inside the f function"
    print(s)
    
def g():
    pass #it doesn't run it

def h(width, height):
    area = width * height
    print(area)

def calculate_area(width, height):
    area = width * height
    return area

def calculate_area(width:int, height:int)->int:
    if not isinstance(width, int):
        raise "Incorrect width"
    if not isinstance(height, int):
        raise "Incorrect height"
    area = width * height
    print("width=", width, "height=", height)
    return area
#%%
def cube_area(x:int, y:int, z:int):
    return x * y * z

def cube_area3(x = 1, y = 1, z =1):
    return x * y * z

def divide (a:int, b:int)->float:
    if b !=0:
        return a/b
    else:
        return 0

    
#%%
# a function that takes an integar parameter and if the parametr is bt 1 & 10
# it prints parameter *2,if not, nothing will be printed
def multiply_by2(x):
    if x < 1: #exit the function
        return
    if x > 10:
        return
    print(x*2)

multiply_by2(12)
multiply_by2(0)
multiply_by2(5)
#%%
#TAKE AVERAGES OF INPIUT PARAMETERS
def avg(a, b, c):
    average = (a + b + c) / 3
    return average

#%%
#integers will return an integers
if __name__ == "__main__": #only run the following if test.py is executed directly, 
                            #do not run it if test.py is imported another file
    print ("Before f()")
    f()
    print("After")
    g()
    h(3, 5)
    # METHOD 1: positional arguments
    area = calculate_area(3, 5)
    # METHOD 2: NAMED ARGUMENTS
    area = calculate_area (width = 3, height = 5)
    #METHOD 1: another example w/ variables
    w =3
    h = 5
    area = calculate_area(w, h)
#Unexpected 
# %%
#METHOD 3: COMBINATION OF POSITIONAL AND NAMED ARGUMENTS
#name one, you need to name the others parameters
cube = cube_area(3, y = 2, z = 3)
print (cube)

d = divide(10,2)
print("Divide results=", d)

#%%
cube = cube_area3()
print("without any parameters=", cube)

cube = cube_area3(2)
print("with any parameters=", cube)


# %%

#
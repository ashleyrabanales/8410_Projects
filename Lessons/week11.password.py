#%%
import string
import random


if __name__ == "__main__":
    print("Letters:", string.ascii_letters) #ASCII - look up table 
    print("Lower:", string.ascii_lowercase)
    print("Upper:", string.ascii_uppercase)
    print("Punctuation:", string.punctuation)

    #randomly selecting 1 characters from a string
    print(random.choice("abc123"))

    #randomly selecting K characters from a string
    print(random.choices("abc123", k=3))

      #randomly selecting K unique characters from a string
    print(random.sample("abc123", k=5))

# %%

#JOIN
lst = ["a", "b", "c"]
#joining with a seperator ( can be join by any lst "APPLE")
print("-".join(lst))

#joing without a seperator
print("".join(lst))

#%%

#Creating a strong password
pswd_length = random.randint(10, 21) #random number from 10 - 21
pswd = random.choices(string.ascii_letters, k=pswd_length)
pswd = "".join(pswd)
print(pswd)

#adding a number
num = random.randint(1, 9)
random_index = random.randint(0, len(pswd)-1)
pswd = pswd[:random_index] + str(num) + pswd[:random_index+1:]
print(pswd)

 # %%

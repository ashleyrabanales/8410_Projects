import string
import random

if __name__ == "__main__":
    print("Letters:", string.ascii_letters)
    print("Lower:", string.ascii_lowercase)
    print("Upper:", string.ascii_uppercase)
    print("Punctuation:", string.punctuation)

    # Randomly selecting 1 character from a string
    print(random.choice("abc123")) 

    # Randomly selecting K characters from a string
    print(random.choices("abc123", k=5))

    # Randomly selecting K unique characters from a string
    print(random.sample("abc123", k=5))

    # join
    lst = ["a", "b", "c"]
    #joining with a - separator
    print("-".join(lst))

    #joinging without a separator
    print("".join(lst))

    #joinging with an AAPLE
    print("APPLE".join(lst))

    # Getting string of random choices
    print("".join(random.choices("abc123", k=5)))

    for i in range(100):

        # Creating a strong password:
        pswd_lenth = random.randint(10, 21) # random number between 10 to 21
        pswd = random.choices(string.ascii_letters, k=pswd_lenth)
        pswd = "".join(pswd)

        # adding a number
        num = random.randint(1, 900)
        random_index = random.randint(0, len(pswd)-1)
        pswd = pswd[:random_index] + str(num) + pswd[random_index:]
        print(pswd)
        


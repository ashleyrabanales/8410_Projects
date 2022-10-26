import pandas as pd

if __name__ == "__main__":

    # Method 1
    states = pd.Series(["Georgia", "North Carolina", "Florida"])
    df = pd.DataFrame({"State": states})
    print(df)
    
    print("----")
    # Method 2
    states = pd.Series(["Georgia", "North Carolina", "Florida"], index=["GA", "NC", "FL"])
    df = pd.DataFrame({"State": states})
    print(df)

    # Print the row having NC index
    print("Using loc function:", df.loc["NC"]["State"])

    # Print the row at index 1 (NC)
    print("Using iloc function:", df.iloc[1]["State"])

    print("----")
    states = pd.Series(["Georgia", "North Carolina", "Florida"])
    population = pd.Series([9000000, 7000000, 13000000])
    df = pd.DataFrame({"State": states, "Population": population})
    print(df)

    print("---")
    transactions = [
        {"id":20, "username": "ni998"},
        {"id":25, "username": "goodcustomer"},
        {"id":62, "username": "badcustomer"},
                ]
   
    # Create a dataframe of transactions with indices starting from 10
    print(list(range(10,len(transactions)+10)))
    indices = [i for i in range(10,len(transactions)+10)] # Method 1
    indices = list(range(10,len(transactions)+10)) #Method 2
    df2 = pd.DataFrame(transactions, index=indices)
    print(df2)
    
    # Printing the username of row index 10
    print(df2.loc[10]["username"])

    # Printing the username of the first row
    print(df2.iloc[0]["username"])

    print("----")

    # Create a DataFrame with the following columns from a dictionary:
    #   number: 20 to 29 (int)
    #   square: square of the number column (int)
    #   divisibleBy5: is the number divisible by 5? (True/False)
    # The index should be from A1 to A10
    
    source_dict = {
        "number": list(range(20,30)),
        "square": [i*i for i in range(20,30)],
        "divisibleBy5": [i%5==0 for i in range(20,30)]
    }
    df3 = pd.DataFrame(source_dict, index=[f"A{i}" for i in range(1,11)])
    print(df3)

    # Print the sum of the squares column
    print(f"Sum of the squares is {df3['square'].sum()}, and the average is {df3['square'].mean()}.")
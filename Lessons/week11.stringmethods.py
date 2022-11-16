def get_numbers_substring(s):
    lst = list(s)
    result = []
    for ch in lst:
        if ch.isdigit():
            result.append(int(ch))
    return result

if __name__ == "__main__":
    s = "IFI8410 course"
    ss = s[3:7] #getting 8410 from the above string
    print(ss)
    print("-----")

    #get the all the numbers from a string as integer
    c = get_numbers_substring(s)
    print(c)
    print("-----")

    #split
    items = "aa-b-cc-dd-ff" # a list of items separated by -
    print(items)
    #show each individual item 
    new_items = items.split("-")
    print(new_items)

    #extract each word in the sentence
    s = "     IFI8410 course     "
    words = s.split(" ")
    print(words)

    #strip: removes leading and tailing white spaces
    words = s.strip().split(" ")
    print(words)
    print("----")

    #remove all white spaces
    s = "     IFI8410 course     "
    nonspace_s = s.replace(" ", "")
    print(nonspace_s)
    print("----")

    # Chaining operations
    sentence = "   this TExT is Not well FORmatted.    "
    # format the text:
    formatted_s = sentence.strip().lower().capitalize()
    print(formatted_s)

    # find index of a substring
    # how to get the value of quantity?
    desc = "This product is available at inventory number 2. Quantity: 29, color: blue."
    qindex = desc.find("Quantity")
    print(qindex)
    start_index = qindex+9
    end_index = desc.find(",")
    print("Quantity is", desc[start_index:end_index].strip())

    # more realistic
    desc = "Product id: p-235, color: red, inventory number: 2, Quantity: 33, width: 10, height: 20"
    # Let's assume that quantity is always the 4th item

    # The above code step-by-step
    properties = desc.split(",") # the result is a list of values
    print(properties) 
    quantitiy_prop = properties[3] #the result is Quantity: 33
    print(quantitiy_prop)
    quantity = quantitiy_prop.split(":")[1]
    print(quantity)
    quantity = quantity.strip()
    quantity = int(quantity)
    print(quantity)

    # in one line:
    q = int(desc.split(",")[3].split(":")[1].strip())
    print(q)
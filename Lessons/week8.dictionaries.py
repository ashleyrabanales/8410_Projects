#%%
if __name__ == "__main__":

    #A list of dictionaries
    #sold_items = [['C1', 'D1'], ['C1', 'D2'], ['C1']]
    sold_items = [
        {"customer_name": "Brad", "member_id": 20, "items": ["C1", "D1"]},
        {"customer_name": "Alice", "member_id": 12, "items": ["C1", "D2"]},
        {"customer_name": "Brad", "member_id": 53, "items": ["C1"]}
    ]
#print a list of unique items
products = []
for i in sold_items:
    for p in i["items"]:
        if p not in products:
            products.append(p)

print(products)

#%%
# Print a list for customers
for i in sold_items:
    print(i["customer_name"])

#%%
#Print a list of customers who brought the product D2
#Method 1
for i in sold_items:
    if "D2" in i["items"]:
        print(i["customer_name"])


#Method 2
for i in sold_items:
    for p in i:
        if p == "D2":
            print(i["customer_name"])
# %%

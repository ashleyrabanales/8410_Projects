import numpy as np
import pandas as pd

# Q1. 
def get_integers(lst):   
    alist = []
    for a in lst:
        if type(a) == int:     # if lst is int, if lst equal int then append and return
            alist.append(a)
    return alist

""" Takes a list and returns a new list containing only integer values.
        For example, if the input parameter, lst, is ["abc", 20, 19.2, "1", 1, True, -1] 
        *then append to the 2nd list
        then, the return will be [20,1,-1]
        
#write one function and parameter is lst
    Args:
        lst (_list_): The input list that could contain any type of value.

    Returns:
        _list_: A list of only integer values of the input list.
    """


#Q2. 
def is_divisible_by_three(the_list, index):
   bcheck = [the_list]
   for b in the_list:  #do a iterate over the inside of the_list
        if b % 3 >= index: 
            return 'True'
        else:
            return 'False'

#used hw 1.3 to figure it out 
# c =  np.add(a1, a2) 
#    c_min = np.min(c) #fixed loop by doing only 'c' and new element
#   if c_min > 0:
#      return c_min
#   else:
#      return 0


""" Checks whether the value of the_list's index is divisible by 3.
        Uses the IndexError exception, and return False if the index is invalid

        HINT: You can use Python's modulo operator (%), 
        if a % b == 0, it means that a is divisible by b.
        # For example:
        #       10 is divisible by 2, because 10 % 5 == 0
        #       10 is not divisible by 3, because 10 % 3 == 1
                ** the reminder wil; be left
        # More information: https://realpython.com/python-modulo-operator/

    Args:
        the_list (list): The input list
        index (int): The index

    Returns:
        _type_: True: if the value is divisible by 3, 
                False: if the value is not divisible by 3,
                False: if the index is invalid
    """

#Q3. 
def remove_duplicates(items):
        c_removed = []
        for c in items: 
            if c not in c_removed:
                c_removed.append(c)
        return c_removed

#https://favtutor.com/blogs/remove-duplicates-from-list-python
#helpful site with 5 methods of removal

"""Removes duplicate items in a list

    Args:
        items (_type_): a list that might contain duplicate items

    Returns:
        list: a unique list of the received items 
        **similar to unique return one items adn returning to another list of items
    """


#Q4.
def average_rating(r):
    d_avg = 0
    for val in r:
        d_avg = d_avg + val['rate']
    d_avg = d_avg / len(r)
    return(+float(d_avg))


#  d_avg = []
# for r in r:
#    for d in r['rate']:
#        if d not in d_avg:
#            d_avg.append(r)
#         return(d_avg)


#   for d in r:
#      d_avg = d_avg + d
#      avg = d_avg / len(r) 
#   return avg 
   #this is for list and how do i make it for dict list?


"""Calculates the average ratings of all customer reviews

    Args:
        r (list): A list of customer reviews. Each customer review is a Python dictionary.

    Returns:
        float: The average of the ratings of all products
    """


#Q5. 
def ratings_below_two(lst):
    new_list = [i for i in lst if i["rate"] <= 2]
    e_below = [] 
    for i in new_list:
        if i["product_id"] not in e_below:
                e_below.append(i["product_id"])
    return e_below

#new_lst = [i for i in lst if rate < 2]
#  for"rate" <= 2:

#    products = []
#    for p in lst:
#           if p <= 2:
#              products.append(p)
#                return 

""" Finds products with at least one rating of <=2

    Args:
        lst (list): A list of customer reviews. Each customer review is a Python dictionary.
    Returns:
        list: a unique list of product IDs having at least one review of 2 or below 2.
    """


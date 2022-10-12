import numpy as np

# Q1. 
def get_integers(lst):
    """ Takes a list and returns a new list containing only integer values.
        For example, if the input parameter, lst, is ["abc", 20, 19.2, "1", 1, True, -1] 
        *then append to the 2nd list
        then, the return will be [20,1,-1]"""
        
#write one function and parameter is lst
    Args:
        lst (_list_): The input list that could contain any type of value.

    Returns:
        _list_: A list of only integer values of the input list.



#Q2. 
def is_divisible_by_three(the_list, index):
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
    pass

#Q3. 
def remove_duplicates(items):
    """Removes duplicate items in a list

    Args:
        items (_type_): a list that might contain duplicate items

    Returns:
        list: a unique list of the received items 
        **similar to unique return one items adn returning to another list of items
    """
    pass

#Q4.
def average_rating(r):
    """Calculates the average ratings of all customer reviews

    Args:
        r (list): A list of customer reviews. Each customer review is a Python dictionary.

    Returns:
        float: The average of the ratings of all products
    """
    pass

#Q5. 
def ratings_below_two(lst):
    """ Finds products with at least one rating of <=2

    Args:
        lst (list): A list of customer reviews. Each customer review is a Python dictionary.
    Returns:
        list: a unique list of product IDs having at least one review of 2 or below 2.
    """
    pass
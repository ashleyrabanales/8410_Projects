import numpy as np
import hw2 as hw

if __name__ == "__main__":    
    ## IMPORTANT: 
    #   I will use tools that detects similar answers, then I will manually check similar submissions. 
    #   If excessive similarities found, I will report the documents to the department.
    #   Please refer to the Plagirasm section on the syllabus for more information.

    print("\n----Q1----")
    a1 = [2, "40", 1.2, 6]
    a2 = [True, 19, 19.5, False]
    print(hw.get_integers(a1)) # expected output: [2, 6]
    print(hw.get_integers(a2)) # expected output: [19]

    print("\n----Q2----")
    b1 = [9,20,2,3]
    print(hw.is_divisible_by_three(b1, 0)) # True
    print(hw.is_divisible_by_three(b1, 1)) # False
    print(hw.is_divisible_by_three(b1, -1)) # True
    print(hw.is_divisible_by_three(b1, 6)) # False
    
    # Q3. Given a list, show all the items in the list without the duplicates.
    print("\n----Q3----")

    #Q3. Example 1
    c1 = [50,5,5,6,5,50,6]
    print(hw.remove_duplicates(c1)) # [50, 5, 6]

    #Q3. Example 2
    c2 = [ "Green", "Red", "Green", "Green", "Red"]
    print(hw.remove_duplicates(c2)) # ["Green", "Red"]

    # Q4. Comparing a list of customer ratings for an online shop, stored as a Python list of dictionaries,
    # show the average rate of all products together.
    print("\n----Q4----")
    ratings = [
        {"product_id": "P3", "rate": 4},
        {"product_id": "P4", "rate": 2},
        {"product_id": "P3", "rate": 5},
        {"product_id": "P3", "rate": 5},
        {"product_id": "P4", "rate": 1},
        {"product_id": "P2", "rate": 1},
        {"product_id": "P2", "rate": 3},
    ] #####list of dictionary###
    # In this example, we have a total 5 products, and the sum of rates are 17. Then, the average of rates are 17/5 = 
    print(hw.average_rating(ratings)) # 3.0 
    
    # Q5. Show the list of product IDs that have at least one rating of 2 or less than 2 
    # (NOTE: each product should be displayed only once)
    print("\n----Q5----")
    print(hw.ratings_below_two(ratings)) # ['P4', 'P2'] or ['P2', 'P4'] 

        #listcomprehension

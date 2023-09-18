"""
####  Sum of List Less Than 100 List Remix  ####

Given a list of numbers, return True if the sum of the values in the list is less than 100; otherwise return False.


[Examples]

___
list_less_than_100([5, 57]) ➞ True

list_less_than_100([77, 30]) ➞ False

list_less_than_100([0]) ➞ True
_____



[Notes]

N/A


[arrays] [language_fundamentals] [math] [validation] 



-------------------------------------------------------------------
[Resources]
_________
sum() function
https://www.w3schools.com/python/ref_func_sum.asp
Returns a number, the sum of all items in an iterable.
_________
_________
sum() Function
https://www.geeksforgeeks.org/sum-function-python/
Sums up the numbers in the list.
_________
_________
Comparison Operators
https://data-flair.training/blogs/python-comparison-operators/#:~:text=4.,to%20that%20on%20the%20right.
These are also called relational operators in Python.
Along with this, we will learn different types of Comparison
Operators in Python: less than, greater than, less t …
_________

"""


# Your code should go here:


def listLessThan100(lst1):
    ## Step: 1

    # To check whether every element in lst1 is numbers or not?
    allNum = 0
    for ele in lst1:
        if isinstance(ele, (int, float)):
            allNum += 1

    # if allNum == len(lst1): # This can also be used.
    try:
        assert allNum == len(lst1)
    except AssertionError:
        return "Not every element in lst1 is numbers."

    ## Step: 2

    # Adding the list.
    sum = 0
    for ele in lst1:
        sum += ele
    # return sum

    ## Step: 3
    if sum < 100:
        return True
    elif sum >= 100:
        return False


print(listLessThan100([5, 57]))  # ➞ True

print(listLessThan100([77, 30]))  # ➞ False

print(listLessThan100([0]))  # ➞ True

# check.
# coding style has increased 10 folds. Well done. Nitkarsh Chourasia.

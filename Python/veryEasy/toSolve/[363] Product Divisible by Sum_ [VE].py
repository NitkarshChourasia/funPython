"""
##Product Divisible by Sum?

Write a function that returns True if the product of a
list is divisible by the sum of that same list. Otherwise, return False.


[Examples]

___
divisible([3, 2, 4, 2]) ➞ False

divisible([4, 2, 6]) ➞ True
# 4 * 2 * 6 / (4 + 2 + 6)

divisible([3, 5, 1]) ➞ False
_____



[Notes]

N/A


[arrays] [math] [numbers] [validation]



-------------------------------------------------------------------
[Resources]
_________
Multiply All Numbers in the List (3 Different Ways)
https://www.geeksforgeeks.org/python-multiply-numbers-list-3-different-ways/
Given a list, print the value obtained after multiplying all numbers in a list.
_________
_________
functools.reduce() Method
https://www.geeksforgeeks.org/reduce-in-python/
Apply function of two arguments cumulatively to the items of iterable, from left to right, so as to reduce the iterable to a single value. For example, reduce(lambda x, …
_________
_________
How to return the product of a list?
https://stackoverflow.com/questions/2104782/returning-the-product-of-a-list
Is there a more concise, efficient or simply pythonic way to do the following? def product(list): p = 1 for i in list: p *= i return p
_________
"""
# Your code should go here:


def divisible(lst1):
    lst1Multiply = 1

    for i in lst1:
        lst1Multiply = multiply * i
    lst1Sum = lst1.sum()

    if lst1Multiply % lst1Sum == 0:
        return True
    else:
        return False

print(divisible([3, 2, 4, 2])) # ➞ False

print(divisible([4, 2, 6])) # ➞ True
# 4 * 2 * 6 / (4 + 2 + 6)

print(divisible([3, 5, 1])) # ➞ False



# testing.
# checkAgain.
# checkAgain. Important to check all the resources here, with respect to multiplication.

"""
####  Get the Sum of All List Elements  ####

Create a function that takes a list and returns the sum of all numbers in the list.


[Examples]

___
get_sum_of_elements([2, 7, 4]) ➞ 13

get_sum_of_elements([45, 3, 0]) ➞ 48

get_sum_of_elements([-2, 84, 23]) ➞ 105
_____



[Notes]

N/A


[arrays] [language_fundamentals] [loops] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
sum() Method
https://www.programiz.com/python-programming/methods/built-in/sum
Adds the items of an iterable and returns the sum. In this tutorial, we will learn about the sum() function with the help of examples.
_________
_________
sum() Method
https://www.geeksforgeeks.org/sum-function-python/
Sum of numbers in the list is required everywhere. Python provide an inbuilt function sum() which sums up the numbers in the list.
_________
_________
sum() Method
https://www.w3schools.com/python/ref_func_sum.asp
Returns a number, the sum of all items in an iterable.
_________
_________
sum() Function
https://www.geeksforgeeks.org/sum-function-python/
Sum of numbers in the list is required everywhere. Python provide an inbuilt function sum() which sums up the numbers in the list.
_________
_________
For Loop
https://www.geeksforgeeks.org/python-for-loops/
Is used for sequential traversal i.e. it is used for iterating over an iterable like String, Tuple, List, Set or Dictionary.
_________

"""


# Your code should go here:

def sumMethod(list1: list):
    return list1.sum()


def whileMethod(list1: list):
    i = 0
    sum = 0
    while i < len(list1):
        sum += list1[i]
    return sum


def forMethod(list1: list):
    sum = 0
    for i in list1:
        sum += i
    return sum


def recursiveMethod(list1: list):
    if i == len(list1):
        return sum  # See if declaration works?
    i = 0
    sum = 0
    i += 1
    sum += list1[i]
    return recursiveMethod(list1)


# Hope this works.


# sumMethod.
print(sumMethod([2, 7, 4]))  # ➞ 13

print(sumMethod([45, 3, 0]))  # ➞ 48

print(sumMethod([-2, 84, 23]))  # ➞ 105

# whileMethod.
print(sumMethod([2, 7, 4]))  # ➞ 13

print(sumMethod([45, 3, 0]))  # ➞ 48

print(sumMethod([-2, 84, 23]))  # ➞ 105

# forMethod.
print(sumMethod([2, 7, 4]))  # ➞ 13

print(sumMethod([45, 3, 0]))  # ➞ 48

print(sumMethod([-2, 84, 23]))  # ➞ 105

# recursiveMethod.
print(sumMethod([2, 7, 4]))  # ➞ 13

print(sumMethod([45, 3, 0]))  # ➞ 48

print(sumMethod([-2, 84, 23]))  # ➞ 105

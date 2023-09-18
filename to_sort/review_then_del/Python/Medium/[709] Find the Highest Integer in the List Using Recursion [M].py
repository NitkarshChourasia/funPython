"""
####  Find the Highest Integer in the List Using Recursion  ####

Create a function that finds the highest integer in the list using recursion.


[Examples]

___
find_highest([-1, 3, 5, 6, 99, 12, 2]) ➞ 99

find_highest([0, 12, 4, 87]) ➞ 87

find_highest([8]) ➞ 8
_____



[Notes]

Please use the recursion to solve this (not the max() method).


[data_structures] [numbers] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
Recursive function to find the largest number in the list?
https://stackoverflow.com/questions/12711397/python-recursive-function-to-find-the-largest-number-in-the-list
I'm trying to do a lab work from the textbook Zelle Python Programming The question asked me to "write and test a recursive function max() to find the largest number i …
_________
_________
Thinking Recursively in Python
https://realpython.com/python-thinking-recursively/
Problems (in life and also in computer science) can often seem big and scary. But if we keep chipping away at them, more often than not we can break them down into smal …
_________
_________
max() Method
https://www.programiz.com/python-programming/methods/built-in/max
Returns the largest item in an iterable. It can also be used to find the largest item between two or more parameters.
_________

"""


# Your code should go here:


def findHighest(lst):
    if len(lst) == 1:
        return lst[0]
    return max(lst[0], findHighest(lst[1:]))


print(findHighest([-1, 3, 5, 6, 99, 12, 2]))  # ➞ 99

print(findHighest([0, 12, 4, 87]))  # ➞ 87

print(findHighest([8]))  # ➞ 8


# complete.


def find_highest(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        sub_max = find_highest(lst[1:])
        return lst[0] if lst[0] > sub_max else sub_max


# Example usage:
print(find_highest([-1, 3, 5, 6, 99, 12, 2]))  # Output: 99
print(find_highest([0, 12, 4, 87]))  # Output: 87
print(find_highest([8]))  # Output: 8

"""
####  Find the Smallest Number in a List  ####

Create a function that takes a list of numbers and returns the smallest number in the list.


[Examples]

___
find_smallest_num([34, 15, 88, 2]) ➞ 2

find_smallest_num([34, -345, -1, 100]) ➞ -345

find_smallest_num([-76, 1.345, 1, 0]) ➞ -76

find_smallest_num([0.4356, 0.8795, 0.5435, -0.9999]) ➞ -0.9999

find_smallest_num([7, 7, 7]) ➞ 7
_____



[Notes]

___
*) Test cases contain decimals.
*) If you get stuck on a challenge, find help in the Resources tab.
*) If you're really stuck, unlock solutions in the Solutions tab.
___



[arrays] [loops] [numbers] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
min() Method
https://www.programiz.com/python-programming/methods/built-in/min
Returns the smallest element in an iterable or smallest of two or more parameters.
_________
_________
Finding the Largest and Smallest Number
http://programminginpython.com/python-program-largest-smallest-number-list/
A simple python program to find the smallest and largest element in a list. Here we use 2 functions max() and min() to find the largest and smallest number.
_________
_________
Python Program To Find The Biggest & Smallest of 3 Numbers
https://medium.com/programminginpython-com/python-program-to-find-the-biggest-and-smallest-of-3-numbers-using-lists-6a1a32119f0e
Here we discuss a simple python program which finds the biggest and smallest number out of given three numbers. Here we use python lists in this program. Here we add th …
_________
_________
min() Function
https://www.w3schools.com/python/ref_func_min.asp
Returns the item with the lowest value, or the item with the lowest value in an iterable. If the values are strings, an alphabetically comparison is done.
_________
_________
min() Function
https://www.geeksforgeeks.org/python-min-function/
Finds the minimum value in a list.
_________
_________
sort() List Method
https://www.freecodecamp.org/news/python-sort-how-to-sort-a-list-in-python/
Learn a different way of performing sorting in Python by using the sorted() function so you can see how it differs from sort(). By the end, you will know the basics of …
_________

"""


# Your code should go here:


def findSmallestNumMinFunc(list1):
    return min(list1)


def findSmallestNumsortedFunc(list1):
    return sorted(list1)[0]


def findSmallestNumsortMeth(list1):
    return list1.sort()[0]


# The same error as of non subscript-able and NoneType may follow up here, too.

# Min function.

print("Outputs by using Min Function.")
print(findSmallestNumMinFunc([34, 15, 88, 2]))  # ➞ 2

print(findSmallestNumMinFunc([34, -345, -1, 100]))  # ➞ -345

print(findSmallestNumMinFunc([-76, 1.345, 1, 0]))  # ➞ -76

print(findSmallestNumMinFunc([0.4356, 0.8795, 0.5435, -0.9999]))  # ➞ -0.9999

print(findSmallestNumMinFunc([7, 7, 7]))  # ➞ 7

# Sorted function.

print("Outputs by using Sorted Function.")
print(findSmallestNumsortedFunc([34, 15, 88, 2]))  # ➞ 2

print(findSmallestNumsortedFunc([34, -345, -1, 100]))  # ➞ -345

print(findSmallestNumsortedFunc([-76, 1.345, 1, 0]))  # ➞ -76

print(findSmallestNumsortedFunc([0.4356, 0.8795, 0.5435, -0.9999]))  # ➞ -0.9999

print(findSmallestNumsortedFunc([7, 7, 7]))  # ➞ 7

# sort function.

print("Outputs by using Sort Method.")
print(findSmallestNumsortMeth([34, 15, 88, 2]))  # ➞ 2

print(findSmallestNumsortMeth([34, -345, -1, 100]))  # ➞ -345

print(findSmallestNumsortMeth([-76, 1.345, 1, 0]))  # ➞ -76

print(findSmallestNumsortMeth([0.4356, 0.8795, 0.5435, -0.9999]))  # ➞ -0.9999

print(findSmallestNumsortMeth([7, 7, 7]))  # ➞ 7

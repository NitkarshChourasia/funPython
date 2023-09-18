"""
####  Find the Largest Number in a List  ####

Create a function that takes a list of numbers. Return the largest number in the list.


[Examples]

___
findLargestNum([4, 5, 1, 3]) ➞ 5

findLargestNum([300, 200, 600, 150]) ➞ 600

findLargestNum([1000, 1001, 857, 1]) ➞ 1001
_____



[Notes]

___
*) Expect either positive numbers or zero (there are no negative numbers).
*) If you get stuck on a challenge, find help in the Resources tab.
*) If you're really stuck, unlock solutions in the Solutions tab.
___



[arrays] [loops] [numbers] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
max() Method
https://www.programiz.com/python-programming/methods/built-in/max
Returns the largest element in an iterable or largest of two or more parameters.
_________
_________
max() Method
https://docs.python.org/3/library/functions.html#max
Return the largest item in an iterable or the largest of two or more arguments.
_________
_________
Aggregations: Min, Max, and Everything In Between
https://jakevdp.github.io/PythonDataScienceHandbook/02.04-computation-on-arrays-aggregates.html#Minimum-and-Maximum
Similarly, Python has built-in min and max functions, used to find the minimum value and maximum value of any given array.
_________
_________
Python Program to Find Largest Number in a List
https://www.geeksforgeeks.org/python-program-to-find-largest-number-in-a-list/
Given a list of numbers, the task is to write a Python program to find the largest number in given list.
_________
_________
max() Function
https://www.w3schools.com/python/ref_func_max.asp
Returns the item with the highest value, or the item with the highest value in an iterable. If the values are strings, an alphabetically comparison is done.
_________
_________
Video Walk Through the Challenge
https://youtu.be/FfGTh_qm-WU
A video walkthrough of this challenge.
_________
_________
sorted() Function
https://www.geeksforgeeks.org/python-sorted-function/
Returns a sorted list from the iterable object.
_________
_________
max() Function
https://www.educba.com/max-function-in-python/
Here we discuss two different ways of implementing the max() function in python along with examples.
_________

"""


# Your code should go here:

# There are three ways to solve the following. Let's do all three ways.


def findLargestNumMaxFunc(list1):
    try:
        for i in list1:
            assert i >= 0
    except AssertionError:
        return "Please input all numbers above zero, please."
    return max(list1)


def findLargestNumsortMeth(list1):
    try:
        for i in list1:
            assert i >= 0
    except AssertionError:
        return "Please input all numbers above zero, please."
    return list1.sort()[-1]


# Yeh batao yeh NoneType kyu de raha hai aur kyu keh raha hai objet is not subscriptable.
# Ismai kya error hai bhai sahab???? Yeh wale sort function?
# review this again, tommorow and ask chatGpt about it. Tell me chatGpt why is this showing me error please.
# chatGpt please explain me this error in much more detail for future things.
# Also find out what it is meant by none type.
def findLargestNumsortedFunc(list1):
    try:
        for i in list1:
            assert i >= 0
    except AssertionError:
        return "Please input all numbers above zero, please."
    return sorted(list1)[-1]


# Max function.
print(findLargestNumMaxFunc([4, 5, 1, 3]))  # ➞ 5
print(findLargestNumMaxFunc([300, 200, 600, 150]))  # ➞ 600
print(findLargestNumMaxFunc([1000, 1001, 857, 1]))  # ➞ 1001

# Sort Method.
print(findLargestNumsortMeth([4, 5, 1, 3]))  # ➞ 5
print(findLargestNumsortMeth([300, 200, 600, 150]))  # ➞ 600
print(findLargestNumsortMeth([1000, 1001, 857, 1]))  # ➞ 1001

# Sorted Function.
print(findLargestNumsortedFunc([4, 5, 1, 3]))  # ➞ 5
print(findLargestNumsortedFunc([300, 200, 600, 150]))  # ➞ 600
print(findLargestNumsortedFunc([1000, 1001, 857, 1]))  # ➞ 1001

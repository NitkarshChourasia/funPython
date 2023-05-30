"""
##Minimum Removals to Make Sum Even

Create a function that returns the minimum number of elements removed to make the sum of all elements in a list even.


[Examples]

___
minimum_removals([1, 2, 3, 4, 5]) ➞ 1

minimum_removals([5, 7, 9, 11]) ➞ 0

minimum_removals([5, 7, 9, 12]) ➞ 1
_____



[Notes]

___
*) If the sum is already even, return 0 (see example #2).
*) The output will be either 0 or 1.
___



[arrays] [higher_order_functions] [loops]



-------------------------------------------------------------------
[Resources]
_________
Minimum Removals to Make Array Sum Even
https://www.geeksforgeeks.org/minimum-removals-to-make-array-sum-even/
Given an array Arr[] of N integers. We need to write a program to find minimum number of elements needed to be removed from the array, so that sum of remaining element …
_________
_________
List sum() Method
https://www.programiz.com/python-programming/methods/built-in/sum
Adds the items of an iterable and returns the sum.
_________
"""
# Your code should go here:

def minimumRemoval(lst1):
    if lst1.sum() % 2 == 0:
        return 0
# if odd then want to remove a odd element then sum - do this recurringly until positive sum is achieved.
    while lst1.sum() % 2 == 1:
        elif lst1.sum() % 2 == 1:
        for i in lst1:
            if i % 2 == 1:
                lst1.pop(i)
        lst1.sum() % 2 == 0:
            return theNumberOfIndex
        lst1.sum() % 2 == 1:
            return theNumberOfIndex

# Notes output will be either 1 or 0, but make a one with extra added features.
# testing.
# checkAgain.
# learn to make recurring testing numbers.
# incomplete.



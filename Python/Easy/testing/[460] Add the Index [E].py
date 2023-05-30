"""
##Add the Index

Given a list of numbers, create a function which returns the list but with each element's index in the
list added to itself. This means you add 0 to the number at index 0, add 1 to the number at index 1, etc...


[Examples]

___
add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4]

add_indexes([1, 2, 3, 4, 5]) ➞ [1, 3, 5, 7, 9]

add_indexes([5, 4, 3, 2, 1]) ➞ [5, 5, 5, 5, 5]
_____



[Notes]

You'll only get numbers in the list.


[arrays] [language_fundamentals] [loops] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
enumerate() Function Demystified
https://dbader.org/blog/python-enumerate
How and why you should use the built-in enumerate function in Python to write cleaner and more Pythonic loops. Python’s enumerate function is a mythical beast—it’s hard …
_________
_________
Iterate Over a List
https://www.geeksforgeeks.org/iterate-over-a-list-in-python/
List is equivalent to arrays in other languages, with the extra benefit of being dynamic in size. In Python, list is a type of container in Data Structures, which is us …
_________
_________
enumerate() Method
https://www.tutorialspoint.com/enumerate-in-python
When using the iterators, we need to keep track of the number of items in the iterator. This is achieved by an in-built method called en ...
_________
""" 
# Your code should go here:

def addIndexes(lst1):
    outputLst1 = []
    i = 0
    while(i < lst1.len()):
        outputLst1.append(lst1[i] + i)
        i = i + 1
    return outputLst1


print(addIndexes([0, 0, 0, 0, 0])) # ➞ [0, 1, 2, 3, 4]

print(addIndexes([1, 2, 3, 4, 5])) # ➞ [1, 3, 5, 7, 9]

print(addIndexes([5, 4, 3, 2, 1])) # ➞ [5, 5, 5, 5, 5]

# testing.
# checkAgain.
# checkAgain. Check all the resources again.



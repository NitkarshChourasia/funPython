"""
##Find the Odd Integer

Create a function that takes a list and finds the integer which appears an odd number of times.


[Examples]

___
find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) ➞ -1

find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) ➞ 5

find_odd([10]) ➞ 10
_____



[Notes]

There will always only be one integer that appears an odd number of times.


[arrays] [bit_operations] [loops] [math]



-------------------------------------------------------------------
[Resources]
_________
count() Method
https://www.programiz.com/python-programming/methods/list/count
Returns the number of occurrences of an element in a list.
_________
_________
Find the Number Occurring Odd Number of Times
https://www.geeksforgeeks.org/find-the-number-occurring-odd-number-of-times/
Given an array of positive integers. All numbers occur even number of times except one number which occurs odd number of times. Find the number in O(n) time & constant …
_________
_________
if/else in Python's list comprehension?
https://stackoverflow.com/questions/4260280/if-else-in-pythons-list-comprehension
How can I do the following in Python? row = [unicode(x.strip()) for x in row if x is not None else ''] Essentially: replace all the Nones with empty strings, and then …
_________
_________
How can I count the occurrences of a list item?
https://stackoverflow.com/questions/2600191/how-can-i-count-the-occurrences-of-a-list-item
Discussions on how to count occurrences in a list without using count() method.
_________
"""
# Your code should go here:

# if there anything as num instead of float(n) or int(n): ?

def findOdd(lst1):

    # Finding odd list
    # Making unique list.
    setLst1 = set(lst1)

    # Finding counts of unique list.
    countLst1 = []
    for i in setLst1: # See if it behaves properly, so.
        countLst1.append(lst1.count(i))

    # Finding odd counts from countlist.
    oddlst1 = []
    i = 0
    while i == countLst1.len(): # Count starts from 0 or 1.
        if countLst1[i] % 2 == 1:
            oddlst1.append(countLst1[i])
            i = i + 1

    outputAns0 = [] # If == 1 then int if more then lst1
    for i in oddlst1:
        outputAns0.append(countLst1.index(i))
    outputAns1 = []
    for i in outputAns0:
        outputAns1.append(setLst1.index(i))

    # Output of answers.
    if outputAns1.len() == 1:
        return int(outputAns1)
    elif outputAns1.len() > 1:
        return outputAns1
    elif outputAns1.len() == 0:
        return "No integers appeared odd numbers of times."


# testing.
# checkAgain.
# checkAgain. Check all the resources unknown to you.


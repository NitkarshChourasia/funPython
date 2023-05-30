"""
##Flatten the Curve

Given a list of integers, replace every number with the mean of all numbers.


[Examples]

___
flatten_the_curve([1, 2, 3, 4, 5]) ➞ [3, 3, 3, 3, 3]

flatten_the_curve([0, 0, 0, 2, 7, 3]) ➞ [2, 2, 2, 2, 2, 2]

flatten_the_curve([4]) ➞ [4]

flatten_the_curve([]) ➞ []
_____



[Notes]

___
*) Round averages to 1 decimal point.
*) Return an empty list if given an empty list (see example #4).
___



[arrays] [language_fundamentals] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
How to Calculate Average in Python
https://appdividend.com/2019/01/28/python-statistics-tutorial-mean-function-example/#:~:text=In%20Python%2C%20we%20usually%20do,data%20set%20passed%20as%20parameters.
In this article, we'll learn everything about Python lists, how they are created, slicing of a list, adding or removing elements from them and so on.
_________
_________
round() Method
https://www.w3schools.com/python/ref_func_round.asp
Returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.
_________
_________
Python List
https://www.programiz.com/python-programming/list
In this article, we'll learn everything about Python lists, how they are created, slicing of a list, adding or removing elements from them and so on.
_________
""" 
# Your code should go here:

def flattenTheCurve(lst1):
    sumLst1 = lst1.sum()
    mean = (sumLst1/lst1.len()).round(1)
    # Is there a more good way to append to the list? A less ram consuming way?
    i = 0
    outputLst1 = []
    while (i < lst1.len()):
        outputLst1.append(mean)
        i = i + 1
    return outputLst1
# See if , if the zero list things works properly if not then add the if else thing.


print(flattenTheCurve([1, 2, 3, 4, 5])) # ➞ [3, 3, 3, 3, 3]

print(flattenTheCurve([0, 0, 0, 2, 7, 3])) # ➞ [2, 2, 2, 2, 2, 2]

print(flattenTheCurve([4])) # ➞ [4]

print(flattenTheCurve([])) # ➞ []


# testing.
# checkResources.
# check the comments in places.

# Is there a more good way to append to the list? A less ram consuming way?
# See if , if the zero list things works properly if not then add the if else thing.

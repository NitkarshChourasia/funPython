"""
##Shapes With N Sides

Create a function that takes a whole number as input and returns the shape with that number's amount of sides.
Here are the expected outputs to get from these inputs.



[Examples]

___
n_sided_shape(3) ➞ "triangle"

n_sided_shape(1) ➞ "circle"

n_sided_shape(9) ➞ "nonagon"
_____



[Notes]

___
*) There won't be any tests with a number below 1 or greater than 10.
*) Return the output in lowercase.
*) The challenge is intended to be completed without conditionals (it would take too long)!
___



[arrays] [geometry] [math] [objects]



-------------------------------------------------------------------
[Resources]
_________
Dictionaries in Python
https://realpython.com/python-dicts/
We'll cover the basic characteristics of Python dictionaries and learn how to access and manage dictionary data. Once you have finished this tutorial, you should have a …
_________
"""
# Your code should go here:


def nSidedShape(num1):
    if num1 > 1 and num1 <= 10:
        dictShape = {1: }

    else:
        return "Invalid side's n input."


print(nSidedShape(1))
print(nSidedShape(2))
print(nSidedShape(3))
print(nSidedShape(4))
print(nSidedShape(5))
print(nSidedShape(6))
print(nSidedShape(7))
print(nSidedShape(8))
print(nSidedShape(9))


# testing.
# checkAgain.
# what is the most efficient way of making the dictionaries.
# what is the most efficient way of making long i.e very long dictionaries.

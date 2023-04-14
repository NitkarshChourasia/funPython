"""
##Both Zero, Negative or Positive

Write a function that returns True if both numbers are:
___
*) Smaller than 0, OR ...
*) Greater than 0, OR ...
*) Exactly 0
___

Otherwise, return False.


[Examples]

___
both(6, 2) ➞ True

both(0, 0) ➞ True

both(-1, 2) ➞ False

both(0, 2) ➞ False
_____



[Notes]

Inputs will always be two numbers.


[conditions] [math] [numbers] [validation]



-------------------------------------------------------------------
[Resources]
_________
Conditional Statements
https://www.tutorialspoint.com/python/python_if_else.htm
An else statement can be combined with an if statement. An else statement contains the block of code that executes if the conditional expression in the if statement res …
_________
_________
Basic Python Operators
https://www.w3schools.com/python/python_operators.asp
Operators are used to perform operations on variables and values. Python divides the operators in the following groups: Arithmetic operators Assignment operat …
_________
"""
# Your code should go here:


def both(a, b):
    if a and b > 0 or a and b < 0 or a and b == 0:
        return True
    else:
        return False



print(both(6, 2)) # ➞ True
print(both(0, 0)) # ➞ True
print(both(-1, 2)) # ➞ False
print(both(0, 2)) # ➞ False


# Use brackets in if, if it throws an error.

# testing.

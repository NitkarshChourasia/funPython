"""
####  Return the Next Number from the Integer Passed  ####

Create a function that takes a number as an argument, increments the number by +1 and returns the result.


[Examples]

___
addition(0) ➞ 1

addition(9) ➞ 10

addition(-3) ➞ -2
_____



[Notes]

___
*) Don't forget to return the result.
*) If you get stuck on a challenge, find help in the Resources tab.
*) If you're really stuck, unlock solutions in the Solutions tab.
___



[algebra] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Python Operators: Arithmetic, Comparison, Logical and more.
https://www.programiz.com/python-programming/operators
Operators are special symbols in Python that carry out arithmetic or logical computation. The value that the operator operates on is called the operand.
_________
_________
All Python Operators
https://www.w3schools.com/python/python_operators.asp
Are used to perform operations on variables and values. Python divides the operators in the following groups: Arithmetic operators, Assignment operators, Comparison o …
_________
_________
Numbers, Type Conversion and Mathematics
https://www.programiz.com/python-programming/numbers
In this article, you'll learn about the different numbers used in Python, how to convert from one data type to the other, and the mathematical operations supported in P …
_________
_________
Increment Operation
https://www.askpython.com/python/examples/python-increment-operation
How do you perform a Python increment operation? If you're coming from a language like C++ or Java, you may want to try extending a similar increment. Before going with …
_________

"""
# Your code should go here:

from numbers import Number
from typing import Any


# Meta data.
__author__ = "Nitkarsh Chourasia"
__version__ = "1.0.0"
__date__ = "05-09-2023"
__difficulty__ = "Very Easy"


def add_1(num: Number) -> Number:  # This any type exists or what?
    """
    Returns the next number(n+1)from the integer passed.
    """
    if isinstance(num, Number):
        return num + 1
    else:
        raise TypeError(f"Expected a number, got {type(num)} instead.") # Will it be proper to implement this, halting program?


if __name__ == "__main__":
    # Printing Meta data.
    print(f"Author: {__author__}")
    print(f"Version: {__version__}")
    print(f"Difficulty: {__difficulty__}")
    print(f"Function Documentation: {add_1.__doc__}")
    print(f"Date: {__date__}")

    print()  # Black line for better readability.

    # Test cases.
    print(add_1(0))
    print(add_1(9))
    print(add_1(-3))

    # Extras
    # print(add_1("256"))
    # print(add_1("abcd"))


# See, whether raising a error is good or not.

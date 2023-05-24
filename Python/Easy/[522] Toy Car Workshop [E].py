"""
##Toy Car Workshop

You work in a toy car workshop, and your job is to build toy cars from a collection of parts.
Each toy car needs 4 wheels, 1 car body, and 2 figures of people to be placed inside.
Given the total number of wheels, car bodies and figures available, how many complete toy cars can you make?


[Examples]

___
cars(2, 48, 76) ➞ 0
# 2 wheels, 48 car bodies, 76 figures

cars(43, 15, 87) ➞ 10

cars(88, 37, 17) ➞ 8
_____



[Notes]

N/A


[math] 



-------------------------------------------------------------------
[Resources]
_________
What does floor division ("//") in Python do?
https://www.quora.com/What-does-floor-division-in-Python-do
There are two types of division operations in python. Ordinary division, with / operator Floor division, with // operator.
_________
_________
min() Method
https://www.programiz.com/python-programming/methods/built-in/min
Returns the smallest element in an iterable or smallest of two or more parameters.
_________
_________
Division Operators in Python
https://www.geeksforgeeks.org/division-operator-in-python/
First output is fine, but the second one may be surprising if we are coming Java/C++ world. In Python 2.7, the “/” operator works as a floor division for integer argume …
_________
_________
min() Function
https://www.w3schools.com/python/ref_func_min.asp
Returns the item with the lowest value, or the item with the lowest value in an iterable.
_________
""" 
# Your code should go here:

def cars(wheels, bodies, figures):
    if wheels >= 4 and bodies >= 1 and figures >=2:
        modWheels = wheels % 4
        modBodies = bodies % 1
        modFigures = figures % 2

        availWheels = wheels - modWheels
        availBodies = bodies - modBodies
        availFigures = figures - modFigures

        carWheels = availWheels / 4
        carBodies = availBodies / 1
        carFigures = availFigures / 2

        outputAns = [carWheels, carBodies, carFigures]
        return outputAns.min()  # Does list does not have min? method?
    else:
        return 0

# What is floor?
# What is ceiling?
# WHat is floor division?

print(cars(2, 48, 76)) # ➞ 0
# 2 wheels, 48 car bodies, 76 figures

print(cars(43, 15, 87)) # ➞ 10

print(cars(88, 37, 17)) # ➞ 8



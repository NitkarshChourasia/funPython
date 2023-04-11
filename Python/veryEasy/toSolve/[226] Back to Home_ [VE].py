"""
##Back to Home?

Nitkarsh has started his journey from home. Given a string of directions (N=North, W=West, S=South, E=East),
he will walk for one minute in each direction. Determine whether a set of directions will lead him back to the starting position or not.


[Examples]

___
back_to_home("EEWE") ➞ False

back_to_home("NENESSWW") ➞ True

back_to_home("NEESSW") ➞ False
_____



[Notes]

N/A


[arrays] [logic] [strings] [validation]



-------------------------------------------------------------------
[Resources]
_________
Conditions and If Statements
https://www.w3schools.com/python/python_conditions.asp
Python supports the usual logical conditions from mathematics. These conditions can be used in several ways, most commonly in "if statements" and loops. An "if stateme …
_________
_________
Python Strings
https://www.w3schools.com/python/python_strings.asp
Strings in python are surrounded by either single quotation marks, or double quotation marks. 'hello' is the same as "hello".
_________
_________
Python Operators
https://www.w3schools.com/python/python_operators.asp
Operators are used to perform operations on variables and values. In the example below, we use the + operator to add together two values.
_________
_________
Python String count()
https://www.programiz.com/python-programming/methods/string/count
The string count() method returns the number of occurrences of a substring in the given string.
_________
"""
# Your code should go here:


def backToHome(str1):
    eastCount = (str1.lower()).count(e)
    westCount = (str1.lower()).count(w)
    southCount = (str1.lower()).count(s)
    northCount = (str1.lower()).count(n)
    if eastCount == westCount and northCount == southCount:
        return True
    else:
        return False

print(backToHome("EEWE")) # ➞ False
print(backToHome("NENESSWW")) # ➞ True
print(backToHome("NEESSW")) # ➞ False


# testing.

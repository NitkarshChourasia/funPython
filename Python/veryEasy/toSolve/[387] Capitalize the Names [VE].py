"""
##Capitalize the Names

Create a function that takes a list of names and returns a list where only the first letter of each name is capitalized.


[Examples]

___
cap_me(["mavis", "senaida", "letty"]) ➞ ["Mavis", "Senaida", "Letty"]

cap_me(["samuel", "MABELLE", "letitia", "meridith"]) ➞ ["Samuel", "Mabelle", "Letitia", "Meridith"]

cap_me(["Slyvia", "Kristal", "Sharilyn", "Calista"]) ➞ ["Slyvia", "Kristal", "Sharilyn", "Calista"]
_____



[Notes]

___
*) Don't change the order of the original list.
*) Notice in the second example above, "MABELLE" is returned as "Mabelle".
___



[arrays] [formatting] [loops]



-------------------------------------------------------------------
[Resources]
_________
capitalize() Method
https://www.tutorialspoint.com/python/string_capitalize.htm
Python String capitalize() Method - Learning Python in simple and easy steps : A beginner's tutorial containing complete knowledge of Python Syntax Object Oriented Lang …
_________
_________
title() Method
https://www.tutorialspoint.com/python/string_title.htm
Returns a copy of the string in which first characters of all the words are capitalized.
_________
_________
Understanding List Comprehensions in Python
https://www.digitalocean.com/community/tutorials/understanding-list-comprehensions-in-python-3
List comprehensions offer a succinct way to create lists based on existing lists. In this tutorial, we will cover the syntax of list comprehension, which will be an imp …
_________
"""
# Your code should go here:


# How to know on which data type the methods works on?
# What is the difference between function and method?


def capMe(lst1):
    outputAns = []
    for i in lst1:
        i = i.lower()
        # will i.lower() as on a single line will perform the same way as of line 60?
        outputAns.append(i.title())
    return outputAns


print(capMe(["mavis", "senaida", "letty"])) # ➞ ["Mavis", "Senaida", "Letty"]
print(capMe(["samuel", "MABELLE", "letitia", "meridith"])) # ➞ ["Samuel", "Mabelle", "Letitia", "Meridith"]
print(capMe(["Slyvia", "Kristal", "Sharilyn", "Calista"])) # ➞ ["Slyvia", "Kristal", "Sharilyn", "Calista"]

# testing.

# checkAgain.
# checkAgain. The last link of resource is fantastic.

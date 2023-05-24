"""
##Automorphic Numbers

A number n is automorphic if n^2 ends in n.
For example: n=5, n^2=25
Create a function that takes a number and returns True if the number is automorphic, False if it isn't.


[Examples]

___
is_automorphic(5) ➞ True

is_automorphic(8) ➞ False

is_automorphic(76) ➞ True
_____



[Notes]

N/A


[algebra] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
endswith() Method
https://www.programiz.com/python-programming/methods/string/endswith
Returns True if a string ends with the specified suffix. If not, it returns False.
_________
_________
Python Program to Check Automorphic (Cyclic) Number
https://www.codesansar.com/python-programming-examples/check-automorphic-cyclic-number.htm
This python program checks whether a given number by user is Automorphic (Cyclic) Number or not.
A number is called Automorphic or Cyclic number if and only if its squa …
_________
""" 
# Your code should go here:

def autoMorphic(n):
    squared = n ** 2
    lst1 = int(x) for x in str(squared)
    if lst1[-1] == n:
        return True
    elif lst1[-1] != n:
        return False


print(isAutomorphic(5)) # ➞ True

print(isAutomorphic(8)) # ➞ False

print(isAutomorphic(76)) # ➞ True


# testing.
# checkResources.



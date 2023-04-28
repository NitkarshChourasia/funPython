"""
##Valid Zip Code

Zip codes consist of 5 consecutive digits. Given a string,
write a function to determine whether the input is a valid zip code. A valid zip code is as follows:
___
*) Must only contain numbers (no non-digits allowed).
*) Must not contain any spaces.
*) Must not be greater than 5 digits in length.
___



[Examples]

___
is_valid("59001") ➞ True

is_valid("853a7") ➞ False

is_valid("732 32") ➞ False
_____



[Notes]

N/A


[regex] [strings] [validation]



-------------------------------------------------------------------
[Resources]
_________
isdigit() Method
https://www.programiz.com/python-programming/methods/string/isdigit
Returns True if all characters in a string are digits. If not, it returns False.
_________
_________
Logical Operators
https://www.programiz.com/python-programming/operators/1#logical
Logical operators are the and, or, not operators.
_________
_________
isnumeric() Method
https://www.programiz.com/python-programming/methods/string/isnumeric
Returns True if all characters in a string are numeric characters. If not, it returns False.
_________
"""
# Your code should go here:


def isValidZipCode(strInput1):
    convert2Int = int(strInput1)
    if convert2Int.len() <= 5 and " " not in convert2Int and convert2Int.isnumeric():
        return True
    else:
        return False



print(isValidZipCode("59001")) # ➞ True

print(isValidZipCode("853a7")) # ➞ False

print(isValidZipCode("732 32")) # ➞ False


# testing.

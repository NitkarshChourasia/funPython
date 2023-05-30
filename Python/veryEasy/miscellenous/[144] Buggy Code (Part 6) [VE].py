"""
##Buggy Code (Part 6)

Nitkarsh wants to remove numbers from a given string!
Help him by fixing the code in the code tab to pass this challenge. Look at the examples below to get an idea of what the function should do.


[Examples]

___
remove_numbers("Nitkarsh1") ➞ "Nitkarsh"

remove_numbers("12ma23tt") ➞ "matt"

removeNumbers("N4444442i23tk2424a243rs234h") -> "Nitkrarsh"
_____



[Notes]

___
*) READ EVERY WORD CAREFULLY, CHARACTER BY CHARACTER!
*) Don't overthink this challenge; it's not supposed to be hard.
___



[bugs] [formatting] [interview] [strings]



-------------------------------------------------------------------
[Resources]
_________
isalpha() Method
https://www.w3schools.com/python/ref_string_isalpha.asp
Returns True if all the characters are alphabet letters (a-z).
_________
_________
isdigit() Method
https://www.w3schools.com/python/ref_string_isdigit.asp
Returns True if all the characters are digits, otherwise False.
_________
_________
join() Method
https://www.w3schools.com/python/ref_string_join.asp
Join all items in a tuple into a string, using a desired character as separator.
_________
_________
isnumeric() Method
https://www.w3schools.com/python/ref_string_isnumeric.asp
Checks if a string is made of numeric values.
_________
"""
# Your code should go here:


def removeNumbers(str1):
    onlyNum = []
    onlyStr = []
    for i in str1:
        if i == isinstance(numType):
            onlyNum.append(i)
        else:
            onlyStr.append(i)


print(removeNumbers("Nitkarsh1"))
print(removeNumbers("12ma23tt"))
print(removeNumbers("N4444442i23tk2424a243rs234h"))

# testing.

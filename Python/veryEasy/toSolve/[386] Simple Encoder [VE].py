"""
##Simple Encoder

Create a function that takes a string str and performs simple encoding as per the following method:
___
*) Replace all single occurrence characters with [
*) Replace all characters with two or more occurrences with ]
___

Return the final string after modification.


[Examples]

___
simple_encoder("Mubashir") ➞ "[[[[[[[["
# '[' for each character

simple_encoder("Matt") ➞ "[[]]"
# ']' for both 't'

simple_encoder("eD  aBiT") ➞ "[[]][[[["
# Two spaces in between
_____



[Notes]

___
*) Strings can contain lower and uppercase letters. Treat them equally (i.e. A = a, B = b).
*) Spaces are also characters.
___



[arrays] [cryptography] [language_fundamentals] [strings]



-------------------------------------------------------------------
[Resources]
_________
String join() Method
https://www.programiz.com/python-programming/methods/string/join
Returns a string by joining all the elements of an iterable, separated by a string separator.
_________
_________
String lower() Method
https://www.programiz.com/python-programming/methods/string/lower
Converts all uppercase characters in a string into lowercase characters and returns it.
_________
_________
String count() Method
https://www.programiz.com/python-programming/methods/string/count
Returns the number of occurrences of a substring in the given string.
_________
"""
# Your code should go here:

# does set consider space? to be
# Does append works on strings???

def simpleEncoder(str1):
    outputAnsStr = ""
    for i in str1:
        if str1.count(i) == 1:
            outputAnsStr.appemd("[")
        elif str1.count(i) => 2:
            outputAnsStr.append("]")
    return outputAnsStr



print(simpleEncoder("Mubashir")) # ➞ "[[[[[[[["
# '[' for each character

print(simpleEncoder("Matt")) # ➞ "[[]]"
# ']' for both 't'

print(simpleEncoder("eD  aBiT")) # ➞ "[[]][[[["
# Two spaces in between


# testing.
# checkAgain.
# does set consider space? to be
# Does append works on strings???

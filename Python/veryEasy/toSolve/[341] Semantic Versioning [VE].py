"""
##Semantic Versioning

In semantic versioning a piece of software can be represented in a format like this example: 6.1.9.

Create three separate functions, one to retrieve each element in the semantic versioning specification.


[Examples]

___
# 6.1.9
retrieve_major("6.1.9") ➞ "6"

retrieve_minor("6.1.9") ➞ "1"

retrieve_patch("6.1.9") ➞ "9"

# 2.1.0
retrieve_major("2.1.0") ➞ "2"

retrieve_minor("2.1.0") ➞ "1"

retrieve_patch("2.1.0") ➞ "0"
_____



[Notes]

N/A


[formatting] [strings]



-------------------------------------------------------------------
[Resources]
_________
split() Method
https://www.w3schools.com/python/ref_string_split.asp
Splits a string into a list.
_________
_________
str.split()
https://devdocs.io/python~3.7/library/stdtypes#str.split
Return a list of the chars/words in a string, using sep as the delimiter string.
_________
"""
# Your code should go here:


def retrieveMajor(input1):
    return input1.split()

def retrieveMinor(input1):
    return input1.split()

def retrievePatch(input1):
    return input1.split()



# 6.1.9
print(retrieveMajor("6.1.9")) # ➞ "6"

print(retrieveMinor("6.1.9")) # ➞ "1"

print(retrievePatch("6.1.9")) # ➞ "9"

# 2.1.0
print(retrieveMajor("2.1.0")) # ➞ "2"

print(retrieveMinor("2.1.0")) # ➞ "1"

print(retrievePatch("2.1.0")) # ➞ "0"


# incomplete.

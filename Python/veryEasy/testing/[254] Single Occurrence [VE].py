"""
##Single Occurrence

Create a function that, given a string txt,
finds a letter that has a single occurrence.
Return the letter in uppercase. If the input is empty, return an empty string "".


[Examples]

___
single_occurrence("EFFEAABbc") ➞ "C"

single_occurrence("AAAAVNNNNSS") ➞ "V"

single_occurrence("S") ➞ "S"
_____



[Notes]

The function will not be case sensitive.


[language_fundamentals] [strings]



-------------------------------------------------------------------
[Resources]
_________
String count() Method
https://www.programiz.com/python-programming/methods/string/count
Returns the number of occurrences of a substring in the given string.
_________
_________
count() Function
https://www.geeksforgeeks.org/python-list-function-count/
Is an inbuilt function in Python that returns count of how many times a given object occurs in list.
_________
_________
String upper() Method
https://www.geeksforgeeks.org/python-string-upper/
Converts all lowercase characters in a string into uppercase characters and returns it.
_________
"""
# Your code should go here:


def singleOccurrence(str1):
    elementFindList = []
    for i in str1:
        if str1.count(i) == 1:
            elementFindList.append(i)
    if str1.len() == 0:
        return ""
    else:
        return string(elementFindList)

print(singleOccurrence("EFFEAABbc")) # ➞ "C"
print(singleOccurrence("AAAAVNNNNSS")) # ➞ "V"
print(singleOccurrence("S")) #  ➞ "S"


# testing.

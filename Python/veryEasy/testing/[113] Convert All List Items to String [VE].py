"""
##Convert All List Items to String

Create a function that takes a list of integers and strings. Convert integers to strings and return the new list.


[Examples]

___
parse_list([1, 2, "a", "b"]) ➞ ["1", "2", "a", "b"]

parse_list(["abc", 123, "def", 456]) ➞ ["abc", "123", "def", "456"]

parse_list([1, 2, 3, 17, 24, 3, "a", "123b"]) ➞ ["1", "2", "3", "17", "24", "3", "a", "123b"]

parse_list([]) ➞ []
_____



[Notes]

N/A


[arrays] [language_fundamentals]



-------------------------------------------------------------------
[Resources]
_________
Convert List of Integer to List of String
https://www.geeksforgeeks.org/python-program-to-convert-list-of-integer-to-list-of-string/
Short code on how to convert list of integers into strings.
_________
_________
List Comprehension
https://www.programiz.com/python-programming/list-comprehension
Can utilize conditional statement to modify existing list (or other tuples). We will create list that uses mathematical operators, integers, and range().
_________
_________
str() Function
https://www.programiz.com/python-programming/methods/built-in/str
Returns the string version of the given object.
_________
_________
map() Function
https://www.programiz.com/python-programming/methods/built-in/map
Applies a given function to each item of an iterable (list, tuple etc.) and returns a list of the results.
_________
"""
# Your code should go here:

pseudo algorithm:
    tempList = []
    for i in list1:
        if i == numtype:
            then tempList.append[str(i)]
        then list1.append(tempList)
        # but the error is it won't keep the order same.


pseudo algorithm "2":
    tempList = []
    for i in list1:
        if i == numType:
            then tempList.append(str(i))
        else:
            tempList.append(i)
        list1 = tempList
        return list1


pseudo algorithm "3":
    tempList = []
    for i in list1:
        tempList.append(str(i))
    list1 = tempList
    return list1

# The best algorithm is this one, and second one too is good.
# parse means?

def parseList(list1):
    tempList = []
    for i in list1:
        tempList.append(str(i))
    list1 = tempList
    return list1



print(parseList([1, 2, "a", "b"]))
print(parseList(["abc", 123, "def", 456]))
print(parseList([1, 2, 3, 17, 24, 3, "a", "123b"]))
print(parseList([]))


# testing.
# try otherWay, the second one.

"""
##State Names and Abbreviations

Create a function that filters out a list of state names into two categories based on the second parameter.



[Examples]

___
filter_state_names(["Arizona", "CA", "NY", "Nevada"], "abb")
➞ ["CA", "NY"]

filter_state_names(["Arizona", "CA", "NY", "Nevada"], "full")
➞ ["Arizona", "Nevada"]

filter_state_names(["MT", "NJ", "TX", "ID", "IL"], "abb")
➞ ["MT", "NJ", "TX", "ID", "IL"]

filter_state_names(["MT", "NJ", "TX", "ID", "IL"], "full")
➞ []
_____



[Notes]

State abbreviations will always be in uppercase.


[arrays] [formatting] [loops]



-------------------------------------------------------------------
[Resources]
_________
filter() Method
https://www.programiz.com/python-programming/methods/built-in/filter
Constructs an iterator from elements of an iterable for which a function returns True.
_________
_________
String isupper() Method
https://www.programiz.com/python-programming/methods/string/isupper
Returns whether or not all characters in a string are uppercased or not.
_________
_________
len() Method
https://www.programiz.com/python-programming/methods/built-in/len
Returns the number of items (length) in an object.
_________
"""
# Your code should go here:


def filterStateNames(lst1, toOutput):
    toOutputLowered = toOutput.lower()
    abbLst1 = []
    fullLst1 = []
    for i in lst1:
        if i.isUpper():
            abbLst1.append(i)
        else:
            fullLst1.append(i)
    if toOutputLowered == "abb":
        return abbLst1
    elif toOutputLowered == "fullLst1":
        return fullLst1



print(filterStateNames(["Arizona", "CA", "NY", "Nevada"], "abb"))
# ➞ ["CA", "NY"]

print(filterStateNames(["Arizona", "CA", "NY", "Nevada"], "full"))
# ➞ ["Arizona", "Nevada"]

print(filterStateNames(["MT", "NJ", "TX", "ID", "IL"], "abb"))
# ➞ ["MT", "NJ", "TX", "ID", "IL"]

print(filterStateNames(["MT", "NJ", "TX", "ID", "IL"], "full"))


# testing.
# checkAgain.
# checkAgain. Especially the filter method.
# ➞ []

"""
##True Ones, False Zeros

Create a function which returns a list of booleans, from a given number.
Iterating through the number one digit at a time, append True if the digit is 1 and False if it is 0.


[Examples]

___
integer_boolean("100101") ➞ [True, False, False, True, False, True]

integer_boolean("10") ➞ [True, False]

integer_boolean("001") ➞ [False, False, True]
_____



[Notes]

Expect numbers with 0 and 1 only.


[arrays] [data_structures] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Convert number to list of integers
https://www.geeksforgeeks.org/python-convert-number-to-list-of-integers/
List comprehension can be used as a shorthand to the longer format of naive method. In this method, we convert the number to string and then extract its each character …
_________
_________
Python bool() Function
https://beginnersbook.com/2019/05/python-bool-function/
Converts the given value to a boolean value (True or False). If the given value is False, the bool function returns False else it returns True.
_________
""" 
# Your code should go here:

def intBool(str1):
    lst1 = [int(x) for x in str1]  # How to use list comprehension with if and else statement? checkAgain.
    i = 0
    outputLst1 = []
    while(i < lst1.len()):
        if lst1[i] == 1:
            outputLst1.append(True)
        elif lst1[i] == 0:
            outputLst1.append(False)
    return outputLst1


print(integerBoolean("100101")) # ➞ [True, False, False, True, False, True]

print(integerBoolean("10")) # ➞ [True, False]

print(integerBoolean("001")) # ➞ [False, False, True]


# testing.
# checkResources.
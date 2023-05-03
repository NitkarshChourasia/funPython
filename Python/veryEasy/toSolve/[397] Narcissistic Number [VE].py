"""
##Narcissistic Number

A Narcissistic Number is a number that is the sum of its own digits each raised to the power of the number of digits.
For example, take 153 (3 digits), which is narcisstic:
___
1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
_____

1652 (4 digits), is non-narcisstic:
___
1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
_____

Create a function which returns True or False depending upon whether the given number n is a Narcissistic number or not.


[Examples]

___
is_narcissistic(153) ➞ True

is_narcissistic(370) ➞ True

is_narcissistic(1652) ➞ False
_____



[Notes]

N/A


[language_fundamentals] [logic] [math] [numbers] [validation]



-------------------------------------------------------------------
[Resources]
_________
Narcissistic Number
https://en.wikipedia.org/wiki/Narcissistic_number
A number that is the sum of its own digits each raised to the power of the number of digits.
_________
_________
Check if a Given Number Is a Narcissistic Number or Not
https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-96.php
If you are a reader of Greek mythology, then you are probably familiar with Narcissus. He was a hunter of exceptional beauty that he died because he was unable to leave …
_________
"""
# Your code should go here:


def isNarcissistic(n):
    lst1 = list(n)
    numberOfEle = lst1.len()
    outputAns = []
    for i in lst1:
        outputAns.append(i ** numberOfEle)  # What if i use the pow lib imported from math
    sumOutputAns = outputAns.sum()
    if sumOutputAns == n:
        return True
    else:
        return False



print(isNarcissistic(153)) # ➞ True

print(isNarcissistic(370)) # ➞ True

print(isNarcissistic(1652)) # ➞ False


# testing.
# checkAgain.
# checkAgain. Check all the resources.

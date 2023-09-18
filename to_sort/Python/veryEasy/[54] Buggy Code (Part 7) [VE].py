"""
####  Buggy Code (Part 7)  ####

Nitkarsh wants to swap two given numbers!
It is not returning the right values. Can you help him fix it?
___
a = 100
b = 200
a, b = swap(a, b)
print(a, b) # Should print out "200, 100", but the function prints out "100, 100"
_____



[Examples]

___
swap(100, 200) ➞ [200, 100]

swap(44, 33) ➞ [33, 44]

swap(21, 12) ➞ [12, 21]
_____



[Notes]

N/A


[bugs] [interview] [language_fundamentals] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Swap Two Variables
https://www.programiz.com/python-programming/examples/swap-variables
In this example, you will learn to swap two variables by using a temporary variable and, without using temporary variable.
_________
_________
Swap Two Variables Using XOR
https://betterexplained.com/articles/swap-two-variables-using-xor/
Most people would swap two variables x and y using a temporary variable, like this...
_________

"""


# Your code should go here:

def swap(a, b):
    temp = b
    b = a
    a = temp
    return [a, b]


print(swap(100, 200))  # ➞ [200, 100]

print(swap(44, 33))  # ➞ [33, 44]

print(swap(21, 12))  # ➞ [12, 21]


def swap1(a, b):
    temp = a
    a = b
    b = temp
    return [a, b]


print(swap1(100, 200))  # ➞ [200, 100]

print(swap1(44, 33))  # ➞ [33, 44]

print(swap1(21, 12))  # ➞ [12, 21]

## So, the order of 'a' or 'b' doesn't matter.
# As, we can see both ways it works.

# Operator method is left to work.
# So, the problem is...
# inc.

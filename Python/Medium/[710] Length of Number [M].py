"""
####  Length of Number  ####

Create a function that takes a number num and returns its length.


[Examples]

___
number_length(10) ➞ 2

number_length(5000) ➞ 4

number_length(0) ➞ 1
_____



[Notes]

The use of the len() function is prohibited.


[numbers] 



-------------------------------------------------------------------
[Resources]
_________
Modulo Operator and Floor Division
https://blog.tecladocode.com/pythons-modulo-operator-and-floor-division/
Learn about the some less well-known operators in Python: modulo and floor division—as well as how they interact with each other and how they're related!
_________
_________
str() Function
https://www.programiz.com/python-programming/methods/built-in/str
Returns the string version of the given object. In this tutorial, we will learn about Python str() in detail with the help of examples.
_________
_________
Length of String Without len() Function
https://stackoverflow.com/questions/3992192/string-length-without-len-function
Can anyone tell me how can I get the length of a string without using the len() function or any string methods. Please anyone tell me as I'm tapping my head madly for t …
_________
_________
How Lambda function works
https://realpython.com/python-lambda/
Python lambdas are little, anonymous functions, subject to a more restrictive but more concise syntax than regular Python functions.
_________
_________
Rfind method in string object
https://www.geeksforgeeks.org/python-string-rfind-method/
Python String rfind() method returns the rightmost index of the substring if found in the given string. If not found then it returns -1.
_________

"""


# Your code should go here:

# Assuming it to take only number type as input.
def numberLength(num):
    if isinstance(num, (int, float)):
        length = 0
        for i in str(num):
            length += 1
        return length
    else:
        return "Only numeric values allowed."


# Find more ways of doing this. Please.

print(numberLength(10))  # ➞ 2

print(numberLength(5000))  # ➞ 4

print(numberLength(0))  # ➞ 1

print(numberLength(""))

print(numberLength("."))  # This do also works. Edge cases building is good.


# Method 2 using While.

def method2(num):
    length = 0
    # As for no proper vision assuming while == True as of now.
    while True:
        try:
            if num[length]:
                length += 1
        except IndexError as error:
            return length


print(method2("Hello"))

# More ways of doing this?

# r.find and all those things what are those?

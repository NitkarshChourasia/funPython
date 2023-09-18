"""
####  FizzBuzz Interview Question  ####

Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".
___
*) If the number is a multiple of 3 the output should be "Fizz".
*) If the number given is a multiple of 5, the output should be "Buzz".
*) If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
*) If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.
*) The output should always be a string even if it is not a multiple of 3 or 5.
___



[Examples]

___
fizz_buzz(3) ➞ "Fizz"

fizz_buzz(5) ➞ "Buzz"

fizz_buzz(15) ➞ "FizzBuzz"

fizz_buzz(4) ➞ "4"
_____



[Notes]

___
*) Try to be precise with how you spell things and where you put the capital letters.
*) If you get stuck on a challenge, find help in the Resources tab.
*) If you're really stuck, unlock solutions in the Solutions tab.
___



[interview] [language_fundamentals] [logic] [math] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
Ternary Operator
https://www.geeksforgeeks.org/ternary-operator-in-python/
Operators that evaluate something based on a condition being true or false. It was added to Python in version 2.5. It simply allows to test a condition in a single line …
_________
_________
Check Number is Divisible by 5 and 11
https://www.tutorialgateway.org/python-program-to-check-number-is-divisible-by-5-and-11/
Allows users to enter any integer value. Next, this Python program checks whether the given number is divisible by both 5 and 11 using If Else.
_________
_________
% modulus
https://python-reference.readthedocs.io/en/latest/docs/operators/modulus.html
Returns the decimal part (remainder) of the quotient.
_________
_________
Check Whether a Number Is Divisible by Another Number
https://www.w3resource.com/python-exercises/python-basic-exercise-147.php
Write a Python function to check whether a number is divisible by another number. Accept two integers values form the user.
_________
_________
Python String to Int
https://careerkarma.com/blog/python-string-to-int/
This website shows how to convert an integer into a string and a string to an integer
_________
_________
Python if, if...else, if...elif...else and Nested if Statement
https://www.programiz.com/python-programming/if-elif-else
In this article, you will learn to create decisions in a Python program using different forms of if..else statement.
_________
_________
Divisibility Rule
https://en.wikipedia.org/wiki/Divisibility_rule
Is a shorthand way of determining whether a given integer is divisible by a fixed divisor without performing the division, usually by examining its digits. Although the …
_________
_________
FizzBuzz
https://www.interviewbit.com/problems/fizzbuzz/
Is one of the most basic problems in the coding interview world. Try to write a small and elegant code for this problem. Given a positive integer A, return an array of …
_________
_________
How to check if a number is divisible by another number?
https://stackoverflow.com/questions/8002217/how-do-you-check-whether-a-number-is-divisible-by-another-number-python
I need to test whether each number from 1 to 1000 is a multiple of 3 or a multiple of 5. The way I thought I'd do this would be to divide the number by 3, and if the re …
_________
_________
Python program to print all the numbers divisible by 3 and 5 for a given number
https://www.tutorialspoint.com/python-program-to-print-all-the-numbers-divisible-by-3-and-5-for-a-given-number
This is a python program to print all the numbers which are divisible by 3 and 5 from a given interger N. There are numerous ways we can write this program exce ...
_________

"""


# Your code should go here:


# Method 1, also devise another methods to them so.

# def fizzBuzz(n: int) -> str:  # Should use only int or float too? I think only int is fine.
#     if isinstance(n, int):
#         match n:
#             case n % 3 == 0 and n % 5 == 0:
#                 return "FizzBuzz"
#             case n % 3 == 0:
#                 return "Fizz"
#             case n % 5 == 0:
#                 return "Buzz"
#             case _:
#                 return str(n)
#     elif not isinstance(n, int):
#         return "Invalid input type, Integers only allowed."
#
#
# print(fizzBuzz(3))  # ➞ "Fizz"
#
# print(fizzBuzz(5))  # ➞ "Buzz"
#
# print(fizzBuzz(15))  # ➞ "FizzBuzz"
#
# print(fizzBuzz(4))  # ➞ "4"


def fizzBuzz(n: int) -> str:
    if isinstance(n, int):
        if n % 3 == 0 and n % 5 == 0:
            return "FizzBuzz"
        elif n % 3 == 0:
            return "Fizz"
        elif n % 5 == 0:
            return "Buzz"
        else:
            return str(n)
    else:
        return "Invalid input type, Integers only allowed."


print(fizzBuzz(3))  # Output: Fizz
print(fizzBuzz(5))  # Output: Buzz
print(fizzBuzz(15))  # Output: FizzBuzz
print(fizzBuzz(4))  # Output: 4


def fizzBuzz(n: int) -> str:
    if isinstance(n, int):
        match n:
            case n % 3 == 0 and n % 5 == 0:
                return "FizzBuzz"
            case n % 3 == 0:
                return "Fizz"
            case n % 5 == 0:
                return "Buzz"
            case _:
                return str(n)
    else:
        return "Invalid input type. Integers only allowed."


print(fizzBuzz(3))  # Output: Fizz
print(fizzBuzz(5))  # Output: Buzz
print(fizzBuzz(15))  # Output: FizzBuzz
print(fizzBuzz(4))  # Output: 4

# How match case functions, see that please.

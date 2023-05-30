"""
##Recursion: Sum of Multiplication

Given a number, return the total sum of that number multiplied
by every number between 1 and 10. Do not use the sum() built-in function.


[Examples]

___
multi_sum(1) ➞ 55
# 1 x 1 + 1 x 2 + 1 x 3 ...... 1 x 9 + 1 x 10 = 55

multi_sum(6) ➞ 330
# 6 x 1 + 6 x 2 + 6 x 3 ...... 6 x 9 + 6 x 10 = 330

multi_sum(10) ➞ 550

multi_sum(8) ➞ 440

multi_sum(2) ➞ 110
_____



[Notes]

Use recursion to solve this challenge.


[math] [numbers] [recursion]



-------------------------------------------------------------------
[Resources]
_________
Python Recursion
https://www.programiz.com/python-programming/recursion
In this tutorial, you will learn to create a recursive function (a function that calls itself).
_________
_________
Thinking Recursively in Python
https://realpython.com/python-thinking-recursively/
Learn how to work with recursion in your Python programs by mastering concepts such as recursive functions and recursive data structures.
_________
_________
Python for Loop
https://www.programiz.com/python-programming/for-loop
In this article, you'll learn to iterate over a sequence of elements using the different variations of for loop.
_________
_________
sum() Method
https://www.programiz.com/python-programming/methods/built-in/sum
Adds the items of an iterable and returns the sum. In this tutorial, we will learn about the sum() function with the help of examples.
_________
"""
# Your code should go here:


def multiSum(n):
    i = 1
    outputAns = 0
    while True:
        outputAns = outputAns + n*i
        i = i + 1
        if i == 10:
            break
    return outputAns


print(multiSum(1)) # ➞ 55
# 1 x 1 + 1 x 2 + 1 x 3 ...... 1 x 9 + 1 x 10 = 55

print(multiSum(6)) # ➞ 330
# 6 x 1 + 6 x 2 + 6 x 3 ...... 6 x 9 + 6 x 10 = 330

print(multiSum(10)) # ➞ 550

print(multiSum(8)) # ➞ 440

print(multiSum(2)) # ➞ 110


# testing.
# checkAgain.
# checkAgain. Check the resources, randomly and see what is recursion.
# checkAgain. Also check whether the problem is solved as per recursion thing?

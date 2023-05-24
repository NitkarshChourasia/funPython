"""
##Number Split

Given a number, return a list containing the two halves of the number.
If the number is odd, make the rightmost number higher.


[Examples]

___
number_split(4) ➞ [2, 2]

number_split(10) ➞ [5, 5]

number_split(11) ➞ [5, 6]

number_split(-9) ➞ [-5, -4]
_____



[Notes]

___
*) All numbers will be integers.
*) You can expect negative numbers too.
___



[arrays] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
math.ceil() Method
https://www.w3schools.com/python/ref_math_ceil.asp
Rounds a number UP to the nearest integer, if necessary, and returns the result.
Tip: To round a number DOWN to the nearest integer, look at the math.floor() method.
_________
_________
math.floor() Method
https://www.w3schools.com/python/ref_math_floor.asp
Rounds a number DOWN to the nearest integer, if necessary, and returns the result.
Tip: To round a number UP to the nearest integer, look at the math.ceil() method.
_________
""" 
# Your code should go here:

# Do it by another efficient way reading the above thing.
def numberSplit(n):
    remaining = n % 2
    twoHalves = (n-remaining) / 2
    outputLst1 = [twoHalves, twoHalves + remaining]
    return outputLst1

def numberSplit1(n):
    if n % 2 != 0:
        return [n/2, n/2 + 1]
    else:
        return [n/2, n/2]



print(numberSplit(4)) # ➞ [2, 2]

print(numberSplit(10)) # ➞ [5, 5]

print(numberSplit(11)) # ➞ [5, 6]

print(numberSplit(-9)) # ➞ [-5, -4]
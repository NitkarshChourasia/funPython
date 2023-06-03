"""
##The Modulus Operator Function

Create a function that will work as the modulus operator % without using the modulus operator.
The modulus operator is a way to determine the remainder of a division operation.
Instead of returning the result of the division, the modulo operation returns the whole number remainder.


[Examples]

___
mod(5, 2) ➞ 1

mod(218, 5) ➞ 3

mod(6, 3) ➞ 0
_____



[Notes]

Don't use the % operator to return the results.


[functional_programming]



-------------------------------------------------------------------
[Resources]
_________
How to Find Modulus Without Using Modulus Operator
https://dyclassroom.com/programming/how-to-find-modulus-without-using-modulus-operator
It is used to find remainder, check whether a number is even or odd etc. Example: 7 % 5 = 2 Dividing 7 by 5 we get remainder 2. 4 % 2 = 0 4 is even as remainder is 0.
_________
"""
# Your code should go here:

def modWithout(num1, num2):
    a = num2
    while(True):
        a = a + num2
        if a > num1:
            break
    print(a)  # tempDebub
    if a > num1:
        answer = a - num2
    i = 0
    while(True):
        i = i + 1
        answer = answer + 1
        if answer == num1:
            break
    return (i)


print(modWithout(5, 2))
print(modWithout(218, 5))
print(modWithout(6, 3))


# testing.

"""
##Odds vs. Evens

Given an integer, return "odd" if the sum of all odd digits is greater than the sum of all even digits.
Return "even" if the sum of even digits is greater than the sum of odd digits, and "equal" if both sums are the same.


[Examples]

___
odds_vs_evens(97428) ➞ "odd"
# odd = 16 (9+7)
# even = 14 (4+2+8)

odds_vs_evens(81961) ➞ "even"
# odd = 11 (1+9+1)
# even = 14 (8+6)

odds_vs_evens(54870) ➞ "equal"
# odd = 12 (5+7)
# even = 12 (4+8+0)
_____



[Notes]

N/A


[language_fundamentals] [math] 



-------------------------------------------------------------------
[Resources]
_________
Convert Number to List of Integers
https://www.geeksforgeeks.org/python-convert-number-to-list-of-integers/
The interconversion of data types is a problem that is quite common in programming. Sometimes we need to convert a single number to list of integers and we don’t wish t …
_________
_________
Using Python to Check for Odd or Even Numbers
https://www.pythoncentral.io/using-python-to-check-for-odd-or-even-numbers/
It's pretty easy to use Python to perform calculations and arithmetic. One cool type of arithmetic that Python can perform is to calculate the remainder of one number d …
_________
""" 
# Your code should go here:

def oddVsEven(int1 : int) -> str:
    oddLst1 : list
    evenLst1 : list
    intLst1 = [int(x) for x in str(int1)]
    i = 0
    while(i < str(int1).len()):
        if intLst1[i] % 2 == 0:
            evenLst1.append(intLst1[i])
        elif intLst1[i] % 2 == 1:
            oddLst1.append((intLst1[i]))
        i = i + 1
    if evenLst1.sum() > oddLst1.sum():
        return "Even."
    elif oddLst1.sum() > evenLst1.sum():
        return "Odd."
    elif oddLst1.sum() == evenLst1.sum():
        return "Equal."

print(oddVsEvens(97428)) # ➞ "odd"
# odd = 16 (9+7)
# even = 14 (4+2+8)

print(oddVsEvens(81961)) # ➞ "even"
# odd = 11 (1+9+1)
# even = 14 (8+6)

print(oddVsEvens(54870)) # ➞ "equal"
# odd = 12 (5+7)
# even = 12 (4+8+0)

# testing.
# checkResources.
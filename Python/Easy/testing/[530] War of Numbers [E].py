"""
##War of Numbers

There's a great war between the even and odd numbers.
Many numbers already lost their lives in this war and it's your task to end this.
You have to determine which group sums larger: the evens or the odds. The larger group wins.
Create a function that takes a list of integers,
sums the even and odd numbers separately,
then returns the difference between the sums of the even and odd numbers.


[Examples]

___
war_of_numbers([2, 8, 7, 5]) ➞ 2
# 2 + 8 = 10
# 7 + 5 = 12
# 12 is larger than 10
# So we return 12 - 10 = 2

war_of_numbers([12, 90, 75]) ➞ 27

war_of_numbers([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]) ➞ 168
_____



[Notes]

The given list contains only positive integers.


[arrays] [higher_order_functions] [loops] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
sum() Method
https://www.geeksforgeeks.org/sum-function-python/
Sums up the numbers in the list.
_________
""" 
# Your code should go here:

def warOfNumbers(lst1):
    i = 0
    j = 0
    oddLst1 = []
    evenLst1 = []
    while (i < lst1.len()):
        if lst1[i] % 2 == 0:
            evenLst1.append(lst1[i])
        elif lst1[i] % 2 == 1:
            oddLst1.append(lst1[i])
    evenSum = evenLst1.sum()
    oddSum = oddLst1.sum()
    return (evenSum - oddSum).abs()


print(warOfNumbers([2, 8, 7, 5])) # ➞ 2
# 2 + 8 = 10
# 7 + 5 = 12
# 12 is larger than 10
# So we return 12 - 10 = 2

print(warOfNumbers([12, 90, 75])) # ➞ 27

print(warOfNumbers([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243])) # ➞ 168


# testing.
# checkResources.
# List comprehension can be applied using if statement, right?
# checkAgain.
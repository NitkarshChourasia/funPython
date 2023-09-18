"""
####  Sum of Odd and Even Numbers  ####

Write a function that takes a list of numbers and returns a list with two elements:



[Example]

___
sum_odd_and_even([1, 2, 3, 4, 5, 6]) ➞ [12, 9]
# 2 + 4 + 6 = 12 and 1 + 3 + 5 = 9

sum_odd_and_even([-1, -2, -3, -4, -5, -6]) ➞ [-12, -9])

sum_odd_and_even([0, 0]) ➞ [0, 0])
_____



[Notes]

Count 0 as an even number.


[arrays] [data_structures] [higher_order_functions] [math] 



-------------------------------------------------------------------
[Resources]
_________
sum() Function
https://www.w3schools.com/python/ref_func_sum.asp#:~:text=The%20sum()%20function%20returns,all%20items%20in%20an%20iterable.
Returns a number, the sum of all items in an iterable.
_________

"""


# Your code should go here:

def sumOddAndEven(lst1):
    evenLst = [ele % 2 == 0 for ele in lst1]
    oddLst = [ele % 2 != 0 for ele in lst1]
    print(evenLst)
    print(oddLst)

    # There are two ways of doing this, one is by list comprehension method.
    # Another way of doing this is by lambda method.
    # Another way of doing this is by append method in to the list.
    # Another way of doing this is by add method in to the list.


print(sumOddAndEven([1, 2, 3, 4, 5, 6]))  # ➞ [12, 9]
# 2 + 4 + 6 = 12 and 1 + 3 + 5 = 9

print(sumOddAndEven([-1, -2, -3, -4, -5, -6]))  # ➞ [-12, -9])

print(sumOddAndEven([0, 0]))  # ➞ [0, 0])

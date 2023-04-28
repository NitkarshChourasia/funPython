"""
##Smaller String Number

Create a function that returns the smaller number.


[Examples]

___
smaller_num("21", "44") ➞ "21"

smaller_num("1500", "1") ➞ "1"

smaller_num("5", "5") ➞ "5"
_____



[Notes]

___
*) Numbers will be represented as strings, and your output should also be a string.
*) If both numbers tie, return either number.
*) Numbers will be positive.
*) Bonus: See if you can do this without converting to integers.
___



[language_fundamentals] [strings]



-------------------------------------------------------------------
[Resources]
_________
Sorted() Function in Python
https://www.geeksforgeeks.org/sorted-function-python/
Sorts any sequence (list, tuple) and always returns a list with the elements in sorted manner, without modifying the original sequence.
_________
_________
Number min() Method
https://www.tutorialspoint.com/python/number_min.htm
Returns the smallest of its arguments: the value closest to negative infinity.
_________
"""
# Your code should go here:



def smallerNum0(strInput1, strInput2):
    if strInput1 < strInput2:
        return strInput1
    elif strInput2 < strInput1:
        return strInput2
    elif strInput2 == strInput1:
        return strInput1


print(smallerNum("21", "44")) # ➞ "21"

print(smallerNum("1500", "1")) # ➞ "1"

print(smallerNum("5", "5")) # ➞ "5"


# testing.

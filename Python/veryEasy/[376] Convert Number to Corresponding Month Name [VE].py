"""
##Convert Number to Corresponding Month Name

Create a function that takes a number (from 1 to 12) and returns its corresponding month name as a string.
For example, if you're given 3 as input, your function should return "March", because March is the 3rd month.



[Examples]

___
month_name(3) ➞ "March"

month_name(12) ➞ "December"

month_name(6) ➞ "June"
_____



[Notes]

___
*) You can expect only integers ranging from 1 to 12 as test input.
*) If you get stuck on a challenge, find help in the Resources tab.
*) If you're really stuck, unlock solutions in the Solutions tab.
___



[arrays] [conditions] [dates] [formatting]



-------------------------------------------------------------------
[Resources]
_________
calendar.month_name
https://docs.python.org/3/library/calendar.html#calendar.month_name
An array that represents the months of the year in the current locale. This follows normal convention of January being month number 1, so it has a length of 13 and mont …
_________
_________
Dictionaries
https://docs.python.org/3/tutorial/datastructures.html#dictionaries
Another useful data type built into Python is the dictionary (see Mapping Types — dict). Dictionaries are sometimes found in other languages as “associative memories” o …
_________
_________
Two Simple Ways to Implement Python Switch Case Statement
https://data-flair.training/blogs/python-switch-case/
Unlike other languages like Java Programming Langauge and C++, Python does not have a switch-case construct. Along with this, we will see how to work a loophole for Pyt …
_________
"""
# Your code should go here:


def monthName(n):
    monthNameStr1 = "January, February, March, April, May, June, July, Auguest, September, October, November, December"
    monthNameLst1 = monthNameStr1.split(",")
    # Some how convert it into list using split or whatever join function.
    return monthNameLst1[n-1]


print(monthName(3)) # ➞ "March"

print(monthName(12)) # ➞ "December"

print(monthName(6)) # ➞ "June"


# the question is how to do it for 100 numbers of items?


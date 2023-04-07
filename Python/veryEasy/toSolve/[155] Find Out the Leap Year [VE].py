"""
##Find Out the Leap Year

A leap year happens every four years, so it's a year that is perfectly divisible by four.
However, if the year is a multiple of 100 (1800, 1900, etc), the year must be divisible by 400.
Write a function that determines if the year is a leap year or not.


[Examples]

___
leap_year(2020) ➞ True

leap_year(2021) ➞ False

leap_year(1968) ➞ True
_____



[Notes]

N/A


[algebra] [algorithms] [validation]



-------------------------------------------------------------------
[Resources]
_________
Leap Year
https://en.wikipedia.org/wiki/Leap_year
A calendar year that contains an additional day (or, in the case of a lunisolar calendar, a month) added to keep the calendar year synchronized with the astronomical ye …
_________
"""
# Your code should go here:



def leapYear(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    if year % 4 == 0:
        return True
    else:
        return False


print(leapYear(2020))
print(leapYear(2021))
print(leapYear(1968))

# testing.
# checkAgain.
# checkAgain the program using something chatGpt or anything.

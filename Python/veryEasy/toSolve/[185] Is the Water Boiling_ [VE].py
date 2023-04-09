"""
##Is the Water Boiling?

Create a function that determines if the temp of the water is considered boiling or not. temp will be measured in Fahrenheit and Celsius.


[Examples]

___
is_boiling("212F") ➞ True

is_boiling("100C") ➞ True

is_boiling("0F") ➞ False
_____



[Notes]

The boiling point of water is 212F in Fahrenheit and 100C in Celsius.


[conditions] [strings] [validation]



-------------------------------------------------------------------
[Resources]
_________
If ... Else
https://www.w3schools.com/python/python_conditions.asp
Python supports the usual logical conditions from mathematics: Equals: a == b Not Equals: a != b Less than: a < b Less than or equal to: a <= b Greater than: a > b Gre …
_________
"""
# Your code should go here:


def isBoiling(tempInput):
    tempInput = tempInput.lower()
    lst1 = list(tempInput)
    if lst1[-1] == "f" or lst1[-1] == "c":
        if "f" in tempInput:
            if "212" in tempInput:
                return True
        elif "c" in tempInput:
            if "100" in tempInput:
                return True
        else:
            return False
    else:
        return "Please add the temperature in correct unit format."


print(isBoiling("212F"))
print(isBoiling("100C"))
print(isBoiling("0F"))


# testing.

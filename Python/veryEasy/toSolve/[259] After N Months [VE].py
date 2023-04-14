"""
##After N Months...

Create a function that takes in year and month as input, then return what year it would be after n-months have elapsed.


[Examples]

___
after_n_months(2020, 24) ➞ 2022

after_n_months(1832, 2) ➞ 1832

after_n_months(1444, 60) ➞ 1449
_____



[Notes]

___
*) Assume that adding 12 months will always increment the year by 1.
*) If no value is given for year or months, return "year missing" or "month missing".
*) At least one value will be present.
___



[dates] [math] [numbers]



-------------------------------------------------------------------
[Resources]
_________
Python If Statement
https://www.w3schools.com/python/gloss_python_if_statement.asp
An "if statement" is written by using the if keyword.
_________
_________
Number floor() Method
https://www.tutorialspoint.com/python/number_floor.htm
Returns floor of x - the largest integer not greater than x. Following is the syntax for floor() method.
_________
_________
Python Operators
https://www.w3schools.com/python/python_operators.asp
Used to perform operations on variables and values.
_________
_________
Is your variable equal to None?
https://stackoverflow.com/questions/23086383/how-to-test-nonetype-in-python/23086405#23086405
Use is operator, like this if variable is None: Why this works? Since None is the sole singleton object of NoneType in Python, we can use is operator to check if a vari …
_________
_________
Lambda Function
https://www.w3schools.com/python/python_lambda.asp
Is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression.
_________
"""
# Your code should go here:


def afterNMonths(year, months):
    if year.len() == 0 and months.len() == 0:
        return "Year and month missing."
    elif year.len() == 0:
        return "Year missing."
    elif months.len() == 0:
        return "Month missing."
    if year.len() > 0 and months.len() > 0:
        if months >= 12:
            addingMonths = months/12
            return year + addingMonths
        elif months < 12:
            return year


print(afterNMonths(2020, 24)) # ➞ 2022
print(afterNMonths(1832, 2)) # ➞ 1832
print(afterNMonths(1444, 60)) # ➞ 1449


# testing.

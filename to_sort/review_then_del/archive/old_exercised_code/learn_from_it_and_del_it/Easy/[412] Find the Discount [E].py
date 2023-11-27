"""
####  Find the Discount  ####

Create a function that takes two arguments: the original price and the
discount percentage as integers and returns the final price after the discount.



[Examples]

___
calculated_discounted_price(1500, 50) ➞ 750

calculated_discounted_price(89, 20) ➞ 71.2

calculated_discounted_price(100, 75) ➞ 25
_____



[Notes]

Your answer should be rounded to two decimal places.


[math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
round() Function
https://www.programiz.com/python-programming/methods/built-in/round
Returns a floating-point number rounded to the specified number of decimals.
In this tutorial, we will learn about Python round() in detail with the help of examples.
_________
_________
Discount Calculator
https://www.calculator.net/discount-calculator.html?pricebefore=700&discount=10&priceafter=&savedamount=&format=p&x=92&y=31
A percent off of a price typically refers to getting some percent, say 10%,
off of the original price of the product or service. For example, if a good costs $45, with …
_________
_________
Percentages, Mathematics, and GCSE Revision
https://revisionmaths.com/gcse-maths-revision/number/percentages
Percentages GCSE Maths revision section of Revision Maths, including: definitions, examples and videos.
_________

"""


# Your code should go here:

# Restrictions:
# - Output round to 2 decimals.

# Requirements:
# -


def calculated_discounted_price(original_price, discount_percentage: float) -> float:
    # if isinstance((original_price, discountPerc), int):
    discount = original_price * (discount_percentage / 100)

    # final_price = round((original_price - discount), 2)
    final_price = original_price - discount
    final_price = round(final_price, 2)

    return final_price


print(calculated_discounted_price(1500, 50))  # ➞ 750

print(calculated_discounted_price(89, 20))  # ➞ 71.2

print(calculated_discounted_price(100, 75))  # ➞ 25

# inc.
# if after decimal it is zero then just integer, if not then float.

# is the program good?

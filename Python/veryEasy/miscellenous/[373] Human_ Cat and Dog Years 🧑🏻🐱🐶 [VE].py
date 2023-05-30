"""
##Human, Cat and Dog Years 🧑🏻🐱🐶

Mubashir has a cat and a dog. He purchased both of them at the same time human_years ago.
Create a function which takes an argument of human_years and returns [human_years, cat_years, dog_years] list.


[Human Years]

___
*) Human Years >= 1
*) Human Years are whole numbers only.
___



[Cat Years]

___
*) 15 cat years for first year.
*) +9 cat years for second year.
*) +4 cat years for each year after that.
___



[Dog Years]

___
*) 15 dog years for first year
*) +9 dog years for second year
*) +5 dog years for each year after that
___



[Examples]

___
calculate_years(1) ➞ [1, 15, 15]

calculate_years(2) ➞ [2, 24, 24]

calculate_years(10) ➞ [10, 56, 64]
_____



[Notes]

N/A


[interview] [logic] [math] [numbers]



-------------------------------------------------------------------
[Resources]
_________
How to Calculate Cat Years to Human Years
https://www.catster.com/cats-101/calculate-cat-age-in-cat-years
One cat year does not equal seven human years. Read on for tips on determining your cat’s age.
_________
_________
How do you really calculate dog years?
https://slate.com/news-and-politics/2009/05/how-do-you-calculate-dog-years.html
The official formula, according to the American Veterinary Medical Association, equates the first year of a medium-sized dog’s life to 15 years of a human’s. The dog’s …
_________
"""
# Your code should go here:

# Improve c3 to cN.
# Avoided loop for space and time complexity.
# If required next time do with loops of different kinds.

def calculateYears(n):
    d1 = 15
    d2 = 9
    dN = 5
    c1 = d1
    c2 = d2
    cN = 4
    return1N = [n, d1, c1]
    return2N = [n, d1 + d2, c1 + c2]
    returnN = [n, d1 + d2 + ((n - 2) * dN), c1 + c2 + ((n - 2) * cN)]
    if n == 0:
        return "Invalid input range."
    elif n == 1:
        return return1N
    elif n == 2:
        return return2N
    elif n >= 3:
        return returnN


print(calculateYears(1)) # ➞ [1, 15, 15]

print(calculateYears(2)) # ➞ [2, 24, 24]

print(calculateYears(10)) # ➞ [10, 56, 64]





# checkAgain.
# checkAgain. The resources, which are not known.
# testing.
# code can be improvised.
# calculator.

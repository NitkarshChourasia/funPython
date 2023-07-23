"""
####  Calculating Damage  ####

Create a function that takes damage and speed (attacks per second)
and returns the amount of damage after a given time.


[Examples]

___
damage(40, 5, "second") ➞ 200

damage(100, 1, "minute") ➞ 6000

damage(2, 100, "hour") ➞ 720000
_____



[Notes]

Return "invalid" if damage or speed is negative.


[conditions] [math] 



-------------------------------------------------------------------
[Resources]
_________
Dictionary get() Method
https://www.w3schools.com/python/ref_dictionary_get.asp
Get method in python dictionary, doesn't throw error if, key is not in dictionary.
_________
_________
index() Method
https://www.programiz.com/python-programming/methods/string/index
Returns the index of a substring inside the string (if found). If the substring is not found, it raises an exception.
_________
_________
Dictionary
https://www.programiz.com/python-programming/dictionary
In this tutorial, you'll learn everything about Python dictionaries; how they are created, accessing, adding, removing elements from them and various built-in methods.
_________

"""
import math


# Your code should go here:

def damage(perAttackDamage, speedAttackPerSec, timePeriod):
    # print("Valid time periods: second, minute, hour")
    match timePeriod:
        case "second":
            return perAttackDamage * speedAttackPerSec * 1
        case "minute":
            return perAttackDamage * speedAttackPerSec * 60
        case "hour":
            return perAttackDamage * speedAttackPerSec * int(math.pow(60, 2))
        case _:
            return "Please enter valid timePeriod."
    # Total Damage in all it returns.


print(damage(40, 5, "second"))  # ➞ 200

print(damage(100, 1, "minute"))  # ➞ 6000

print(damage(2, 100, "hour"))  # ➞ 720000

print(damage(200, 10, "day"))

# inc.
# This is meant to solve by dictionary method.
# Ask chatgpt if unsure, how to solve it using the dictionary method.


# Remember, the goal is to learn. Not showcase the number, but the quality. Indeed.

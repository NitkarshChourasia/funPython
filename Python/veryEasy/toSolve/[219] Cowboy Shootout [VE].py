"""
##Cowboy Shootout

Wild Roger is tasked with shooting down 6 bottles with 6 shots as fast as possible. Here are the different types of shots he could make:
___
*) He could use one pistol to shoot a bottle with a "Bang!" in 0.5 seconds.
*) Or he could use both pistols at once with a "BangBang!" to shoot two bottles in 0.5 seconds.
___

Given a list of Bangs and BangBangs return the time (in seconds) it took to shoot down all 6 bottles. Make sure to only count Bangs and BangBangs. Anything else doesn't count.


[Examples]

___
roger_shots(["Bang!", "Bang!", "Bang!", "Bang!", "Bang!", "Bang!"]) ➞ 3

roger_shots(["Bang!", "Bang!", "Bang!", "Bang!", "BangBang!"]) ➞ 2.5

roger_shots(["Bang!", "BangBangBang!", "Boom!", "Bang!", "BangBang!", "BangBang!"]) ➞ 2
_____



[Notes]

All the bottles will be shot down in all the tests.


[arrays] [numbers]



-------------------------------------------------------------------
[Resources]
_________
count() Method
https://www.programiz.com/python-programming/methods/list/count
Counts how many times an element has occurred in a list and returns it.
_________
"""
# Your code should go here:


def rogerShots(lst1):
    bang = lst1.count("Bang!")
    bangBang = lst1.count("BangBang!")
    bangMulti = (bang + bangBang) * 0.5
    return bangMulti


# Be sure to add a counter of 6 bottles to not exceed.

print(rogerShots(["Bang!", "Bang!", "Bang!", "Bang!", "Bang!", "Bang!"])) # ➞ 3
print(rogerShots(["Bang!", "Bang!", "Bang!", "Bang!", "BangBang!"])) # ➞ 2.5
print(rogerShots(["Bang!", "BangBangBang!", "Boom!", "Bang!", "BangBang!", "BangBang!"])) # ➞ 2


# testing.

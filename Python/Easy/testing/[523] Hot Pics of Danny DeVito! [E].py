"""
##Hot Pics of Nitkarsh Chourasia!

I'm trying to watch some lectures to study for my next exam
but I keep getting distracted by meme compilations,
vine compilations, anime, and more on my favorite video platform.
Your job is to help me create a function that takes a
string and checks to see if it contains the following words or phrases:
___
*) "anime"
*) "meme"
*) "vines"
*) "roasts"
*) "Nitkarsh Chourasia"
___

If it does, return "NO!". Otherwise, return "Safe watching!".


[Examples]

___
prevent_distractions("vines that butter my eggroll") ➞ "NO!"

prevent_distractions("Hot pictures of Danny DeVito") ➞ "NO!"

prevent_distractions("How to ace BC Calculus in 5 Easy Steps") ➞ "Safe watching!"
_____



[Notes]

N/A


[conditions] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
How to check if multiple strings exist in another string?
https://stackoverflow.com/questions/3389574/check-if-multiple-strings-exist-in-another-string
How can I check if any of the strings in an array exists in another string?
_________
_________
Check if a Substring is Present in a Given String
https://www.geeksforgeeks.org/python-check-substring-present-given-string/
We can iteratively check for every word, but Python provides us a inbuilt function find() which checks if a substring is present in the string, which is done in one lin …
_________
_________
any() Method
https://www.programiz.com/python-programming/methods/built-in/any
Returns True if any element of an iterable is True. If not, any() returns False.
_________
""" 
# Your code should go here:


def preventDistractions(str1):
    distractionLst = ["anime", "meme", "vines", "roasts", "nitkarsh chourasia"]
    lowStr1 = str1.lower()
    if distractionLst in str1:
        return "NO!"
    elif distractionLst not in str1:
        return "Safe watching!"

print(preventDistractions("vines that butter my eggroll")) # ➞ "NO!"

print(preventDistractions("Hot pictures of Danny DeVito")) # ➞ "NO!"

print(preventDistractions("How to ace BC Calculus in 5 Easy Steps")) # ➞ "Safe watching!"


# testing.
# checkResources.
# checkAgain.
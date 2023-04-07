"""
## Amazing Nitkarsh!

Create a function that takes a string and changes the word amazing to not amazing.
Return the string without any change if the word Nitkarsh is part of the string.


[Examples]

___
amazing_Nitkarsh("Nitkarsh is amazing.") ➞ "Nitkarsh is amazing."

amazing_Nitkarsh("Mubashir is amazing.") ➞ "Mubashir is not amazing."

amazing_Nitkarsh("Infinity is amazing.") ➞ "Infinity is not amazing."
_____



[Notes]

Nitkarsh is amazing :)


[regex] [strings] [validation]



-------------------------------------------------------------------
[Resources]
_________
replace() Method
https://www.w3schools.com/python/ref_string_replace.asp
Replaces a specified phrase with another specified phrase.
_________
_________
Check if String Contains Substring
https://stackabuse.com/python-check-if-string-contains-substring/
In this article, we'll examine four ways to use Python to check whether a string contains a substring. Each has their own use-cases and pros/cons, some of which we'll b …
_________
_________
Conditions
https://www.w3schools.com/python/python_conditions.asp
In this example we use two variables, a and b, which are used as part of the if statement to test whether b is greater than a. As a is 33, and b is 200, we know that …
_________
"""
# Your code should go here:


def amazingNitkarsh(str1):
    if "Nitkarsh" in str1:
        return str1
    else:
        return str1.replace("amazing", "not amazing")

print(amazingNitkarsh("Nitkarsh is amazing."))
print(amazingNitkarsh("Sadhguru is amazing."))
print(amazingNitkarsh("Acharya Prashant is amazing."))

# testing.

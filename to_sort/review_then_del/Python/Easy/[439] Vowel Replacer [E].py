"""
####  Vowel Replacer  ####

Create a function that replaces all the vowels in a string with a specified character.


[Examples]

___
replace_vowels("the aardvark", "#") ➞ "th# ##rdv#rk"

replace_vowels("minnie mouse", "?") ➞ "m?nn?? m??s?"

replace_vowels("shakespeare", "*") ➞ "sh*k*sp**r*"
_____



[Notes]

All characters will be in lower case.


[regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
String replace() Method
https://www.w3schools.com/python/ref_string_replace.asp
Replaces a specified phrase with another specified phrase.
_________
_________
Python RegEx (With Examples)
https://www.programiz.com/python-programming/regex
In this tutorial, you will learn about regular expressions (RegEx), and use Python's re module to work with RegEx (with the help of examples).
_________
_________
join() Method
https://www.programiz.com/python-programming/methods/string/join
Provides a flexible way to create strings from iterable objects. It joins each element of an iterable (such as list, string and tuple) by a string separator (the string …
_________
_________
replace() Function
https://www.programiz.com/python-programming/methods/string/replace
Enables a user to replace character(s) in a string with an alternative character(s).
_________
_________
Python regex replace strings
https://flexiple.com/python/python-regex-replace/
Regex can be used to perform various tasks in Python. It is used to do search and replace operations, replace patterns in text, and check if a string contains a specifi …
_________

"""


# Your code should go here:

def replaceVowels(theString, toRepFrom):
    # Restrictions:
    # - To check if string.
    # - To check if lowercase.

    # Checking if string only.
    if isinstance(theString, str):

        # String length.
        try:
            count = 0
            while True:
                theString[count]
                count += 1
        except IndexError:
            pass

        # Check if lowercase only.
        checkLowerOnly = [chr(ele) for ele in range(97 + 97 + 25)]
        i = 0

        while i < count:
            if theString[i] in checkLowerOnly:
                pass
            elif theString[i] not in checkLowerOnly:
                # Halt the program.
                return "Only lowercase string input is allowed."
            # Can I use assert here?
            # Instead of all this if and else statements?

        # Now the replace program starts from here.
        outputString = ""
        vowels = "aeiou"
        i = 0
        while i < count:
            if theString[i] in vowels:
                outputString += toRepFrom
            elif theString[i] not in vowels:
                outputString += theString[i]
            i += 1
        return outputString


print(replaceVowels("the aardvark", "#"))  # ➞ "th# ##rdv#rk"

print(replaceVowels("minnie mouse", "?"))  # ➞ "m?nn?? m??s?"

print(replaceVowels("shakespeare", "*"))  # ➞ "sh*k*sp**r*"

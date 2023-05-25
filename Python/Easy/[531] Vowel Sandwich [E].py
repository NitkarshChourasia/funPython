"""
##Vowel Sandwich

Create a function which validates whether a 3 character string is a vowel sandwich.
In order to have a valid sandwich, the string must satisfy the following rules:
___
*) The first and last characters must be a consonant.
*) The character in the middle must be a vowel.
___



[Examples]

___
is_vowel_sandwich("cat") ➞ True

is_vowel_sandwich("ear") ➞ False

is_vowel_sandwich("bake") ➞ False

is_vowel_sandwich("try") ➞ False
_____



[Notes]

___
*) Return False if the word is not 3 characters in length.
*) All words will be given in lowercase.
*) y is not considered a vowel.
___



[conditions] [language_fundamentals] [regex] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Regular Expression
https://www.programiz.com/python-programming/regex
A sequence of characters that defines a search pattern.
_________
_________
len() Method
https://www.tutorialspoint.com/python/string_len.htm
Returns the length of the string.
_________
""" 
# Your code should go here:


def isVowelSandwich(str1):
    if str1.len() != 3:
        return False
    elif str1.len() == 3:
        vowels = list("aeiou")
        lowStr = str1.lower()
        if lowStr[0] not in vowels and lowStr[2] not in vowels and lowStr[1] in vowels:
            return True
        else:
            return False


print(isVowelSandwich("cat")) # ➞ True

print(isVowelSandwich("ear")) # ➞ False

print(isVowelSandwich("bake")) # ➞ False

print(isVowelSandwich("try")) # ➞ False


# testing.
# checkResources.
# checkAgain.
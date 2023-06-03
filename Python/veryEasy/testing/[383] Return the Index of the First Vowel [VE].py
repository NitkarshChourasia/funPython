"""
##Return the Index of the First Vowel

Create a function that returns the index of the first vowel in a string.


[Examples]

___
first_vowel("apple") ➞ 0

first_vowel("hello") ➞ 1

first_vowel("STRAWBERRY") ➞ 3

first_vowel("pInEaPPLe") ➞ 1
_____



[Notes]

___
*) Input will be single words.
*) Characters in words will be upper or lower case.
*) "y" is not considered a vowel.
*) Input always contains a vowel.
___



[language_fundamentals] [loops] [regex] [strings]



-------------------------------------------------------------------
[Resources]
_________
Membership Test Operations
https://docs.python.org/3/reference/expressions.html#in
The operators in and not in test for membership. x in s evaluates to True if x is a member of s, and False otherwise. x not in s returns the negation of x in s. All bui …
_________
_________
index() Method
https://www.tutorialspoint.com/python/string_index.htm
Determines if string str occurs in string or in a substring of string if starting index beg and ending index end are given. This method is same as find(), but raises an …
_________
"""
# Your code should go here:

# can I produce an empty variable in python.

def firstVowel(str1):
    str1Lowr = str1.lower()
    vowels = "aeiou"
    vowelsLst1 = list(vowels)
    index1 = ""
    for i in str1:
        if vowels in i:
            index1 = str1.index(i)
        if index1.len() == 1:
            break
    return int(index1)

print(firstVowel("apple")) # ➞ 0

print(firstVowel("hello")) # ➞ 1

print(firstVowel("STRAWBERRY")) # ➞ 3

print(firstVowel("pInEaPPLe")) # ➞ 1


# testing.
# checkAgain.
# checkAgain. The resources.

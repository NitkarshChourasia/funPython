"""
##Cycling Through Strings

Given two strings, repeatedly cycle through all of the letters in the first string until it is the same length as the second string.


[Examples]

___
string_cycling("abc", "hello") ➞ "abcab"

string_cycling("programming", "edabit") ➞ "progra"

string_cycling("ha", "good morning") ➞ "hahahahahaha"
_____



[Notes]

All tests will include valid strings.


[loops] [strings]



-------------------------------------------------------------------
[Resources]
_________
How to Repeat a String
https://www.kite.com/python/answers/how-to-repeat-a-string-in-python
Repeating a string joins copies of it into a single string. For example, repeating "abc" three times results in "abcabcabc".
_________
_________
While Loops
https://www.w3schools.com/python/python_while_loops.asp
With the while loop we can execute a set of statements as long as a condition is true.
_________
_________
Conditions and if Statements
https://www.w3schools.com/python/python_conditions.asp
Python supports the usual logical conditions from mathematics. These conditions can be used in several ways, most commonly in "if statements" and loops. An "if stateme …
_________
"""
# Your code should go here:


def stringCycling(str1, str2):
    if str1.len() == str2.len():
        return str1
    elif str1.len() < str2.len():
        indexPlus = 0
        # preserve the original str1 and make it in another string.
        while(str1.len()  == str2.len()):
            str1.append(str1[indexPlus])
            indexPlus = indexPlus + 1
        return str1
    elif str1.len() > str2.len():
        # preserve the original str1 and make it in another string to be modified.
        while str1.len() == str2.len():
            str1.pop()
        return str1


print(stringCycling("abc", "hello")) # ➞ "abcab"

print(stringCycling("programming", "edabit")) # ➞ "progra"

print(stringCycling("ha", "good morning")) # ➞ "hahahahahaha"


# testing.
# checkAgain.
# checkAgain. To preserve the original string.




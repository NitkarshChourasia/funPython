"""
####  Xs and Os, Nobody Knows  ####

Create a function that takes a string, checks if it has the same number of "x"s and "o"s and returns either True or False.
___
*) Return a boolean value (True or False).
*) Return True if the amount of x's and o's are the same.
*) Return False if they aren't the same amount.
*) The string can contain any character.
*) When "x" and "o" are not in the string, return True.
___



[Examples]

___
XO("ooxx") ➞ True

XO("xooxx") ➞ False

XO("ooxXm") ➞ True
# Case insensitive.

XO("zpzpzpp") ➞ True
# Returns True if no x and o.

XO("zzoo") ➞ False
_____



[Notes]

___
*) Remember to return True if there aren't any x's or o's.
*) Must be case insensitive.
___



[conditions] [language_fundamentals] [regex] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
count() Method
https://www.programiz.com/python-programming/methods/string/count
Returns the number of occurrences of a substring in the given string.
_________
_________
How to count occurrence of a character in a string?
http://stackoverflow.com/questions/1155617/count-occurrence-of-a-character-in-a-string
What's the simplest way to count the number of occurrences of a character in a string? e.g. count the number of times "a" appears in "Mary had a little lamb"
_________
_________
lower() Method
https://www.geeksforgeeks.org/python-string-lower/
Converts all uppercase characters in a string into lowercase characters and returns it.
_________
_________
count() Method
https://www.geeksforgeeks.org/python-string-count/
Returns an integer that denotes number of times a substring occurs in a given string.
_________
_________
isupper(), islower(), lower(), upper()
https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/
isupper() is a built-in method used for string handling. The isupper() methods returns “True” if all characters in the string are uppercase, Otherwise, It returns “Fals …
_________
_________
upper() method
https://www.w3schools.com/python/ref_string_upper.asp
Returns a string where all characters are in upper case.
_________

"""


# Your code should go here:

# Restrictions:
# - input should be String.
# - Case insensitive.
# - if not any x and o return True.


def XO(theString1: str) -> bool:
    # Checking if the input is only string.
    # How to check if it is a string or not ...
    # By not using any function or method at all.
    if isinstance(theString1, str):
        # couting the length.
        count = 0
        try:
            while True:
                theString1[count]
                count += 1
        except IndexError:
            pass

        # Checking for 'o''O' and 'x''X' in the string.
        i = 0
        countoO = 0
        countxX = 0
        while i < count:
            if theString1[i] == "x" or "X":
                countxX += 1
            elif theString1[i] == "o" or "O":
                countoO += 1
            i += 1

        # if 'o' || 'O' kept on if.
        # It returns the same count as of length of the string.

        # Now when 'x' || 'X' kept on if.
        # It returns the same count as of length of the string.

        ### ASK CHATGPT ABOUT THIS.
        # Like I know where and what is the logical error in the code.
        # Or where is the error in the code.
        # But, I don't know the WHY behind it.
        # Why it is doing what it is doing?
        # Like, what is the actual reason behind it to do so???
        # Like, I want to know the blackbox of or for it.
        # Thank you.

        print(f"length: {count}")
        print(f"X in str: {countxX}")
        print(f"O in str: {countoO}")
        if countoO == countxX:
            return True
        elif countoO != countxX:
            return False


print(XO("ooxx"))  # ➞ True

print(XO("print(XOoxx"))  # ➞ False

print(XO("ooxXm"))  # ➞ True
# Case insensitive.

print(XO("zpzpzpp"))  # ➞ True
# Returns True if no x and o.

print(XO("zzoo"))  # ➞ False

# inc.
# Read if there are any other resources in it.

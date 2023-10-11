"""
####  Hiding the Card Number  ####

Write a function that takes a credit card number and only displays the last four characters.
The rest of the card number must be replaced by ************.


[Examples]

___
card_hide("1234123456785678") ➞ "************5678"

card_hide("8754456321113213") ➞ "************3213"

card_hide("35123413355523") ➞ "**********5523"
_____



[Examples]

___
*) Ensure you return a string.
*) The length of the string must remain the same as the input.
___



[formatting] [numbers] [strings] 



-------------------------------------------------------------------
[Resources]
_________
How to get the last 4 characters of a string?
https://stackoverflow.com/questions/7983820/get-the-last-4-characters-of-a-string
I have the following string: "aaaabbbb" How can I get the last four characters and store them in a string using Python?
_________
_________
String Indexing With ":"
https://stackoverflow.com/questions/4012340/colon-in-python-list-index
I'm new to Python. I see : used in list indices especially when it's associated with function calls. Python 2.7 documentation suggests that lists.append translates to …
_________
_________
How to pad strings with zero, space or some other character?
https://thispointer.com/python-how-to-pad-strings-with-zero-space-or-some-other-character/
In this article we will discuss how to do left padding of strings or right padding of strings either with zero, space or some other character. Left padding a string mea …
_________
_________
Python Strings
https://www.w3schools.com/python/python_strings.asp
String literals in python are surrounded by either single quotation marks, or double quotation marks.
_________
_________
Slicing Strings
https://www.w3schools.com/python/python_strings_slicing.asp
You can return a range of characters by using the slice syntax. Specify the start index and the end index, separated by a colon, to return a part of the string.
_________

"""


# Your code should go here:


def cardHide(theString1: str) -> str:
    # Counting the length.
    try:
        count = 0
        while True:
            theString1[count]
            count += 1
    except IndexError:
        pass

    # Setting the limit of credit card.
    # The limit should be either 14 or 16.

    try:
        assert count == 14
    except AssertionError:
        try:
            assert count == 16
        except AssertionError:
            # return "The number entered, is not credit card number."
            return "The number entered is invalid credit card number."

    # Now make a algorithm like whether it should have hundred or thousand.
    # It should * all the indexs except lasts.

    # Let's perform the main function.
    starSide = theString1[:-4]
    fourDigitSide = theString1[-4:]
    # starSide[:] = "*"  # There should be much more simpler way to just
    # Replace all the indexes with * symbol.

    # Replacing with '*' all the theString1[:-4]
    starSide = list(starSide)
    i = 0
    while i < count - 4:
        starSide[i] = "*"
        i += 1
    print(starSide)
    print(type(starSide))
    print(len(starSide))
    # Converting into string.
    i = 0
    # starSideString = ""
    while i < count - 4:
        # starSideString += str(starSide[i])
        # starSideString += starSide[i]
        starSide += str(starSide[i])
        i += 1

    print(starSide)
    print(len(starSide))
    print(type(starSide))

    # Amending the output together.

    outputStrings = starSide + fourDigitSide
    # outputStrings = starSideString + fourDigitSide
    return outputStrings


# Why the lengths are 16, 16 and 14?
# Please do check it out.
# Please do look into this matter.

print(cardHide("1234123456785678"))  # ➞ "************5678"


# print(cardHide("8754456321113213"))  # ➞ "************3213"

# print(cardHide("35123413355523"))  # ➞ "**********5523"

# inc.
# Read the unknown resources.
# It is just solved. Just it need to be revised once again.
# Just use the starSideString with the string += thing.
# return the starSideString

# By the way, do it the official way too.
# By reading the resources.
# Like, by using the methods and functions.


def cardHideMain(theString1: str) -> str:
    return "Do the way of using methods and functions."


print(cardHideMain())

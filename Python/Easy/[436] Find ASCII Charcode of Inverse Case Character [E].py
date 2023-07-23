"""
####  Find ASCII Charcode of Inverse Case Character  ####

Create a function that takes a single character as an argument
and returns the char code of its lowercased / uppercased counterpart.


[Examples]

___
Given that:
  - "A" char code is: 65
  - "a" char code is: 97

counterpartCharCode("A") ➞ 97

counterpartCharCode("a") ➞ 65
_____



[Notes]

___
*) The argument will always be a single character.
*) Not all inputs will have a counterpart (e.g. numbers), in which case return the input's char code.
___



[formatting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
ord() Method
https://docs.python.org/3/library/functions.html#ord
Given a string representing one Unicode character, return an integer representing the Unicode code point of that character. For example, ord('a') returns the integer 97 …
_________
_________
swapcase() Method
https://www.tutorialspoint.com/python/string_swapcase.htm
Returns a copy of the string in which all the case-based characters have had their case swapped.
_________
_________
Get the ASCII Value of a Character
https://www.w3resource.com/python-exercises/python-basic-exercise-86.php
Write a Python program to get the ASCII value of a character. ASCII codes represent text in computers, telecommunications equipment, and other devices. Most modern char …
_________
_________
isupper(), islower()
https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/
This may be an alternative way to solving the solution but beware it may be more complicated then necessary. The commands isupper() converts all txt to uppercase and vi …
_________
_________
Character to Integer
https://mail.python.org/pipermail/python-win32/2005-April/003100.html
function ord() would get the int value of the char. and in case you want to convert back after playing with the number, function chr() does the trick
_________
_________
isalpha() Method
https://www.w3schools.com/python/ref_string_isalpha.asp
Check if all the characters in the text are letters.
_________

"""


# Your code should go here:

def counterPartCharCode(input1: str) -> int:
    # Making character ranges.
    upperCaseRange = range(65, 65 + 26)
    lowerCaseRange = range(97, 97 + 26)
    charUpperRange = [chr(n) for n in upperCaseRange]
    charLowerRange = [chr(n) for n in lowerCaseRange]
    # print(charLowerRange)
    # print(charUpperRange)

    # Checking it's length.
    count = 0
    try:
        while True:
            # if input1[i] == True:  # This may be a ticket to not using the while True:
            #     count += 1
            #     i += 1
            # elif input1[i] != True:
            #     pass

            input1[count]
            count += 1
    except IndexError:
        pass

    # Setting count limit.
    if count == 1:

        # Checking if it is only character or not.
        if input1 in charLowerRange or charUpperRange:

            # Now swapping them.
            if input1 in charLowerRange:
                formula = chr(ord(input1) - (25 + 7))
                return formula
            elif input1 in charUpperRange:
                formula = chr(ord(input1) + (25 + 7))
                return formula

        elif input1 not in charLowerRange or charUpperRange:
            return "Input provided is not a letter."
            # return "Input given is not a letter."
            # return "Input is not a letter."


    elif count == 0 or count > 1:
        return "Input length should be 1 only."

    # Checking if it is only letter?


print(counterPartCharCode("n"))
# Now the work is remaining for it to output in the swapcased ASCII number.

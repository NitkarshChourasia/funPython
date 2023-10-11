"""
####  The Reverser!  ####

The "Reverser" takes a string as input and returns that string in reverse order, with the opposite case.


[Examples]

___
reverse("Hello World") ➞ "DLROw OLLEh"

reverse("ReVeRsE") ➞ "eSrEvEr"

reverse("Radar") ➞ "RADAr"
_____



[Notes]

There will be no punctuation in any of the test cases.


[formatting] [language_fundamentals] [strings] 



-------------------------------------------------------------------
[Resources]
_________
swapcase() Method
https://www.programiz.com/python-programming/methods/string/swapcase
Converts all uppercase characters to lowercase and all lowercase characters to
uppercase characters of the given string, and returns it.
_________
_________
How to Reverse a String
https://www.w3schools.com/python/python_howto_reverse_string.asp
Learn how to reverse a string in Python.
_________
_________
swapcase() Method
https://www.geeksforgeeks.org/python-string-swapcase/
Converts all uppercase characters to lowercase and vice versa of the given string, and returns it.
_________
_________
reversed() Function
https://www.programiz.com/python-programming/methods/built-in/reversed
Returns the reversed iterator of the given sequence.
_________

"""


# Your code should go here:

# Restrictions:
# - Takes string.
# - Outputs string.


# To solve for:
# - Reverse the string.
# - Swap the cases.
def reverse(the_string: str) -> str:
    # Checking strictly for string type input.
    if isinstance(the_string, str):
        # String reversed.
        reversed_string = the_string[::-1]

        # Swapping case.
        smallcase_letters = [chr(letters) for letters in range(97, 97 + 26)]

        uppercase_letters = [chr(letters) for letters in range(65, 65 + 26)]

        output_string = ""
        for ele in reversed_string:
            if ele in smallcase_letters:
                output_string += chr(ord(ele) - 32)
            elif ele in uppercase_letters:
                output_string += chr(ord(ele) + 32)
            elif ele == " ":
                output_string += " "
        return output_string

    elif not isinstance(the_string, str):
        "Only string inputs are valid."


print(reverse("Hello World"))  # ➞ "DLROw OLLEh"

print(reverse("ReVeRsE"))  # ➞ "eSrEvEr"

print(reverse("Radar"))  # ➞ "RADAr"

print(reverse("Nitin"))

# complete.

"""
####  Recursion to Repeat a String n Number of Times  ####

Create a recursive function that takes two parameters and repeats the string n number of times.
The first parameter txt is the string to be repeated and
the second parameter is the number of times the string is to be repeated.


[Examples]

___
repetition("ab", 3) ➞ "ababab"

repetition("kiwi", 1) ➞ "kiwi"

repetition("cherry", 2) ➞ "cherrycherry"
_____



[Notes]

The second parameter of the function is positive integer.


[recursion] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Recursion and Recursive Functions
https://pythonspot.com/recursion/
In English there are many examples of recursion: "To understand recursion, you must first understand recursion", "A human is someone whose mother is human". You mig …
_________
_________
Repeat a String N Times and Print N Lines of It
https://stackoverflow.com/questions/40008279/repeat-a-string-n-times-and-print-n-lines-of-it
I've been stuck on a question for some time now: I'm looking to create a python function that consumes a string and a positive integer. The function will print the str …
_________
_________
Recursion
https://www.programiz.com/python-programming/recursion
Is the process of defining something in terms of itself. A physical world example would be to place two parallel mirrors facing each other. Any object in between them …
_________
_________
How to print a string multiple times on the same line in Python?
https://kite.com/python/answers/how-to-print-a-string-multiple-times-on-the-same-line-in-python#:~:text=Use%20the%20multiplication%20operator%20*%20to,as%20value%20to%20print%20it.
Multiply a string with the multiplication operator * by an integer n to concatenate the string with itself n times. Call print(value) with the resultant string as value …
_________

"""


# Your code should go here:

# I wanted to preserve the original string therefore did all this manipulations.
def repetition1(string1, ntimes):
    if ntimes == 0:
        return ""

    elif ntimes == 1:
        return string1

    elif ntimes > 1:
        result = ""
        i = 0
        while i < ntimes:  # While loop defeats the purpose of recursion.
            result += string1
            i += 1
        return result

    # return repetition(string1, ntimes - 1)


# print(repetition("ab", 3))  # ➞ "ababab"
#
# print(repetition("kiwi", 1))  # ➞ "kiwi"
#
# print(repetition("cherry", 2))  # ➞ "cherrycherry"


def repetition(string1, ntimes):
    if ntimes == 0:
        return ""
    elif ntimes == 1:
        return string1 + string1 + string1
    print(string1, end="")

    return repetition(string1, ntimes - 1)


print(repetition("ab", 3))  # ➞ "ababab"

print(repetition("kiwi", 1))  # ➞ "kiwi"

print(repetition("cherry", 3))  # ➞ "cherrycherry"

# inc.

# successful toh hua, par kya sahi mai hua lekin?
# successful toh hua, par kya sahi mai yeh recursion hai?
# chatgpt, ko puchna padega.
# par at least recursion ke t
# is recursion ko auur chota kar sakta hu mai. Kaise?
# elif == 1 hatha kar mai iss recursion ko auur chota kar sakta hu.
# aur koi tarika hai isse chota karne ka? efficient aur efficient banane ka?
# par recursion toh hua lekin chatgpt ko puchuga ki aurr kaise behtar banaau isse...


# ERROR ke liye Return Value dekho, please.

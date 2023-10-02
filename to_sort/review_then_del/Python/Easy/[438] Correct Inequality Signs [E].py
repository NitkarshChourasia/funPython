"""
####  Correct Inequality Signs  ####

Create a function that returns True if a given inequality expression is correct and False otherwise.


[Examples]

___
correct_signs("3 < 7 < 11") ➞ True

correct_signs("13 > 44 > 33 > 1") ➞ False

correct_signs("1 < 2 < 6 < 9 > 3") ➞ True
_____



[Notes]

N/A


[regex] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
eval() Method
https://www.programiz.com/python-programming/methods/built-in/eval
Parses the expression passed and runs python expression (code) within the program.
_________
_________
Eval Really Is Dangerous
https://nedbatchelder.com/blog/201206/eval_really_is_dangerous.html
Python has an eval() function which evaluates a string of Python code. This is very powerful, but is also very dangerous if you accept strings to evaluate from untruste …
_________
_________
String Split
https://www.w3schools.com/python/ref_string_split.asp
Though this can be solved easily by using eval(), try challenging yourself with a different way! Without eval, this can be done by splitting the string into a list and …
_________
_________
Video Walk Through of Challenge
https://www.youtube.com/watch?v=vda8JZbXVq8
In this video, you will learn how to solve these problems in Python: 0:15 Correct Inequality Signs, 2:25 Alphabet Soup, 5:21 The Museum of Incredibly DULL Things.
_________
_________
eval() Method
https://towardsdatascience.com/python-eval-built-in-function-601f87db191
This would be a short article about eval function in python, wherein I would be explaining to you about eval function, its syntax, and few questions that are often aske …
_________

"""


# Your code should go here:

def correctSigns(input1):
    list1 = [input1]
    list2 = list(input1)
    print(list1)
    # what is the type of operator?
    plusOperator = '+'
    print(plusOperator)
    a = 99
    b = 99
    c = a + b
    # print(type(+)) # WHAT IS THE TYPE OF THIS?
    # What if I want to use this way the way I am intending it to be used?
    return list2


print(correctSigns("3 < 7 < 11"))  # ➞ True

print(correctSigns("13 > 44 > 33 > 1"))  # ➞ False

print(correctSigns("1 < 2 < 6 < 9 > 3"))  # ➞ True


def correctSigns1(input1):
    # I can use remove and replace method or function to remove whitespaces.
    # What are other ways to remove the whitespaces???!
    # What are other ways to remove the whitespaces?? Keep that in mind.
    # Please! Keep this in mind.
    list1 = list(input1)
    print(f"list1: {list1}")

    try:
        count = 0
        while True:
            list1[count]
            count += 1
    except IndexError:
        pass

    outputLst1 = []
    strAppend = ""
    i = 0
    while i <= count:
        if i == count:
            outputLst1.append(strAppend)
        elif list1[i] != " ":
            strAppend += list1[i]
        elif list1[i] == " ":
            outputLst1.append(strAppend)
            strAppend = ""
        i += 1
    return f"outputLst1: {outputLst1}, i: {i}"


# Debug it one more time to see how it behaves.

# Possible ways to do them is: separate numbers and separate operators.
# And then apply some zip and whip to work with them.
# Maybe, just a planning. See what lies ahead.

print(correctSigns1("3 < 7 < 11"))  # ➞ True

# print(correctSigns1("13 > 44 > 33 > 1"))  # ➞ False

# print(correctSigns1("1 < 2 < 6 < 9 > 3"))  # ➞ True

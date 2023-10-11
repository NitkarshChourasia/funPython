"""
####  Instant JAZZ  ####

Create a function which concatenates the number 7 to the end of every chord in a list. Ignore all chords which already end with 7.


[Examples]

___
jazzify(["G", "F", "C"]) ➞ ["G7", "F7", "C7"]

jazzify(["Dm", "G", "E", "A"]) ➞ ["Dm7", "G7", "E7", "A7"]

jazzify(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]) ➞ ["F7", "E7", "A7", "Ab7", "Gm7", "C7"]

jazzify([]) ➞ []
_____



[Notes]

___
*) Return an empty list if the given list is empty.
*) You can expect all the tests to have valid chords.
___



[arrays] [language_fundamentals] [loops] 



-------------------------------------------------------------------
[Resources]
_________
endswith() Method
https://www.programiz.com/python-programming/methods/string/endswith
Returns True if a string ends with the specified suffix. If not, it returns False.
_________
_________
How to get Last N characters in a string?
https://thispointer.com/python-how-to-get-last-n-characters-in-a-string/
A String is a sequence of characters, and each character in it has an index number associated with it. For example, we have a string variable sample_str that contains a …
_________
_________
How can you repeat strings in Python?
https://www.quora.com/How-can-you-repeat-strings-in-Python-What-are-some-tips-for-doing-so
In Python if you use loop for this ,then you cannot differentiate it’s feature with other programming languages. Python makes our stuffs easier. If you want to repeat …
_________
_________
endswith() Method
https://www.tutorialspoint.com/python/string_endswith.htm
Returns True if the string ends with the specified suffix, otherwise return False optionally restricting the matching with the given indices start and end.
_________
_________
String Concatenation
https://www.digitalocean.com/community/tutorials/an-introduction-to-working-with-strings-in-python-3
This Python tutorial will go over how to create and print strings, how to concatenate and replicate strings, and how to store strings in variables.
_________

"""


# Your code should go here:


def jazzify(lst1):
    output_lst1 = []
    # How does it behave with empty list?
    # Like the last example?
    # what if the len(input) == 0: return [] # How will this react?
    for ele in lst1:
        if "7" not in ele:
            output_lst1.append(ele + str(7))
        elif "7" in ele:
            output_lst1.append(ele)
    return output_lst1


print(jazzify(["G", "F", "C"]))  # ➞ ["G7", "F7", "C7"]

print(jazzify(["Dm", "G", "E", "A"]))  # ➞ ["Dm7", "G7", "E7", "A7"]

print(
    jazzify(["F7", "E7", "A7", "Ab7", "Gm7", "C7"])
)  # ➞ ["F7", "E7", "A7", "Ab7", "Gm7", "C7"]

print(jazzify([]))  # ➞ []


# Restriction maybe only iterative like a list or tuple or dictionary.
# Because may not be viable option let's see, what happens.
def jazzify1(lst1):
    # How to find len without len function?
    # Search google about this.

    ## while True with try and except method. # IMP
    ## for loop ho gaya with count+=1. # IMP
    ## any more method?????. # IMP
    try:
        count = 0
        while True:
            lst1[count]
            count += 1
    except IndexError:
        pass

    output_lst1 = "0" * count
    print("Count: {0}".format(count))
    print("Len function output_lst1: {}".format(len(output_lst1)))
    print("|{}|".format(output_lst1))
    # return ("|{}|".format(output_lst1)) # Just to output while avoiding while condition:

    lst1 = list(lst1)
    i = 0
    while i < count:
        # This will malfunction because count can be more then i, let's see maybe.
        if "7" not in lst1[i]:
            output_lst1[i] = lst1[i] + str(7)
        elif "7" in lst1[i]:
            output_lst1[i] = lst1[i]
        i += 1
    return map(output_lst1, str)


# WHATEVER IS THE PROBLEM I NEED TO SOLVE THIS.
# USE CHATGPT IF NEEDED.

# How to tackle the error in the last segment.
# One was filter and another one was map. # See, both of these.
# One was boolean based and another one was output based, something.

print(jazzify1(lst1="abcdefghijklmnopqrstuvwxyz"))

# inc.


## IN SHORT.

# - Another ways to solve len.
# - Another ways to solve the error encountered of 'str' object does not support item assignment.

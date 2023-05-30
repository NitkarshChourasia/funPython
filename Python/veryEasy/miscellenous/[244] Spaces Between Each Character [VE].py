"""
##Spaces Between Each Character

Create a function that takes a string and returns a string with spaces in between all of the characters.


[Examples]

___
space_me_out("space") ➞ "s p a c e"

space_me_out("far out") ➞ "f a r   o u t"

space_me_out("elongated musk") ➞ "e l o n g a t e d   m u s k"
_____



[Notes]

Treat a space as its own character (i.e. leave three spaces between words).


[arrays] [formatting] [language_fundamentals] [strings]



-------------------------------------------------------------------
[Resources]
_________
join() Method
https://www.tutorialspoint.com/python/string_join.htm
Returns a string in which the string elements of sequence have been joined by a separator.
_________
_________
Adding Space Between Characters
https://stackoverflow.com/questions/18221436/python-adding-space-between-characters-in-string-most-efficient-way
Say I have a string s = "BINGO"; I want to iterate over the string to produce "B I N G O". Is there a more efficient way to go about this?
_________
"""
# Your code should go here:


def spaceMeOut(str1):
    return str1.join(" ")



print(spaceMeOut("space")) # ➞ "s p a c e"
print(spaceMeOut("far out")) # ➞ "f a r   o u t"
print(spaceMeOut("elongated musk")) # ➞ "e l o n g a t e d   m u s k"


def spaceMeOutUsingFor(str1):
    spacedList = []
    for i in str1:
        emptyList.append(i + " ")
    stringfied = string(emptyList)  # converting list into strings.
    return stringfied

print(spaceMeOutUsingFor("space")) # ➞ "s p a c e"
print(spaceMeOutUsingFor("far out")) # ➞ "f a r   o u t"
print(spaceMeOutUsingFor("elongated musk")) # ➞ "e l o n g a t e d   m u s k"

# testing.

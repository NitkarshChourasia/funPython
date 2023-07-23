"""
####  Compare Strings by Count of Characters  ####

Create a function that takes two strings as arguments and return either True or False depending on whether
the total number of characters in the first string is equal to the total number of characters in the second string.


[Examples]

___
comp("AB", "CD") ➞ True

comp("ABC", "DE") ➞ False

comp("hello", "edabit") ➞ False
_____



[Notes]

___
*) Don't forget to return the result.
*) If you get stuck on a challenge, find help in the Resources tab.
*) If you're really stuck, unlock solutions in the Solutions tab.
___



[conditions] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Python Strings
https://thepythonguru.com/python-strings/
The length variable is applicable to array but not for string objects whereas the length() method is applicable for string objects but not for arrays.
_________
_________
The Length of a string len() Function
https://www.tutorialspoint.com/python3/string_len.htm
Returns the length of the string.
_________
_________
len() Method
https://www.guru99.com/python-string-length-len.html#:~:text=len()%20is%20a%20built,provide%20the%20number%20of%20elements.
Is a built-in function in python. You can use the len() to get the length of the given string, array, list, tuple, dictionary, etc. You can use len function to optimize …
_________

"""


# Your code should go here:

def comp(string1, string2):
    if isinstance(string1, str):
        count1 = 0
        while string1[count1] != string1[-1]:
            count1 += 1
        count2 = 0
        try:
            while True:  # Nasa avoids this kind of statements...altogether. # So, if possible think of another way.
                string2[count2]
                count2 += 1
        except IndexError:
            pass
            # I just want to catch this, that's it.
        print(count1)
        print(count2)
        if count1 == count2:
            return True
        elif count1 != count2:
            return False
        else:
            return "Some different bug is present."


# print(comp("AB", "CD"))  # ➞ True
#
# print(comp("ABC", "DE"))  # ➞ False
#
# print(comp("hello", "edabit"))  # ➞ False
#
print(comp("Heollo", "Heollo"))
#

while True:
    pass

# What is multithreading? Does it means I can run a program and simultaneously run many programs in it.
# Like TWO WHILE LOOPS?!!!
# what 'e' does in vim?

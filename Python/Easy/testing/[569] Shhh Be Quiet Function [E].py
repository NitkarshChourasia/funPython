"""
##Shhh Be Quiet Function

Write a function that removes all capital letters from a sentence except the first letter,
puts quotation marks around the sentence and adds ", whispered Edabit." at the end.


[Examples]

___
shhh("HI THERE!") ➞ '"Hi there!", whispered Edabit.'

shhh("tHaT'S Pretty awesOme") ➞ '"That's pretty awesome", whispered Edabit.'

shhh("") ➞ '"", whispered Edabit.'
_____



[Notes]

Don't forget to surround the original string with double quotation marks "".


[formatting] [language_fundamentals] [strings] 



-------------------------------------------------------------------
[Resources]
_________
string capitalize()
https://www.geeksforgeeks.org/string-capitalize-python/
Using the capitalize() function in Python to capitalize the first letter of a string.
_________
_________
Using % and .format() for great good!
https://pyformat.info
Simple positional formatting is probably the most common use-case. Use it if the order of your arguments is not likely to change and you only have very few elements you …
_________
_________
String lower() Method
https://www.programiz.com/python-programming/methods/string/lower
Converts all uppercase characters in a string into lowercase characters and returns it.
_________
""" 
# Your code should go here:

def shhh(str1 : str) -> str:
    lowStr1 = str1.lower()
    if str1.len() > 0:
        return "{0}{1}, whispered Edabit".format(lowStr1[0].upper(), lowStr1[1::])
    elif str1.len() == 0:
        return '"", whispered Edabit.'


print(shhh("HI THERE!")) # ➞ '"Hi there!", whispered Edabit.'

print(shhh("tHaT'S Pretty awesOme")) # ➞ '"That's pretty awesome", whispered Edabit.'

print(shhh("")) # ➞ '"", whispered Edabit.'


# testing.
# checkResources.

# what is this errors with .len() functions? huh/?
"""
##Even and Odd Strings

Given a one word lowercase string txt, return another string such that even-indexed and odd-indexed characters are grouped and groups are space-separated.


[Examples]

___
even_odd_string("Nitkarsh") ➞ "mbsi uahr"
# Letters at even indexes = "mbsi"
# Letters at odd indexes = "uahr"
# Join both strings with a space

even_odd_string("amazing") ➞ "eai dbt"

even_odd_string("airforce") ➞ "aroc ifre"
_____



[Notes]

There will be no space in the given string.


[interview] [language_fundamentals] [sorting] [strings]



-------------------------------------------------------------------
[Resources]
_________
Separate Odd and Even Index Elements
https://www.geeksforgeeks.org/python-separate-odd-and-even-index-elements/
Python list are quite popular and no matter what type of field one is coding, one has to deal with lists and its various applications. In this particular article, we di …
_________
_________
Access Item Index in a Comprehension List
https://stackoverflow.com/questions/14864922/in-python-list-comprehension-is-it-possible-to-access-the-item-index
How to access item index in a comprehension list.
_________
"""
# Your code should go here:


def evenOddIndexStr(str1):
    str1 = str1.lower()
    evenIndexStr1 = range(0, str1.len(), 2)
    oddIndexStr1 = range(1, str1.len(), 2)
    evenIndexList = []
    oddIndexList = []
    for i in evenIndexStr1:
        evenIndexList.append(str1[i])
    for j in oddIndexStr1:
        oddIndexList.append(str1[i])
    returnAns = string(evenIndexList) + " " + string(oddIndexList) # The answer should be as expected as in the example.
    return returnAns



even_odd_string("Nitkarsh") ➞ "ntarh ik" #
# Letters at even indexes = "mbsi"
# Letters at odd indexes = "uahr"
# Join both strings with a space
even_odd_string("amazing") ➞ "eai dbt"
even_odd_string("airforce") ➞ "aroc ifre"


# testing.
# correct the example while testing.

"""
##"EdaBit" Challenge

Create a function that returns the list of numbers from a given range.
But for multiples of three, return “Nit” instead of the number and for the multiples of five,
return “Karsh”. For numbers which are multiples of both three and five, return “NitKarsh”.


[Examples]

___
nit_karsh(0, 10) ➞ ["NitKarsh", 1, 2, "Nit", 4, "Karsh", "Nit", 7, 8, "Nit", "Karsh" ]

nit_karsh(14, 20) ➞ [14,  "NitKarsh", 16, 17,  "Nit", 19, "Karsh" ]

nit_karsh(99, 106) ➞ ["Nit", "Karsh", 101, "Nit", 103, 104, "NitKarsh", 106 ]
_____



[Notes]

In case the number 0 happens to be in the range, return "NitKarsh" as well.


[algorithms] [math] 



-------------------------------------------------------------------
[Resources]
_________
Python range() Function
https://www.w3schools.com/python/ref_func_range.asp
Returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
_________
_________
Hexadecimal Based FizzBuzz in Python
https://stackoverflow.com/questions/33199156/hexadecimal-based-fizzbuzz-in-python
To most of you, this may be very easy to create. Though after browsing online, I've found some posts where they were challenged not to use the modulus operator. I found …
_________
_________
Python if...else Statement
https://www.programiz.com/python-programming/if-elif-else
Learn to create decisions in a Python program using different forms of if..else statement.
_________
_________
append() Method
https://www.programiz.com/python-programming/methods/list/append
The method takes a single argument item - an item to be added at the end of the list. The item can be numbers, strings, dictionaries, another list, and so on.
_________
""" 
# Your code should go here:


def nitkarsh(start, end):
    lst1 = [x for x in range(start, end+1)]
    i = 0
    outputLst1 = []
    while ( i < lst1[-1])
        if lst1[i] % 3 == 0:
            outputLst1.append("Nit")
        elif lst1[i] % 5 == 0:
            outputLst1.append("Karsh")
        elif lst1[i] % 5 == 0 and lst[i] % 3 == 0:
            outputLst1.append(("Nitkarsh"))
        i = i + 1
    return outputLst1




print(nitKarsh(0, 10)) # ➞ ["NitKarsh", 1, 2, "Nit", 4, "Karsh", "Nit", 7, 8, "Nit", "Karsh" ]

print(nitKarsh(14, 20)) # ➞ [14,  "NitKarsh", 16, 17,  "Nit", 19, "Karsh" ]

print(nitKarsh(99, 106)) # ➞ ["Nit", "Karsh", 101, "Nit", 103, 104, "NitKarsh", 106 ]


testing.
# checkResources.
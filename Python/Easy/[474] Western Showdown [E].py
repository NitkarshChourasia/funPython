"""
##Western Showdown

Wild Roger is participating in a Western Showdown, meaning he has to draw (pull out and shoot) his gun faster than his opponent in a gun standoff.
Given two strings,p1 and p2, return which person drew their gun the fastest. If both are drawn at the same time, return "tie".


[Examples]

___
showdown(
  "   Bang!        ",
  "        Bang!   "
) ➞ "p1"

# p1 draws his gun sooner than p2

showdown(
  "               Bang! ",
  "             Bang!   "
) ➞ "p2"

showdown(
  "     Bang!   ",
  "     Bang!   "
) ➞ "tie"
_____



[Notes]

Both strings are the same length.


[conditions] [strings] 



-------------------------------------------------------------------
[Resources]
_________
find() Method
https://www.geeksforgeeks.org/string-find-python/
Returns the lowest index of the substring if it is found in given string. If its is not found then it returns -1.
_________
_________
index() Method
https://www.w3schools.com/python/ref_list_index.asp
Returns the position at the first occurrence of the specified value.
_________
""" 
# Your code should go here:

def showdown(p1, p2):
    lowerP1 = p1.lower()
    lowerP2 = p2.lower()
    indexP1 = lowerP1.index("b")
    indexP2 = lowerP2.index('b')
    if indexP1 > indexP2:
        return "p1 draws his gun sooner than p2."
    elif indexP2 > indexP1:
        return "p2 draws his gun sooner then p1."
    elif indexP1 == indexP2:
        return  "tie."


print(showdown(
    "   Bang!        ",
    "        Bang!   "
)) # ➞ "p1"

# p1 draws his gun sooner than p2

print(showdown(
    "               Bang! ",
    "             Bang!   "
)) # ➞ "p2"

print(showdown(
    "     Bang!   ",
    "     Bang!   "
)) # ➞ "tie"


# testing.
# checkAgain.
# checkAgain. Check, all the resources unknown.
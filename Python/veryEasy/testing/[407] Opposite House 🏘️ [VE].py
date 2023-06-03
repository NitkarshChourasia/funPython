"""
##Opposite House 🏘️

Nitkarsh was walking through a straight street with exactly n identical houses on both sides. House numbers in the street look like this:
___
1 |   | 6

3 |   | 4

5 |   | 2
_____

He noticed that Even numbered houses increase on the right while Odd numbered houses decrease on the left.
Create a function that takes a house number house and length of the street n and returns the house number on the opposite side.


[Examples]

___
opposite_house(1, 3) ➞ 6

opposite_house(2, 3) ➞ 5

opposite_house(3, 5) ➞ 8
_____



[Notes]

N/A


[interview] [logic] [math] [numbers]



-------------------------------------------------------------------
[Resources]
_________
Python Operators
https://www.w3schools.com/python/python_operators.asp
Operators are used to perform operations on variables and values.
_________
"""
# Your code should go here:


def oppositeHouse(houseNo, houseLen):
    i = 0
    oddLst1 = []
    evenLst1 = []
    oddNum = 1
    evenNum = 2
    toAdd = 0
    while oddNum == houseLen and evenNum == houseLen:
        oddNum = oddNum + toAdd
        evenNum = evenNum + toAdd
        oddLst1.append(oddNum)
        evenLst1.append(evenNum)
        while toAdd = 2:
            toAdd = toAdd + 1
        # if oddNum == houseLen and evenNum == houseLen:
            # break

    revEvenLst1 = evenLst1.reverse()
    # add two list use index
    if houseNo in oddLst1:
        indexNo = oddLst1.index(houseNo)
        outputAns = revEvenLst1[indexNo] # Does index function output based on whole number or integers, on that basis I'll have to minus it.
        return outputAns
    elif houseNo in revEvenLst1:
        indexNo = revEvenLst1.index(houseNo)
        outputAns = oddLst1.index(houseNo)
        return outputAns


print(oppositeHouse(1, 3)) # ➞ 6

print(oppositeHouse(2, 3)) # ➞ 5

print(oppositeHouse(3, 5)) # ➞ 8

print(oppositeHouse(9, 10)) # 12, I guess.

# Add 3 more. Homework to be done.


# testing.
# checkAgain.
# checkAgain. The resources.
# interesting.
# awesome.

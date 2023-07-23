"""
####  Pythagorean Triplet  ####

Create a function that validates whether three given integers form a Pythagorean triplet.
The sum of the squares of the two smallest integers must equal the square of the largest number to be validated.


[Examples]

___
is_triplet(3, 4, 5) ➞ True
# 3² + 4² = 25
# 5² = 25

is_triplet(13, 5, 12) ➞ True
# 5² + 12² = 169
# 13² = 169

is_triplet(1, 2, 3) ➞ False
# 1² + 2² = 5
# 3² = 9
_____



[Notes]

Numbers may not be given in a sorted order.


[geometry] [math] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
sorted() Function
https://www.programiz.com/python-programming/methods/built-in/sorted
Returns a sorted list from the items in an iterable. In this tutorial, we will learn to sort elements in ascending and descending order using the Python shorted() function.
_________
_________
max() and min() ⁠— Finding Max and Min in List or Array
https://howtodoinjava.com/python/max-min/
Python examples to find the largest (or the smallest) item in a collection (e.g. list, set or array) of comparable elements using max() and min() methods.
_________
_________
Python List sort() Method
https://www.w3schools.com/python/ref_list_sort.asp
Used to create a sorted list according to the values and mode provided
_________
_________
Sort Three Integers Without Using Conditional Statements and Loops
https://www.w3resource.com/python-exercises/python-basic-exercise-69.php
Write a Python program to sort three integers without using conditional statements and loops.
_________
_________
Pythagorean Triple
https://en.wikipedia.org/wiki/Pythagorean_triple
Consists of three positive integers a, b, and c, such that a2 + b2 = c2. Such a triple is commonly written (a, b, c), and a well-known example is (3, 4, 5). If (a, b, c …
_________
_________
Program to Find the Largest Among Three Numbers
https://scanftree.com/programs/python/python-program-to-find-the-largest-among-three-numbers/
How to find the largest variable in 3 variables.
_________

"""
import math


# Your code should go here:


def isTriplet(a, b, c):
    # if isinstance((a,b,c), int): Check this.

    # Making list.
    elements = [a, b, c]

    # I know it is going to be three elements only.
    # But for practice purposes let's create a counting element.

    # Length count.
    count = 0
    try:
        while True:
            elements[count]
            count += 1
    except IndexError:
        pass
    print(f"Count: {count}")
    # Another way of doing this is.
    # for ele in elements:
    #     count += 1

    # FEATURE ADD: if elements > 3 then abort the function, because pythogorean based triangle has three sides only.

    # Sorting, Ascending.
    i = 0
    j = 1  # Watch out this. Because this can be the thing where things must be going wrong.
    while i < count:
        while j < count:
            if elements[i] < elements[j]:
                # j += 1
                pass
            elif elements[j] < elements[i]:
                temp = elements[i]
                elements[i] = elements[j]
                elements[j] = temp
                # j += 1
            elif elements[i] == elements[j]:
                temp = elements[i + 1]
                elements[i + 1] = elements[j]
                elements[j] = temp
                # j += 1
            print(f"J: {j}")
            j += 1
        print(f"I: {i}")
        j = 0  # Will it matter if j = 0 is placed here, Or...
        i += 1
        # j = 0 # Will it matter if j = 0 is placed here, Or...

    firstSide = math.pow(elements[0], 2)
    print(firstSide)
    secondSide = math.pow(elements[1], 2)
    print(secondSide)
    thirdSide = math.pow(elements[2], 2)
    print(thirdSide)

    leftSideSum = firstSide + secondSide
    rightSideSum = thirdSide  # Just for the naming purposes, can use both the names doesn't matter much.

    if leftSideSum == rightSideSum:
        return True
    elif leftSideSum != rightSideSum:
        return False


print(isTriplet(3, 4, 5))  # ➞ True
# 3² + 4² = 25
# 5² = 25

print(isTriplet(13, 5, 12))  # ➞ True
# 5² + 12² = 169
# 13² = 169

print(isTriplet(1, 2, 3))  # ➞ False
# 1² + 2² = 5
# 3² = 9


# Some error in sorting happened.
# While it was equal.
# Compare it with: [423] Let's Sort This List! [E].py
# Compare in split with: [423] Let's Sort This List! [E].py
# Also some other errors to solve.

# inc.

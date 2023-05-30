"""
##Return Odd > Even

Given a list, return True if there are more odd numbers than even numbers, otherwise return False.


[Examples]

___
oddeven([1, 2, 3, 4, 5, 6, 7, 8, 9]) ➞ True

oddeven([1]) ➞ True

oddeven([13452394823795273847528572346]) ➞ False
_____



[Notes]

All lists will have at least 1 item.


[math] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Using List Comprehensions Instead of Map and Filter
https://www.oreilly.com/library/view/python-cookbook/0596001673/ch01s11.html
List comprehensions, added in Python 2.0, delightfully display how pragmatism can enhance both clarity and elegance.
The built-in map and filter functions still have th …
_________
_________
Python Modulo Operator
https://www.jquery-az.com/python-modulo/
In Python and generally speaking, the modulo (or modulus) is referred to the remainder from the
division of the first argument to the second. The symbol used to get th …
_________
""" 
# Your code should go here:

def oddEven(lst1):
    i = 0
    oddLst1 = []
    evenLst1 = []
    while (i < lst1.len()):
        if lst1[i] % 2 == 0:
            evenLst1.append(lst1[i])
        elif lst1[i] % 2 == 1:
            oddLst1.append(lst1[i])
        i = i + 1
    if oddLst1.len() > evenLst1.len():
        return True
    elif oddLst1.len() ! > evenLst1.len():  # Will this not bigger then symbol work????????????
        return False


print(oddEven([1, 2, 3, 4, 5, 6, 7, 8, 9])) # ➞ True

print(oddEven([1])) # ➞ True

print(oddEven([13452394823795273847528572346])) # ➞ False


# testing.
# checkResources.
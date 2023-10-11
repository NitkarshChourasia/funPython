"""
####  Let's Sort This List!  ####

Create a function that takes a list of numbers lst,
a string s and return a list of numbers as per the following rules:
___
*) "Asc" returns a sorted list in ascending order.
*) "Des" returns a sorted list in descending order.
*) "None" returns a list without any modification.
___



[Examples]

___
asc_des_none([4, 3, 2, 1], "Asc" ) ➞ [1, 2, 3, 4]

asc_des_none([7, 8, 11, 66], "Des") ➞ [66, 11, 8, 7]

asc_des_none([1, 2, 3, 4], "None") ➞ [1, 2, 3, 4]
_____



[Notes]

N/A


[arrays] [numbers] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
How to Reverse a List
https://www.programiz.com/python-programming/methods/built-in/reversed
How to reverse a list without changing the original list?
_________
_________
sorted() function
https://www.programiz.com/python-programming/methods/built-in/sorted
Returns a sorted list from the items in an iterable. The sorted() function sorts the elements of a given iterable in a specific order (either ascending or descending) a …
_________
_________
When to Use Sorted() and When to Use .Sort()
https://realpython.com/python-sort/#when-to-use-sorted-and-when-to-use-sort
This is a part of a bigger article "How to Use sorted() and sort() in Python". Since when I started this challenge I saw no difference in sorted() and .sort(), it made …
_________
_________
How to reverse a string?
https://www.w3schools.com/python/python_howto_reverse_string.asp
How to reverse a string (can also be used to reverse a Array).
_________
_________
sorted() Function
https://www.w3schools.com/python/ref_func_sorted.asp#:~:text=The%20sorted()%20function%20returns,string%20values%20AND%20numeric%20values.
How to sort a list/Array.
_________
_________
Dictionaries
https://www.w3schools.com/python/python_dictionaries.asp
Is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
_________

"""


# Your code should go here:


# I want to apply some sorting algorithm to it.
def ascDesNone(lst1, sortType):
    # For checking if the list contains only numbers or not?
    for i in lst1:
        if isinstance(i, (int, float)):
            pass
        elif not isinstance(i, (int, float)):
            return "List with only numbers are allowed."
    lowerCasedType = sortType.lower()
    if lowerCasedType == "asc":
        i = 0
        j = 0
        ## Some sort of bubble sort it is.
        while i < len(lst1):
            while j < len(lst1):
                if lst1[i] < lst1[j]:
                    # j += 1
                    pass
                elif lst1[j] < lst1[i]:
                    temp = lst1[j]
                    lst1[j] = lst1[i]
                    lst1[i] = temp
                    # j += 1
                elif lst1[i] == lst1[j]:
                    temp = lst1[i + 1]
                    lst1[i + 1] = lst1[j]
                    lst1[j] = temp
                    # j += 1

                j += 1
                print("printing I: {0}".format(i))
                print("printing J: {0}".format(j))
                print("Iterative lst1: {0}".format(lst1))

            i += 1
            j = (
                i + 1
            )  # Need to remove these all print statements which are kind of maybe, unnecessary.
            # Inculcate a habit of using debugger instead of print statements, maybe.
            # Next tiem use debugger and see what happens.
            print("Next iteration.")
            print("printing I: {0}".format(i))
        return "Final list: {0}".format(lst1)
    elif lowerCasedType == "des":
        i = 0
        j = 0
        while i < len(lst1):
            while j < len(lst1):
                if lst1[i] > lst1[j]:
                    # j += 1
                    pass
                elif lst1[j] > lst1[i]:
                    temp = lst1[i]
                    lst1[i] = lst1[j]
                    lst1[j] = temp
                    # j += 1
                elif lst1[i] == lst1[j]:
                    temp = lst1[i + 1]
                    lst1[i + 1] = lst1[j]
                    lst1[j] = temp
                    # j += 1
                j += 1
            i += 1
            j = i + 1  # One step ahead always.
        return "Final list: {0}".format(lst1)

    # Let it be whatever it is.
    # Can you do on paper? It would be good, if you did it on paper.


# Only Asc Testing.
print("Ascendings.")
print(ascDesNone([4, 3, 2, 1], "Asc"))  # ➞ [1, 2, 3, 4]

print(
    ascDesNone([9, 4, 3, 2, 1, 3], "Asc")
)  # Convert the sort type to lower/higher, preferred lower.

print(ascDesNone([9, 4, 3, 2, 1], "Asc"))  # let's see.

print(ascDesNone([7, 8, 11, 66], "Asc"))  # ➞ [66, 11, 8, 7]

print(ascDesNone([192, 0, -100, -1, 7, 8, 1661, 66], "Asc"))  # ➞ [66, 11, 8, 7]

# Only Des Testing.
print("Descendings.")
print(ascDesNone([4, 3, 2, 1], "Des"))  # ➞ [1, 2, 3, 4]

print(
    ascDesNone([9, 4, 3, 2, 1, 3], "Des")
)  # Convert the sort type to lower/higher, preferred lower.

print(ascDesNone([9, 4, 3, 2, 1], "Des"))  # let's see.

print(ascDesNone([7, 8, 11, 66], "Des"))  # ➞ [66, 11, 8, 7]

print(ascDesNone([192, 0, -100, -1, 7, 8, 1661, 66], "Des"))  # ➞ [66, 11, 8, 7]

# print(ascDesNone([1, 2, 3, 4], "None"))  # ➞ [1, 2, 3, 4]


# some corrections are left to be done.
# but these is almost done.


# Koi toh prakar ka sorting list banaya hai pata nahi.
# inc.
# what is the name of this sorting list.
# today, wrote my first algorithm and very happy about it.


# Hey, bhagwan phew!
# Desc bhi design karna hai.
# In different ways.
# Why not you make it modular?
# First design them in one function.
# Then modularise it.
# Why? Because the function is supposed to do only one task not hundreds.


# VERY GOOD. VERY GOOD ALGORITHM I DID.

# DSA
# |
# |
# |
# DSA IS THE THING.


# Second iteration was instant.
# The first one only takes time.
# Second and then third and then fourth don't.
# it took me almost 5% of the time.
# It didn't even took me 5% of the time.
# It was just instantaneous.


# Aur Na na prakar ke sorting algorithm design karna padega.
# Yeh shayad itna efficient nahi.
# Maybe.
# the best.
# inc.
# The almighty.
# The good.
# Also, check resources. Too.
# Like the first resource in resources.

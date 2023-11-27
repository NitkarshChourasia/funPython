"""
####  Characters in Shapes  ####

Create a function to calculate how many characters in total are needed to make up the shape.
You will be given a list of strings which make up a shape in the compiler (i.e. a square, a rectangle or a line).


[Examples]

___
count_characters([
  "###",
  "###",
  "###"
]) ➞ 9

count_characters([
  "22222222",
  "22222222",
]) ➞ 16

count_characters([
  "------------------"
]) ➞ 18

count_characters([]) ➞ 0

count_characters(["", ""]) ➞ 0
_____



[Notes]

Return 0 if the given list is empty.


[arrays] [language_fundamentals] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Python List
https://www.programiz.com/python-programming/list
In this article, we'll learn everything about Python lists, how they are created, slicing of a list,
adding or removing elements from them and so on. Python offers a ra …
_________
_________
len() Method
https://www.tutorialspoint.com/python3/string_len.htm
Returns the length of the string.
_________
_________
How to check if the string is empty?
https://stackoverflow.com/questions/9573244/how-to-check-if-the-string-is-empty
Regardless, what's the most elegant way to check for empty string values?
I find hard coding "" every time for checking an empty string not as good.
_________
_________
For Loops
https://www.w3schools.com/python/python_for_loops.asp
This is less like the for keyword in other programming languages,
and works more like an iterator method as found in other object-orientated programming languages.
_________
_________
Finding the Amount of Characters of All Words in a List
https://stackoverflow.com/questions/25934586/finding-the-amount-of-characters-of-all-words-in-a-list-in-python
Finding the amount of characters of all words in a list in Python.
_________

"""


# Your code should go here:

# Restrictions:
# - Take list.
# - List contains only string.

# To solve for:
# count = len(the_list_string[n])
# length of all the sublist's strings summed and returned.


def count_characters(the_string: str) -> int:
    outer_ele_len = len(the_string)

    total_elements_count: int = 0
    i = 0
    while i < outer_ele_len:
        total_elements_count += len(the_string[i])
        i += 1

    return total_elements_count


print(count_characters(["###", "###", "###"]))  # ➞ 9

print(
    count_characters(
        [
            "22222222",
            "22222222",
        ]
    )
)  # ➞ 16

print(count_characters(["------------------"]))  # ➞ 18

print(count_characters([]))  # ➞ 0

print(count_characters(["", ""]))  # ➞ 0

# inc.
# Remaining type check to the sublist.

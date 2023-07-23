"""
####  Filter out Strings from an Array  ####

Create a function that takes a list of non-negative integers and strings and return a new list without the strings.


[Examples]

___
filter_list([1, 2, "a", "b"]) ➞ [1, 2]

filter_list([1, "a", "b", 0, 15]) ➞ [1, 0, 15]

filter_list([1, 2, "aasf", "1", "123", 123]) ➞ [1, 2, 123]
_____



[Notes]

___
*) Zero is a non-negative integer.
*) The given list only has integers and strings.
*) Numbers in the list should not repeat.
*) The original order must be maintained.
___



[arrays] [formatting] [loops] 



-------------------------------------------------------------------
[Resources]
_________
isinstance() Method
https://www.programiz.com/python-programming/methods/built-in/isinstance
The isinstance() function checks if the object (first argument) is an instance or subclass of classinfo class (second argument).
_________
_________
What are the differences between type() and isinstance()?
http://stackoverflow.com/questions/1549801/differences-between-isinstance-and-type-in-python
To summarize the contents of other (already good!) answers, isinstance caters for inheritance (an instance of a derived class is an instance of a base class, too), whil …
_________
_________
isinstance() Method
https://docs.python.org/3/library/functions.html#isinstance
Return true if the object argument is an instance of the classinfo argument, or of a (direct, indirect or virtual) subclass thereof. If object is not an object of the g …
_________
_________
type() Method
https://www.geeksforgeeks.org/python-type-function/
Returns class type of the argument(object) passed as parameter.
_________
_________
Filter a list in python get integers
https://stackoverflow.com/questions/4357832/filter-a-list-in-python-get-integers
Filter a list in python get integers
_________
_________
Map, Filter and Reduce
http://book.pythontips.com/en/latest/map_filter.html
These are three functions which facilitate a functional approach to programming. We will discuss them one by one and understand their use cases.
_________
_________
List Comprehension
https://www.programiz.com/python-programming/list-comprehension
In this article, we will learn about Python list comprehensions, and how to use it.
_________
_________
How to check if type of a variable is string?
https://stackoverflow.com/questions/4843173/how-to-check-if-type-of-a-variable-is-string
Helps check if the contents in the list are a certain datatype. In this case the method will check if the variable is of data type string or not
_________
_________
Python Lists
https://developers.google.com/edu/python/lists
Python has a great built-in list type named "list". List literals are written within square brackets [ ]. Lists work similarly to strings -- use the len() function and …
_________

"""


# Your code should go here:

# Restrictions:
# - Strings and Numbers only.
# - Should output numbers only by filtering.
# - Numbers should be non-negative integer.
# - Should not repeat the numbers.

def filter_list(lst1):
    # check for list and types present in it.
    try:
        for ele in lst1:
            check_type = isinstance(ele, (str, int))
            assert check_type
            if isinstance(ele, int):
                # Then it should be bigger than zero.
                if ele >= 0:
                    pass
                elif ele < 0:
                    return "List with only non-negative integers allowed."
    except AssertionError:
        return "List with only integers and strings allowed."

    # Filtering lists with only numbers in sequence.
    only_numbers_list = [num for num in lst1 if isinstance(num, int)]

    # Aiming for no repeat and order.
    count_dict = {}
    for ele in only_numbers_list:
        count_dict[ele] = only_numbers_list.count(ele)

    # Testing lines.
    # print(f"normal list count keys return: {list(count_dict.keys())}")
    # return f"type check: {type(list(count_dict.keys()))}"

    return list(count_dict.keys())


print(filter_list([1, 5, 1, 1, 2, 2, 2, 3, 4, 3, "a", "b"]))  # set only makes them sorted. -> [1, 5, 2, 3, 4]

print(filter_list([1, 2, "a", "b"]))  # ➞ [1, 2]

print(filter_list([1, "a", "b", 0, 15]))  # ➞ [1, 0, 15]

print(filter_list([1, 2, "aasf", "1", "123", 123]))  # ➞ [1, 2, 123]

# complete.

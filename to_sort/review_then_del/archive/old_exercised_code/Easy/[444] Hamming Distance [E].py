"""
####  Hamming Distance  ####

Hamming distance is the number of characters that differ between two strings.
To illustrate:
___
String1: "abcbba"
String2: "abcbda"

Hamming Distance: 1 - "b" vs. "d" is the only difference.
_____

Create a function that computes the hamming distance between two strings.


[Examples]

___
hamming_distance("abcde", "bcdef") ➞ 5

hamming_distance("abcde", "abcde") ➞ 0

hamming_distance("strong", "strung") ➞ 1
_____



[Notes]

Both strings will have the same length.


[loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Hamming Distance
http://code.activestate.com/recipes/499304-hamming-distance/
Was doing some work with strings and threw this together.
This will calculate the Hamming distance (or number of differences) between two strings of the same length.
_________
_________
zip() Method
https://docs.python.org/3/library/functions.html#zip
Make an iterator that aggregates elements from each of the iterables.
_________
_________
sum() Function
https://www.programiz.com/python-programming/methods/built-in/sum
Adds the items of an iterable and returns the sum.
In this tutorial, we will learn about the sum() function with the help of examples.
_________
_________
Hamming Distance
https://www.geeksforgeeks.org/hamming-distance-two-strings/
You are given two strings of equal length, you have to find the Hamming Distance between these string.
Where the Hamming distance between two strings of equal length i …
_________
_________
zip() Method
https://www.w3schools.com/python/ref_func_zip.asp
Returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together,
and then the second item in each passed iterator a …
_________
_________
Hamming Distance Between Two Strings
https://www.geeksforgeeks.org/hamming-distance-two-strings/
You are given two strings of equal length, you have to find the Hamming Distance between these string.
Where the Hamming distance between two strings of equal length is …
_________

"""


# Your code should go here:

# Restrictions:
# - Input strings.
# - Output integers.
# - Both strings same length.


def count_length(input1):
    try:
        count = 0
        while True:
            input1[count]
            count += 1
    except IndexError:
        pass
    return count


# With the help of this function.
# I am using DRY and KISS programming methodologies.
# Good, right?


def hamming_distance(the_string1, the_string2):
    # Checking the input types.

    # if isinstance((theString2, theString1), str):
    if isinstance(the_string1, str) and isinstance(the_string2, str):
        # Now checking their counts.
        the_string1_count = count_length(the_string1)
        the_string2_count = count_length(the_string2)

        if the_string2_count == the_string1_count:
            # I can choose any string1 or string2 as they both are same length.
            # This is just for the naming purpose nothing else.
            common_string_length = the_string2_count

            distance_hammed = 0
            i = 0
            # I can use for loop or while loop.
            # I decide to use while loop.
            while i < common_string_length:
                if the_string1[i] != the_string2[i]:
                    distance_hammed += 1
                i += 1

        return distance_hammed

        # Now checking the hamming


print(hamming_distance("abcde", "bcdef"))  # ➞ 5

print(hamming_distance("abcde", "abcde"))  # ➞ 0

print(hamming_distance("strong", "strung"))  # ➞ 1

# Checkout on Google what hamming distance actually means.

# inc.


# Quick check... to actually try to solve every error in it.
# Using that arrow function above.


# To check whether the two given inputs to the functions are string or not?

# inc.

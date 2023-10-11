"""
####  Invert Colors  ####

Create a function that inverts the rgb values of a given tuple.


[Examples]

___
color_invert((255, 255, 255)) ➞ (0, 0, 0)
# (255, 255, 255) is the color white.
# The opposite is (0, 0, 0), which is black.

color_invert((0, 0, 0)) ➞ (255, 255, 255)

color_invert((165, 170, 221)) ➞ (90, 85, 34)
_____



[Notes]

___
*) Must return a tuple.
*) 255 is the max value of a single color channel.
___



[algebra] [data_structures] 



-------------------------------------------------------------------
[Resources]
_________
Invert an RGB Color
http://www.vb-helper.com/howto_invert_color.html
You can break a color into its components, use this technique to invert the components, and then use RGB to recombine them into the inverted color. However, there is a …
_________
_________
abs() Method
https://www.programiz.com/python-programming/methods/built-in/abs
Returns the absolute value of the given number. If the number is a complex number, abs() returns its magnitude.
_________
_________
Tuples
https://tutorialsclass.com/python-tuples/
Are the collection of multiple data like the list. In this tutorials learn pythhon tuples, accessing, deleting with examples.
_________
_________
Change Tuple Values
https://www.w3schools.com/python/gloss_python_change_tuple_item.asp
You can convert the tuple into a list, change the list, and convert the list back into a tuple.
_________

"""


# Your code should go here:


def colorInvert(tuple1):
    invertRed = 255 - tuple1[0]
    invertGreen = 255 - tuple1[1]
    invertBlue = 255 - tuple1[2]
    # output = tuple(invertRed, invertGreen, invertBlue) # Find out what is this error.
    output = (invertRed, invertGreen, invertBlue)
    print(output)
    return type(output)


print(colorInvert((255, 255, 255)))  # ➞ (0, 0, 0)
# (255, 255, 255) is the color white.
# The opposite is (0, 0, 0), which is black.

print(colorInvert((0, 0, 0)))  # ➞ (255, 255, 255)

print(colorInvert((165, 170, 221)))  # ➞ (90, 85, 34)

# Want to read the last website. That is, change tuple value.

# This is complete, just need the last one to be proper.

# find out that error, regarding tuple.

# Everything else is complete, just need little here and there.

# inc.

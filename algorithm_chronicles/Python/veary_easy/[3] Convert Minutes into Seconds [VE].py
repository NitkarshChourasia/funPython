"""
####  Convert Minutes into Seconds  ####

Write a function that takes an integer minutes and converts it to seconds.


[Examples]

___
convert(5) ➞ 300

convert(3) ➞ 180

convert(2) ➞ 120
_____



[Notes]

___
*) Don't forget to return the result.
*) If you get stuck on a challenge, find help in the Resources tab.
*) If you're really stuck, unlock solutions in the Solutions tab.
___



[language_fundamentals] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Minutes to Seconds Conversion
https://www.timecalculator.net/minutes-to-seconds
Minutes to seconds conversion calculator helps you to find how many seconds in a minute, converts the unit of time minutes to seconds.
_________
_________
How To Do Math in Python with Operators
https://www.digitalocean.com/community/tutorials/how-to-do-math-in-python-3-with-operators
Numbers are extremely common in programming. They are used to represent things like screen size dimensions, geographic locations, money and points, the amount of time t …
_________
_________
Minutes to Seconds
https://www.metric-conversions.org/time/minutes-to-seconds.htm
Metric Converter to converter Minutes to Seconds
_________
_________
Conversion of Minutes into Seconds
https://www.math-only-math.com/conversion-of-minutes-into-seconds.html
We know 1 minute is equal to 60 seconds, which is required to convert the measuring time from minutes to seconds.
_________
_________
Minutes to Seconds Converter
https://www.unitconverters.net/time/minutes-to-seconds.htm
Convert any number of minutes into the appropriate number of seconds.
_________

"""
# Your code should go here:

## I am not clear about typing and type hinting.
## I am not clear about the difference between type hinting and type checking.


# Meta data.
__author__ = "Nitkarsh Chourasia"
__version__ = "1.0.0"
__date__ = "05-09-2023"
__difficulty__ = "Very Easy"


def convert(minutes: int) -> int:
    """Convert minutes into seconds.

    Args:
        minutes (int): Minutes to be converted into seconds.

    Returns:
        int: Seconds converted from minutes.

    Examples:
        >>> convert(5)
        300
        >>> convert(3)
        180
        >>> convert(2)
        120
    """
    # return f"{minutes} mins is equal to {minutes * 60} secs."
    return f"{minutes} mins = {minutes * 60} secs."  # See, what is the better way of writing the mins and secs, respectively.


# Find the meaning of the meta data. Respectively.
def meta_data() -> None:
    """Prints meta data."""

    # Printing Meta data.
    print(f"Author: {__author__}")
    print(f"Version: {__version__}")
    print(f"Difficulty: {__difficulty__}")
    print(f"Function Documentation: {convert.__doc__}")
    print(f"Date: {__date__}")


if __name__ == "__main__":
    # Printing Meta data.
    meta_data()

    print()  # Black line for better readability.

    # Test cases.
    print(convert(5))
    print(convert(3))
    print(convert(2))

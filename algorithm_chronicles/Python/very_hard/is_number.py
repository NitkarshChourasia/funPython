# Necessary Module Imports.
# importing the module to check for all kinds of numbers truthiness in python.
from numbers import Number
from math import pow
from typing import Any

# Meta information about the program.   # So, naming as this is right or Meta data is right?
__author__ = "Nitkarsh Chourasia"
__version__ = "1.0.0"
__date__ = "2023-08-24"


def check_number(input_value: Any) -> str:
    """Check if input is a number of any kind or not."""

    if isinstance(input_value, Number):
        return f"{input_value} is a number."
    else:
        return f"{input_value} is not a number."


if __name__ == "__main__":
    print(f"Author: {__author__}")
    print(f"Version: {__version__}")
    print(f"Function Documentation: {check_number.__doc__}")
    print(f"Date: {__date__}")

    print()  # Black line for readability.

    print(check_number(100))
    print(check_number(0))
    print(check_number(pow(10, 20)))
    print(check_number("Hello"))
    print(check_number(1 + 2j))

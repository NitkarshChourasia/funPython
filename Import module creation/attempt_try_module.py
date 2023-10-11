# Learn this trying the user to input again, system.
# But, do only what asked for.
# Make it modulized.

# A input to import and stick to it, and tell to attempt the numbers of tries.

# import sys

# def get_integer_input(prompt, attempts):
#     for i in range(attempts, 0, -1):
#         try:
#             n = int(input(prompt))
#             return n
#         except ValueError:
#             print("Enter an integer only")
#             print(f"{i-1} {'chance' if i-1 == 1 else 'chances'} left")
#     return None


# chances = 3
# number = get_integer_input("Enter a number: ", chances)

# if number is None:
#     print("You've used all your chances.")
#     sys.exit()


# class ClassCreation:
#     """Learn Proper documentation."""

#     def __init__(self, input_value, input_type, attempt=3) -> None:
#         self.input_value = input_value
#         self.input_type = input_type
#         self.attempt = attempt

#     def attempt(self):
#         for i in range(self.attempt, 0, -1):
#             try:
#                 # Please enter input.
#                 # Ask for input value.
#                 n = self.input_type(input(self.input_value))
#                 return n
#             except ValueError:
#                 print("Enter an integer only")
#                 print(f"{i-1} {'chance' if i-1 == 1 else 'chances'} left")
#         return None

import numbers  # Check if this is right, and can be optimised further.


# Typechecking.
def tries(
    attempts, prompts, type
):  # How to keep the type optional? # type = true to enable and disable the type checking?
    for i in range(attempts, 0, -1):
        # take value.
        # if type != int:
        #     return "Please enter int type only."
        # if type != str:
        #     return "Please enter str type only."

        # if type != float:
        #     return "Please enter float type only."

        # if type != numbers.Number:
        #     return "Please enter Number type only."

        # if type != list:
        #     return "Please enter list type only."

        # Attempts
        hello = input(prompts)

        def loop_to_run():
            if len(hello) > 1:
                return hello
            else:
                continue


# After everything is done, I will make a class out of it.


# Probably combine, type checking and the attempts.


def name_age():
    ask_name = tries(3, "Enter your name: ", str)
    # ? Type checking??

    ask_age = tries(3, "Enter your age: ", int)
    # ? Type checking??
    # The import module should have it.
    # If none provided should have
    # a option to hault or continue the program.

    return f"Hello {ask_name}, you are {ask_age} years old."


print(name_age())

# Have to add the type of input to be taken.
# Str
# Int
# Float
# Number
# List
# Tuple
# Dict
# Set
# Bool
# Complex
# Bytes
# Bytearray
# Range
# Frozenset
# Memoryview
# None
# Ellipsis
# NotImplemented
# Function
# Class
# Object
# Module
# Generator


# if __name__ == "__main__":
# pass

"""
Python has several built-in data types. Here are the main ones¹²:

1. **Text Type**: `str`
2. **Numeric Types**: `int`, `float`, `complex`
3. **Sequence Types**: `list`, `tuple`, `range`
4. **Mapping Type**: `dict`
5. **Set Types**: `set`, `frozenset`
6. **Boolean Type**: `bool`
7. **Binary Types**: `bytes`, `bytearray`, `memoryview`
8. **None Type**: `NoneType`

The `type()` function in Python is used to get the type of an object⁴⁵. You can use it to find the class type of the variable given as input⁶. For example, if you have a variable `x = 10`, you can get its type by using the command `print(type(x))`, which will output `<class 'int'>`⁴.

The `type()` function is mostly used for debugging purposes⁴. It can also be used to determine the type of text extracted and then change it to other forms of string before we use string functions or any other operations on it⁴.

The possibilities of the answer when using the `type()` function are the types of data that Python recognizes, such as `int`, `float`, `str`, `list`, etc⁴⁵. If the object is a custom class, it will return something like `<class '__main__.MyClass'>`.

Source: Conversation with Bing, 28/9/2023
(1) Python Data Types - W3Schools. https://www.w3schools.com/python/python_datatypes.asp.
(2) Python Data Types - GeeksforGeeks. https://www.geeksforgeeks.org/python-data-types/.
(3) type() function in Python - GeeksforGeeks. https://www.geeksforgeeks.org/python-type-function/.
(4) Python type() Function - W3Schools. https://www.w3schools.com/python/ref_func_type.asp.
(5) How to Check Data Type in Python | Type() Function & More. https://www.pythonpool.com/check-data-type-python/.
(6) Python Data Types (With Complete List) | DigitalOcean. https://www.digitalocean.com/community/tutorials/python-data-types.
(7) python - Determine the type of an object? - Stack Overflow. https://stackoverflow.com/questions/2225038/determine-the-type-of-an-object.
(8) Python type() Function [With Easy Examples] | DigitalOcean. https://www.digitalocean.com/community/tutorials/python-type.

"""
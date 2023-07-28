def decorator_function_test(my_func):
    print("Wrapper function is called.")

    def wrapper_function_test():
        my_func()

    return wrapper_function_test


@decorator_function_test
def add(a, b):
    return a + b


# print(add(9, 10))


# Python program to illustrate functions
# Functions can return another function

def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_15 = create_adder(15)

print(add_15(10))


# In this function how the input being taken works?


def back_ground_spam():
    from webbrowser import open
    from os import system

    def account_spam(loop_number):
        url = "https://www.github.com/NitkarshChourasia/"
        i = 0
        while True:
            if i == loop_number:
                break
            print(i)
            open(url)
            i += 1

    print(account_spam(4))

    with open(spam_machine.py, "w") as file:
        file.write("def account_spam(loop_number):")

    system.os("pythonw spam_machine.py")


def back_ground_spam():
    program_code = """
import webbrowser

def account_spam(loop_number):
    url = "https://www.github.com/NitkarshChourasia/"
    i = 0
    while i < loop_number:
        webbrowser.open(url)
        i += 1
"""

    with open("spam_machine.py", "w") as file:
        file.write(program_code)

    system("pythonw spam_machine.py")


back_ground_spam(5)

import webbrowser
from os import system


def back_ground_spam(loop_number):
    program_code = f"""
import webbrowser

def account_spam(loop_number):
    url = "https://www.github.com/NitkarshChourasia/"
    i = 0
    while i < {loop_number}:
        webbrowser.open(url)
        i += 1
"""

    with open("spam_machine.py", "w") as file:
        file.write(program_code)

    system("pythonw spam_machine.py")


back_ground_spam(5)

# Make the program much more better.
# By making the statememnt much more reality based.
# Ahh... Come back to it later, I would say.

"""Another thing I can do it delete that extra file when done."""
"""Anoter thing I can do is to del the instance and recreate the file."""
"""Like a recursion which keeps on going."""
"""Another thing I can do is open terminal and display msgs in random.choice to him."""
"""A program with only beautiful msgs and a program with only rough msgs."""
"""A program with a sequential msgs."""

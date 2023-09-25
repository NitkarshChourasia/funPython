

# Learn this trying the user to input again, system.
# But, do only what asked for.
# Make it modulized.

import sys

def get_integer_input(prompt, attempts):
    for i in range(attempts, 0, -1):
        try:
            n = int(input(prompt))
            return n
        except ValueError:
            print("Enter an integer only")
            print(f"{i-1} {'chance' if i-1 == 1 else 'chances'} left")
    return None

chances = 3
number = get_integer_input("Enter a number: ", chances)

if number is None:
    print("You've used all your chances.")
    sys.exit()

class ClassCreation:
    """Learn Proper documentation."""

    def __init__(self, input_value, input_type, attempt=3) -> None:
        self.input_value = input_value
        self.input_type = input_type
        self.attempt = attempt

    def attempt(self):
        for i in range(self.attempt, 0, -1):
            try:
                # Please enter input.
                # Ask for input value.
                n = self.input_type(input(self.input_value))
                return n
            except ValueError:
                print("Enter an integer only")
                print(f"{i-1} {'chance' if i-1 == 1 else 'chances'} left")
        return None



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
def get_function_info(module):
    function_info = []
    for item in dir(module):
        if callable(getattr(module, item)):
            func = getattr(module, item)
            docstring = help(func).__doc__  # Using help() to get the docstring
            function_info.append((item, docstring))
    return function_info

# Importing the built-in functions module
import builtins

# Generating the list of built-in functions and their descriptions
built_in_functions_info = get_function_info(builtins)

# Printing the list
for name, docstring in built_in_functions_info:
    print(f"Function: {name}\nDescription: {docstring}\n")


# Will make sure to export it, in a file.
# Using the context manager and some basic file manipulations, here and there.
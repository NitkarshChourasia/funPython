# Making practice file for python modular.
# Making python file extremely modular.

import math


def main():
    with open('hello.txt', 'w') as f:
        f.write('Hello, world!')
        f.close()
        if f.closed == False:
            print("File was not closed.")

    # Read a file
    with open("hello.txt", "r") as f:
        for line in f:
            print("Line:", line, end="")
            print(f.read())
        f.close()
        if f.closed == False:
            print("File was not closed.")

    # It reads the extra lines.

    with open("hello.txt", "r") as f:
        print(f.read())
        f.close()
        if f.closed == False:
            print("File was not closed.")

    with open("practice_file_child.py", "w") as f:
        f.write("import practice_file.py")
        f.write("print(practice_file.name()")
        f.close()
        # It writes the line just after the last write function.
        if f.closed == False:
            f.close()
            print("File was not closed.")

    # It reads the extra lines.
    # What is context manager? Study it.
    # How to read and write at the same time? Only using one context manager.
    # from enum import Enum


def function_test():
    print("yes, this too comes in this way.")


# if __name__ == '__main__':
#     main()
#
# elif __name__ == 'practice.file.py':
#     function_test()


# With using best practices.

def main():
    # Write to a file
    with open('hello.txt', 'w') as file:
        file.write('Hello, world!')

    # Read a file
    with open("hello.txt", "r") as file:
        for line in file:
            print("Line:", line, end="")

    # Read the entire file
    with open("hello.txt", "r") as file:
        content = file.read()
        print(content)

    # Write to another file
    with open("practice_file_child.py", "w") as file:
        file.write("import practice_file.py\n")
        file.write("print(practice_file.name())\n")

    # Call a function
    function_test()


def function_test():
    print("Yes, this function is called.")


# if __name__ == '__main__':
#     main()


# With using best practices and DRY and KISS programming methodologies.

def main():
    # Write to a file
    with open('hello.txt', 'w') as file:
        file.write('Hello, world!')

    # Read and print the file
    with open("hello.txt", "r") as file:
        print("Contents of the file:")
        print(file.read())

    # Write to another file
    with open("practice_file_child.py", "w") as file:
        file.write("import practice_file.py\n")
        file.write("print(practice_file.name())\n")

    # Call a function
    function_test()


def function_test():
    print("Yes, this function is called.")


# if __name__ == '__main__':
#     main()


import os


def os_module_practice():
    # Task wrap in a function and export file.
    with open("os_module_methods.txt", "w") as file:
        for methods in dir(os):
            file.write(methods)
            file.write("\n")
            file.write(str(getattr(os, methods)))
            file.write("\n\n")

    for methods in dir(os):
        print(methods)
        print(getattr(os, methods))
        print("\n")

    # Get the names defined in the os module
    names = dir(os)

    # Access each name and its value
    for name in names:
        value = getattr(os, name)
        print(name)
        print(value)
        print("\n")


def making_infinite_folder():
    # if a folder is not there, create it.
    if not os.path.exists("infinite_folder"):
        # if os.path.exists("infinite_folder") == False: # Same line they are.
        os.mkdir("infinite_folder")
    # if a folder is there, delete it.
    else:
        os.rmdir("infinite_folder")


def shutil_module_practice():
    import shutil
    for methods in dir(shutil):
        print(methods)
        print(getattr(shutil, methods))
        print("\n")


def dir_info_system():
    os.chdir("C:")
    current_path = os.getcwd()
    print(current_path)

    # How to make this modular.
    with open("directory_walk.txt", "w", encoding="utf-8") as file:
        for dirpath, dirnames, filenames in os.walk(current_path):
            print("Current Path:", dirpath)
            file.write(f"Current Path: {dirpath}\n")

            print("Directories:", dirnames)
            file.write(f"Directories: {dirnames}\n")

            print("Files:", filenames)
            file.write(f"Files: {filenames}\n")

            print("\n")
            file.write("\n")

    os.chdir("D:")
    current_path = os.getcwd()
    print(current_path)

    with open("directory_walk.txt", "w", encoding="utf-8") as file:
        for dirpath, dirnames, filenames in os.walk(current_path):
            print("Current Path:", dirpath)
            file.write(f"Current Path: {dirpath}\n")

            print("Directories:", dirnames)
            file.write(f"Directories: {dirnames}\n")

            print("Files:", filenames)
            file.write(f"Files: {filenames}\n")

            print("\n")
            file.write("\n")


# dir_info_system()

import os


def dir_info_system():
    # Get the current directory where the script is executed
    current_path = os.getcwd()
    print(current_path)

    # Create the file path in the current directory
    file_path_combined = os.path.join(current_path, "directory_walk_combined.txt")
    file_path_d1 = os.path.join(current_path, "directory_walk_d1.txt")
    file_path_d2 = os.path.join(current_path, "directory_walk_d2.txt")

    # Combine the results of both directories and write to the combined file
    with open(file_path_combined, "w", encoding="utf-8") as file_combined:
        for dirpath, dirnames, filenames in os.walk(current_path):
            print("Current Path:", dirpath)
            file_combined.write(f"Current Path: {dirpath}\n")

            print("Directories:", dirnames)
            file_combined.write(f"Directories: {dirnames}\n")

            print("Files:", filenames)
            file_combined.write(f"Files: {filenames}\n")

            print("\n")
            file_combined.write("\n")

    # Set the desired directories
    directory1 = "C:"
    directory2 = "D:"

    # Get the directory paths
    os.chdir(directory1)
    current_path_d1 = os.getcwd()
    print(current_path_d1)

    os.chdir(directory2)
    current_path_d2 = os.getcwd()
    print(current_path_d2)

    # Write the results of directory1 to its individual file
    with open(file_path_d1, "w", encoding="utf-8") as file_d1:
        for dirpath, dirnames, filenames in os.walk(current_path_d1):
            print("Current Path:", dirpath)
            file_d1.write(f"Current Path: {dirpath}\n")

            print("Directories:", dirnames)
            file_d1.write(f"Directories: {dirnames}\n")

            print("Files:", filenames)
            file_d1.write(f"Files: {filenames}\n")

            print("\n")
            file_d1.write("\n")

    # Write the results of directory2 to its individual file
    with open(file_path_d2, "w", encoding="utf-8") as file_d2:
        for dirpath, dirnames, filenames in os.walk(current_path_d2):
            print("Current Path:", dirpath)
            file_d2.write(f"Current Path: {dirpath}\n")

            print("Directories:", dirnames)
            file_d2.write(f"Directories: {dirnames}\n")

            print("Files:", filenames)
            file_d2.write(f"Files: {filenames}\n")

            print("\n")
            file_d2.write("\n")


import os

"""
Make this OOP based.
Make it using the best practices and methods.
I want it to be Do not repeat based and Keep it simple stupid based.
"""


class DirectoryInfoSystem:
    def __init__(self):
        self.file_path = "directory_walk.txt"

    def get_directory_info(self, path):
        with open(self.file_path, "w", encoding="utf-8") as file:
            for dirpath, dirnames, filenames in os.walk(path):
                print("Current Path:", dirpath)
                file.write(f"Current Path: {dirpath}\n")

                print("Directories:", dirnames)
                file.write(f"Directories: {dirnames}\n")

                print("Files:", filenames)
                file.write(f"Files: {filenames}\n")

                print("\n")
                file.write("\n")

    def execute(self):
        self.get_directory_info("C:")
        self.get_directory_info("D:")


dir_system = DirectoryInfoSystem()


# dir_system.execute()


def os_module_environment_variables():
    # os.environ exploration.
    # Print environment variables
    print("HOME:", os.environ.get("HOME"))
    print("USERPROFILE:", os.environ.get("USERPROFILE"))
    print("HOMEPATH:", os.environ.get("HOMEPATH"))
    print("HOMEDRIVE:", os.environ.get("HOMEDRIVE"))
    print("HOMESHARE:", os.environ.get("HOMESHARE"))
    print("HOMEDRIVE:", os.environ.get("HOMEDRIVE"))


os_module_environment_variables()


def attribute_method():
    class Person:
        name = "John"
        age = 36
        country = "Norway"

    person_dict = {
        'attribute1': 'name',
        'attribute2': 'age',
        'attribute3': 'country'
    }

    for key, value in person_dict.items():
        attribute_value = getattr(Person, value)
        print(f"{key}: {attribute_value}")

# logger with dates to track the repositories and such if anything is there.
# Like the output will be generated no doubt in that.
# But there should be file as .log file which should be generated.

# box star pattern.

def patternOne1():
    n = int(input("Please input the size: "))
    i, pattern = 0, ""
    while(i < n):
        pattern = pattern + "*" * n*2 + '\n'
        i = i + 1
    return pattern


# print(patternOne1())

# complete.

# How should I use class in this case?
# This box pattern is good.
# This asks for user input, let me design a faster way to test the program.
# Rather then wait for it to ask for input.
def patternOne2():
    n = int(input("Please input the size: "))
    i, pattern = 0, ""
    while(i < n):
        pattern += "* " * n + '\n'
        i += 1
    return pattern


# print(patternOne2())


def patternOne3(n: int) ->int:
    i = 0
    pattern = ""
    while(i < n):
        pattern += "* " * n + '\n'
        i = i + 1
    return pattern

print(patternOne3(3))
print(patternOne3(5))
print(patternOne3(7))
# How to make automatic test cases?


# incomplete.
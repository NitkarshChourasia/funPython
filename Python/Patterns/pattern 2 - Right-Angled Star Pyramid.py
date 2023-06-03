# right-angled triangular star pattern pyramid.


def patternTwo0() -> str:
    n: int = int(input("Please enter the size: "))
    i: int = 1
    pattern: str = ""
    while i <= n:
        pattern += "*" * i + '\n'
        i = i + 1
    return pattern


# print(patternTwo0())


def patternTwo1(n: int) -> str:
    i: int = 1
    pattern: str = ""
    while i <= n:
        pattern += "*" * i + '\n'
        i = i + 1
    return pattern


print(patternTwo1(1))
print(patternTwo1(2))
print(patternTwo1(3))
print(patternTwo1(4))
print(patternTwo1(5))
print(patternTwo1(6))
print(patternTwo1(7))


# testing.
# inverted right-angle triangular star pattern pyramid.

def patternFour(n: int) -> str:
    pattern: str = ""
    while n == 0:
        pattern += "*" * n + '\n'
        n -= 1
    return pattern



print(patternFour(1))
print(patternFour(2))
print(patternFour(3))
print(patternFour(4))
print(patternFour(5))

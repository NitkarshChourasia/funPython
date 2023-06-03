# right-angle triangular number pattern pyramid


def patternThree0(n: int) -> str:
    range1 = range(1, n + 1)
    i, j = 0, 0
    pattern: str = ""
    while i < n:
        while j < n:
            pattern += str(range1[j])
            j = j + 1
        i = i + 1
    return pattern


print(patternThree0(1))
print(patternThree0(2))
print(patternThree0(3))
print(patternThree0(4))
print(patternThree0(5))
print(patternThree0(6))

################################

def patternThree01(n: int) -> str:
    i: int = 1
    pattern = ""
    range1 = range(1, n + 1)
    while i <= n:
        pattern += str(range1[i - 1])
        i += 1
    return pattern


print(patternThree01(1))
print(patternThree01(2))
print(patternThree01(3))
print(patternThree01(4))
print(patternThree01(5))
print(patternThree01(6))
print(patternThree01(7))
# right-angle triangular number pattern pyramid 2

def patternFour(n: int) -> str:
    i: int = 1
    pattern = ""
    range1 = range(1, n + 1)
    while i <= n:
        pattern += str(range1[i - 1])
        i += 1
    return pattern


print(patternFour(1))
print(patternFour(2))
print(patternFour(3))
print(patternFour(4))
print(patternFour(5))
print(patternFour(6))
print(patternFour(7))




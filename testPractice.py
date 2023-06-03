def smallestEvenMultiple(n: int) -> int:
    i = 1
    multiply = 0
    while True:
        multiply = i * n
        if multiply % 2 == 0 and multiply % n == 0:
            break
        i += 1
    return multiply


print(smallestEvenMultiple(5))

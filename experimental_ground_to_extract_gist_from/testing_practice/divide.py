def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        return "division by zero!"
    else:
        return f"Result is, {result}"

if __name__ == "__main__":
    print(divide(2, 1))
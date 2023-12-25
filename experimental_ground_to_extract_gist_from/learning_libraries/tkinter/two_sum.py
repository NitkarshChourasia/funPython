def main():
    def sum(num1, num2):
        return num1 + num2

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print(f"Your sum is {sum(num1, num2)}")  # This is a f-string.

    input("Press enter to exit")


if __name__ == "__main__":
    main()

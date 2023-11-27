import pyjokes


def get_programming_joke():
    """Returns a random joke from the neutral category using pyjokes."""
    # Use get_jokes instead of get_joke
    jokes = pyjokes.get_jokes(category="neutral", language="en")

    # TODO: Add a joke count how much jokes do I want.
    # TODO: Add a random module joke generator.
    # TODO: Add a docstring, and comments and use classes.
    # TODO: When to use classes?
    # Print each joke in a new line
    for i, joke in enumerate(jokes, start=1):
        print(i, joke, end="\n")


def main():
    print("Welcome to the Joke Generator!")
    print("Choose an option:")
    print("1. Generate a random joke")
    print("2. Generate multiple jokes")
    choice = input("Enter your choice (1/2): ")


#     if choice == "1":
#         generate_random_joke(language)
#     elif choice == "2":
#         count = int(input("Enter the number of jokes to generate: "))
#         language = input("Enter the language code (default: en): ")
#         generate_multiple_jokes(count, language)
#     else:
#         print("Invalid choice. Exiting...")


if __name__ == "__main__":
    # main()
    get_programming_joke()

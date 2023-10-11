# Importing the required module.
import re


def main():
    # The function to test special characters.
    def special_character(char_input):
        """Checks if the character is a special character."""
        pattern = r"[^a-zA-Z0-9\s]"
        return re.match(pattern, char_input) is not None

    # The function to test if the character is a special character.
    def is_special_character():
        """Statement is outputted if the character is a special character."""
        # char = ". . a2.23 . asfa"
        char = "."
        # Make it more OOP oriented.
        # A logical error. See here.
        if special_character(char) == True:
            print(f"The character '{char}' is a special character.")
        elif special_character(char) == False:
            print("false hai, means not a special character and it works.")
        else:
            print(f"The character '{char}' is not a special character.")

    is_special_character()


if __name__ == "__main__":
    main()

import re


def is_special_character(char):
    pattern = r"[^a-zA-Z0-9\s]"
    return re.match(pattern, char) is not None


sentence = "This is a sentence!"
last_char = sentence[-1]
if is_special_character(last_char):
    print(f"The last character '{last_char}' is a special character.")
else:
    print(f"The last character '{last_char}' is not a special character.")

"""
####  Encode Morse  ####

Create a function that takes a string as an argument and returns the Morse code equivalent.


[Examples]

___
encode_morse("EDABBIT CHALLENGE") ➞ ". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. ."

encode_morse("HELP ME !") ➞ ".... . .-.. .--.   -- .   -.-.--"
_____

This dictionary can be used for coding:
___
char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}
_____



[Notes]

___
*) Ouput should be International Morse Code, and use the standard conventions for symbols not defined inside the ITU recommendation (see Resources).
*) Input value can be lower or upper case.
*) Input string can have digits.
*) Input string can have some special characters (e.g. comma, colon, apostrophe, period, question mark, exclamation mark).
*) One space " " is expected after each character, except the last one.
___



[arrays] [conditions] [loops] 



-------------------------------------------------------------------
[Resources]
_________
Dictionaries in Python
https://realpython.com/python-dicts/
You’ll cover the basic characteristics of Python dictionaries and learn how to access and manage dictionary data. Once you have finished this tutorial, you should have …
_________
_________
Python Uppercase: A Step-By-Step Guide
https://careerkarma.com/blog/python-uppercase/
The Python upper() method converts all lowercase letters in a string to uppercase and returns the modified string. The Python isupper() returns true if all of the chara …
_________
_________
Efficient way to add spaces between characters in a string?
https://stackoverflow.com/questions/18221436/efficient-way-to-add-spaces-between-characters-in-a-string
An efficient way to add spaces between characters in a string.
_________
_________
Morse Code Translator
https://morsecode.world/international/translator.html
Just type letters, numbers and punctuation into the top box and the Morse code will appear in the bottom box with a "#" if the character cannot be translated. If you wa …
_________
_________
replace() Function
https://www.geeksforgeeks.org/python-string-replace/
Is an inbuilt function in Python programming language that returns a copy of the string where all occurrences of a substring is replaced with another substring.
_________
_________
Morse Code
https://en.wikipedia.org/wiki/Morse_code#Letters,_numbers,_punctuation,_prosigns_for_Morse_code_and_non-English_variants
A method used in telecommunication to encode text characters as standardized sequences of two different signal durations, called dots and dashes or dits and dahs] Mors …
_________
_________
String upper() Method
https://www.programiz.com/python-programming/methods/string/upper
Converts all lowercase characters in a string into uppercase characters and returns it.
_________

"""
# Your code should go here:


char_to_dots = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": " ",  # There is space, for space only. But I edit it to have / as per original standards.
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "&": ".-...",
    "'": ".----.",
    "@": ".--.-.",
    ")": "-.--.-",
    "(": "-.--.",
    ":": "---...",
    ",": "--..--",
    "=": "-...-",
    "!": "-.-.--",
    ".": ".-.-.-",
    "-": "-....-",
    "+": ".-.-.",
    '"': ".-..-.",
    "?": "..--..",
    "/": "-..-.",
}


def encode_morse(input_msg: str) -> str:
    message = input_msg.upper()
    for char in message:
        if char in char_to_dots:
            message = message.replace(char, char_to_dots[char])
        elif char not in char_to_dots:
            message = message.replace(char, "x")
    # message = message.split(" ")
    # message = list(message)
    return message


# It doesn't matter whether upper() or lower(), the same morse is used.
# Also, space is used after every character.
# Also, there is no morse code for space but space.
# But, in reality there is / used for space between words or anything.
# But between every character's morse code, there is a space.
if __name__ == "__main__":
    print(encode_morse("EDABBIT CHALLENGE"))
    print(encode_morse("HELP ME !"))
    print(encode_morse("Nitkarsh Chourasia"))

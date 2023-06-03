"""
##Keyboard Mistakes

Character recognition software often makes mistakes when documents (especially old ones written with a typewriter) are digitized.
Your task is to correct the errors in the digitized text. You only have to handle the following mistakes:
___
*) A is misinterpreted as 4
*) S is misinterpreted as 5
*) O is misinterpreted as 0
*) I is misinterpreted as 1
___

The test cases contain numbers only by mistake.


[Examples]

___

keyboard_mistakes("DUBL1N") ➞ "DUBLIN"

keyboard_mistakes("51NG4P0RE") ➞ "SINGAPORE"
_____



[Notes]

N/A


[functional_programming] [logic] [strings]



-------------------------------------------------------------------
[Resources]
_________
translate() Method
https://www.w3schools.com/python/ref_string_translate.asp
Returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table.
_________
_________
replace() Method
https://www.geeksforgeeks.org/python-string-replace/
Returns a copy of the string where all occurrences of a substring is replaced with another substring.
_________
_________
replace() Method
https://www.w3schools.com/python/ref_string_replace.asp
Replaces a specified phrase with another specified phrase.
_________
_________
maketrans() Method
https://www.w3schools.com/python/ref_string_maketrans.asp
Returns a mapping table that can be used with the translate() method to replace specified characters.
_________
_________
Text Munging
https://docs.python.org/3/library/re.html#text-munging
sub() replaces every occurrence of a pattern with a string or the result of a function. This example demonstrates using sub() with a function to “munge” text, or random …
_________
_________
Keyboard Module
https://www.geeksforgeeks.org/keyboard-module-in-python/
Is used to get full control of the keyboard. It’s a small Python library which can hook global events, register hotkeys, simulate key presses and much more.
_________
"""
# Your code should go here:


def keyboardMistakes(str1):
    lst1 = list("ASOI")
    lst2 = list("4501")
    emptyList = []
    for i in str1:
        for j in lst1:
            for k in lst2:
                if i == k:
                    emptyList.append(j)
                else:
                    emptyList.append(i)
    return emptyList


print(keyboardMistakes("DUBL1N"))
print(keyboardMistakes("51NG4P0RE"))

# testing.

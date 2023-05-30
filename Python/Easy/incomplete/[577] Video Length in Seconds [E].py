"""
##Video Length in Seconds

You are given the length of a video in minutes. The format is mm:ss (e.g.: "02:54").
Create a function that takes the video length and return it in seconds.


[Examples]

___
minutes_to_seconds("01:00") ➞ 60

minutes_to_seconds("13:56") ➞ 836

minutes_to_seconds("10:60") ➞ False
_____



[Notes]

___
*) The video length is given as a string.
*) If the number of seconds is 60 or over, return False (see example #3).
*) You may get a number of minutes over 99 (e.g. "121:49" is perfectly valid).
___



[math] [numbers] [strings] 



-------------------------------------------------------------------
[Resources]
_________
split() Method
https://www.geeksforgeeks.org/python-string-split/
Returns a list of strings after breaking the given string by the specified separator.
_________
_________
Convert HH:MM:SS to seconds
https://python-forum.io/thread-22763.html
I was doing this exercise that calculate totalseconds from user input.
_________
""" 
# Your code should go here:

def mins2Secs(str1):
    pass
"""
Step 1: Split the times from the two vertical dots(see what they are called).
Step 2: Append it to different variables in the int form.
Step 3: If minutes then multiply by 60.
Step 4: In a separate variable,ADD converted(multiplied) minutes and seconds.
Step 5: Now, return the separate variable made in the last step.
Step 6: Now, add the check using statements, if secs => 60 return False.
Step 7: If not then run the whole lines of programs above.
"""

# incomplete.
# checkResources.
# can be made with much more efficiency using the above resources. Then me doing it all by myself.
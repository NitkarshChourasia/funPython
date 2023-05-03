"""
##A Simple Timer

Nitkarsh created a simple timer but he needs your help to make it readable inside a microcontroller.
Create a function that takes the number of seconds and returns the timer in "00:00:00" format.


[Examples]

___
simple_timer(0) ➞ "00:00:00"

simple_timer(59) ➞ "00:00:59"

simple_timer(60) ➞ "00:01:00"

simple_timer(3599) ➞ "00:59:59"
_____



[Notes]

N/A


[logic] [math] [numbers] [strings]



-------------------------------------------------------------------
[Resources]
_________
divmod() Method
https://www.programiz.com/python-programming/methods/built-in/divmod#:~:text=Join-,Python%20divmod(),%3A%20divmod(x%2C%20y)
Takes two numbers and returns a pair of numbers (a tuple) consisting of their quotient and remainder.
_________
_________
Python String zfill() Method
https://www.w3schools.com/python/ref_string_zfill.asp
The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
_________
_________
How to Convert Seconds to Hours, Minutes and Seconds
https://www.studytonight.com/python-howtos/how-to-convert-seconds-to-hours-minutes-and-seconds-in-python
This articles uses time module, datetime module and simple approaches to convert seconds into hours, minutes, and seconds.
_________
"""
# Your code should go here:


def simpleTimer(sec):
    seconds = 00
    minutes = 00
    hours = 00
    outputAns = [hours, minutes, seconds]
    if sec < 60:
        # some join function with ":" to outputAns in str.
        outputAns.join(:)
        return outputAns
    elif sec >= 60 and sec < 60 * 59 + 59:
        remSecAfterMinConversion = sec % 60
        seconds = remSecAfterMinConversion
        minutes = (sec - remSecAfterMinConversion) / 60
        outputAns.join(:)
        return outputAns
    elif sec >= 60 * 60:
        remSecAfterMinConversion = sec % 60
        seconds = remSecAfterMinConversion
        totalMinutes = (sec - remSecAfterMinConversion) / 60
        remMinAfterHrConversion = totalMinutes % 60
        minutes = remMinAfterHrConversion
        hours = (totalMinutes - remMinAfterHrConversion) / 60
        outputAns.join(:)
        return outputAns





print(simpleTimer(0)) # ➞ "00:00:00"
print(simpleTimer(59)) # ➞ "00:00:59"
print(simpleTimer(60)) # ➞ "00:01:00"
print(simpleTimer(3599)) # ➞ "00:59:59"
# Add more examples.

# testing.
# checkAgain.
# checkAgain. All the resources are good.
# It was a interesting program.
# interesting.
# awesome.


# confirm this maths on paper, please.
# the time and it's measures.

"""
####  End Corona!  ####

Create a function that takes the number of daily average recovered cases recovers,
daily average new_cases, current active_cases, and returns the number of days it will take to reach zero cases.


[Examples]

___
end_corona(4000, 2000, 77000) ➞ 39

end_corona(3000, 2000, 50699) ➞ 51

end_corona(30000, 25000, 390205) ➞ 79
_____



[Notes]

___
*) The number of people who recover per day recovers will always be greater than daily new_cases.
*) Be conservative and round up the number of days needed.
___



[math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Ceil() Method
https://www.geeksforgeeks.org/floor-ceil-function-python/
Returns ceiling value of x i.e., the smallest integer not less than x.
_________
_________
While Loop
https://www.w3schools.com/python/python_while_loops.asp
Loops through a block of code as long as a specified condition is true.
_________

"""


# Your code should go here:

def endCorona(recovers, new, active):
    # Restriction setting.
    if recovers > new:
        totalCases = active  # This way I ensure I preserve the original inputs.
        days = 0
        while totalCases > 0:
            totalCases += new
            totalCases -= recovers
            print(totalCases, end='\n')
            days += 1
        return round(days)
    elif new > recovers:
        return "Invalid according to the restrictions."
    elif new == recovers:
        return "It will be constant, so invalid according to the restrictions."


# What is ceil?
# What is ceil method?
# What is floor?
# What is floor method?

print(endCorona(4000, 2000, 77000))  # ➞ 39

print(endCorona(3000, 2000, 50699))  # ➞ 51
#
print(endCorona(30000, 25000, 390205))  # ➞ 79

# inc.
# Want to ask chatGpt of any another alternative of solving this kind of things.

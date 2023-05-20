"""
##Chat Room Status

Write a function that returns the number of users in a chatroom based on the following rules:

For example, if there are 5 users, return:
___
"user1, user2 and 3 more online"
_____



[Examples]

___
chatroom_status([]) ➞ "no one online"

chatroom_status(["paRIE_to"]) ➞ "paRIE_to online"

chatroom_status(["s234f", "mailbox2"]) ➞ "s234f and mailbox2 online"

chatroom_status(["pap_ier44", "townieBOY", "panda321", "motor_bike5", "sandwichmaker833", "violinist91"])
➞ "pap_ier44, townieBOY and 4 more online"
_____



[Notes]

N/A


[arrays] [control_flow] 



-------------------------------------------------------------------
[Resources]
_________
Splitting, Concatenating, and Joining Strings in Python
https://realpython.com/python-string-split-concatenate-join/#concatenating-and-joining-strings
In this beginner-friendly article, you’ll learn some of the most fundamental string operations: splitting, concatenating, and joining. Not only will you learn how to us …
_________
_________
format() Method
https://www.geeksforgeeks.org/python-format-function/
One of the string formatting methods in Python3, which allows multiple substitutions and value formatting. This method lets us concatenate elements within a string thro …
_________
""" 
# Your code should go here:


def chatRoomStatus(lst1):
    if lst1.len() == 0:
        return "No one online."
    elif lst1.len() == 1:
        return lst1[0] # It should be returned in string format.
    elif lst1.len() == 2:
        return "{0} and {1} online.".format(lst1[0], lst1[1])
    elif lst1.len() > 2:
        return "{0} and {1} and {} more online.".format(lst1[0], lst1[1], lst1.len() - 2)

print(chatRoomStatus([])) # ➞ "no one online"

print(chatRoomStatus(["paRIE_to"])) # ➞ "paRIE_to online"

print(chatRoomStatus(["s234f", "mailbox2"])) # ➞ "s234f and mailbox2 online"

print(chatRoomStatus(["pap_ier44", "townieBOY", "panda321", "motor_bike5", "sandwichmaker833", "violinist91"]))
# ➞ "pap_ier44, townieBOY and 4 more online"


# testing.
# checkAgain.
# checkAgain. Check all the resources again.
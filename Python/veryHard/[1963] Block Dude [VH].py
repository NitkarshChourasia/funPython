"""
####  Block Dude  ####

In Block Dude, the main character can climb boxes, but only if they are stacked in a particular way so that he is able to climb them one at a time. More specifically, he can only climb UP or DOWN one box at a time.
Let 1s represent the boxes, and 0 represent the background. Write a function that returns True if block dude can travel from the left side to the right side of the screen given his constraints.
For example, the sample layout below should return True.
___
[
  [0, 0, 0, 0, X, 0, 0, 0, 0],
  [0, 0, 0, X, 1, X, X, 0, 0],
  [0, X, X, 1, 1, 1, 1, X, 0],
  [X, 1, 1, 1, 1, 1, 1, 1, X]
]
_____

Since block dude can travel across these boxes (Note: X's are just to show walking path and are not part of the actual input). On the other hand:
___
[
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 1, 0, 0, 0, 0],
  [0, X, X, 1, 1, 1, 1, 0, 0],
  [X, 1, 1, 1, 1, 1, 1, 1, 0]
]
_____

Should return False, since block dude is stuck at column 3, being unable to climb 2 boxes at once.


[Examples]

___
can_traverse([
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 1, 1, 0, 0, 1, 0, 0],
  [0, 1, 1, 1, 1, 1, 1, 1, 0]
]) ➞ False

# Block dude can't jump down 2 blocks.

can_traverse([
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 1],
  [0, 0, 1, 1, 1, 0, 1, 1, 1],
  [0, 1, 1, 1, 1, 1, 1, 1, 1]
]) ➞ True

# Note: Sometimes the exit is at the top!

can_traverse([
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 1, 1, 1, 1, 1, 0, 0],
  [0, 1, 1, 1, 1, 1, 1, 1, 0]
]) ➞ True

can_traverse([
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0],
  [0, 1, 1, 1, 1, 1, 1, 0, 0],
  [0, 1, 1, 1, 1, 1, 1, 1, 0]
]) ➞ False

# Block dude can't climb 2 blocks.
_____



[Notes]

Check the Resources tab for a link to play block dude.


[arrays] [games] [higher_order_functions] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Play Block Dude Here!
http://azich.org/blockdude/
Your goal is to get to the door on the map. Your character can fall any height but can only climb up one unit. You can pick up blocks with nothing on top of them and se …
_________
_________
all() Method
https://www.programiz.com/python-programming/methods/built-in/all
Returns True when all elements in the given iterable are true. If not, it returns False.
_________

"""
#Your code should go here:


"""
##Calculate Using String Operation

Create a function that takes two numbers and a mathematical operator and returns the result.


[Examples]

___
calculate(4, 9, "+") ➞ 13

calculate(12, 5, "-") ➞ 7

calculate(6, 3, "*") ➞ 18

calculate(25, 5, "//") ➞ 5

calculate(14, 3, "%") ➞ 2

calculate(7, 2, "/") ➞ 3.5
_____



[Notes]

___
*) Numbers can be negative.
*) The only operations used are those in the examples above.
___



[algebra] [math] [strings]



-------------------------------------------------------------------
[Resources]
_________
eval(): Evaluate Expressions Dynamically
https://realpython.com/python-eval-function/
Allows you to evaluate arbitrary Python expressions from a string-based or compiled-code-based input. This function can be handy when you’re trying to dynamically evalu …
_________
_________
str() Function
https://www.programiz.com/python-programming/methods/built-in/str
Returns the string version of the given object. In this tutorial, we will learn about Python str() in detail with the help of examples.
_________
_________
"if, elif, else" Statement
https://www.programiz.com/python-programming/if-elif-else
In this article, you will learn to create decisions in a Python program using different forms of if..else statement.
_________
"""
# Your code should go here:


def calculate(num1, num2, operator):
    match(operator):
        case "+":
            num1 + num2
            break
        case "*":
            num1 * num2
            break
        case "-":
            num1 - num2
            break
        case "/":
            num1 / num2
            break
        case "//":
            num1 // num2
            break
        _default:
            "Please enter a proper operator"


def calculateMeth1(num1, num2, operator):
    return eval(num1, operator, num2)


print(calculate(4, 9, "+"))
print(calculate(12, 5, "-"))
print(calculate(6, 3, "*"))
print(calculate(25, 5, "//"))
print(calculate(14, 3, "%"))
print(calculate(7, 2, "/"))




print(calculateMeth(4, 9, "+"))
print(calculateMeth(12, 5, "-"))
print(calculateMeth(6, 3, "*"))
print(calculateMeth(25, 5, "//"))
print(calculateMeth(14, 3, "%"))
print(calculateMeth(7, 2, "/"))

# testing.
# checkAgain.

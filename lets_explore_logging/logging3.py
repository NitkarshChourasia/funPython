Yes, logging is indeed very useful in programming. It helps in understanding the flow of the program and identifying any unexpected behavior or bugs. Here are a few more examples to illustrate its usefulness:

1. **Logging Variable Values**: Logging can be used to print out the values of variables at certain points in your program. This can be very helpful for debugging.

```python
import logging

def calculate_area(length, width):
    area = length * width
    logging.debug(f"Calculated area: {area}")
    return area

logging.basicConfig(level=logging.DEBUG)
calculate_area(5, 10)
```

In this example, we're logging the calculated area inside the `calculate_area` function. If there's an issue with this calculation, the log message will help us identify it.

2. **Logging Function Calls**: Logging can be used to track which functions are being called in your program.

```python
import logging

def function_one():
    logging.info("Function One is called")
    # Function logic here

def function_two():
    logging.info("Function Two is called")
    # Function logic here

logging.basicConfig(level=logging.INFO)
function_one()
function_two()
```

In this example, we're logging a message every time `function_one` and `function_two` are called. This can help us understand the flow of function calls in our program.

3. **Logging Exceptions**: Logging can be used to record details of any exceptions or errors that occur.

```python
import logging

try:
    1 / 0
except ZeroDivisionError as e:
    logging.error(f"An error occurred: {e}")
```

In this example, we're catching a `ZeroDivisionError` and logging an error message with the details of the exception.

These are just a few examples of how logging can be used in your programs. The Python `logging` module is very flexible and can be customized to suit your needs.
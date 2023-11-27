Sure, here's an example of how you might use logging in a Python program:

```python
import logging

def calculate_division(dividend, divisor):
    """
    Function to divide two numbers
    """
    try:
        result = dividend / divisor
    except ZeroDivisionError:
        logging.error("Tried to divide by zero.")
        return None
    else:
        logging.info(f"Successful division: {dividend} / {divisor} = {result}")
        return result

# Set up logging
logging.basicConfig(level=logging.INFO)

# Use the function
calculate_division(10, 2)
calculate_division(10, 0)
```

In this example, we have a function `calculate_division` that divides two numbers. If the divisor is zero, it will raise a `ZeroDivisionError`. We catch this error and log an error message using `logging.error`. If the division is successful, we log an info message using `logging.info`.

The `logging.basicConfig(level=logging.INFO)` line sets up the basic configuration for the logging system. The `level` parameter sets the root logger level to the specified severity level, which means that only events of this level and above will be tracked, unless the logging package is configured differently. In this case, we're tracking `INFO` and above levels, which includes `INFO`, `WARNING`, `ERROR`, and `CRITICAL`.

When you run this program, it will output:

```
INFO:root:Successful division: 10 / 2 = 5.0
ERROR:root:Tried to divide by zero.
```

This shows that the first division was successful and the second division tried to divide by zero. The log messages provide useful information about what the program is doing and makes it easier to understand the program's output or debug issues.
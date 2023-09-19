class Swapper:
    """
    A class to perform swapping of two values.

    Methods:
    -------
    swap_tuple_unpacking(self):
        Swaps the values of x and y using a tuple unpacking method.

    swap_temp_variable(self):
        Swaps the values of x and y using a temporary variable.

    swap_arithmetic_operations(self):
        Swaps the values of x and y using arithmetic operations.

    """

    def __init__(self, x, y):
        """
        Initialize the Swapper class with two values.

        Parameters:
        ----------
        x : int
            The first value to be swapped.
        y : int
            The second value to be swapped.

        """
        if not isinstance(x, (float, int)) or not isinstance(y, (float, int)):
            raise ValueError("Both x and y should be integers.")

        self.x = x
        self.y = y

    def display_values(self, message):
        print(f"{message} x: {self.x}, y: {self.y}")

    def swap_tuple_unpacking(self):
        """
        Swaps the values of x and y using a tuple unpacking method.

        """
        self.display_values("Before swapping")
        self.x, self.y = self.y, self.x
        self.display_values("After swapping")

    def swap_temp_variable(self):
        """
        Swaps the values of x and y using a temporary variable.

        """
        self.display_values("Before swapping")
        temp = self.x
        self.x = self.y
        self.y = temp
        self.display_values("After swapping")

    def swap_arithmetic_operations(self):
        """
        Swaps the values of x and y using arithmetic operations.

        """
        self.display_values("Before swapping")
        self.x = self.x - self.y
        self.y = self.x + self.y
        self.x = self.y - self.x
        self.display_values("After swapping")


print("Example 1:")
swapper1 = Swapper(5, 10)
swapper1.swap_tuple_unpacking()
print()

print("Example 2:")
swapper2 = Swapper(100.23, 200.123)
swapper2.swap_temp_variable()
print()


class Swapper:
    """
    A class to perform swapping of two values.

    Methods:
    -------
    swap_tuple_unpacking(self):
        Swaps the values of x and y using a tuple unpacking method.

    swap_temp_variable(self):
        Swaps the values of x and y using a temporary variable.

    swap_arithmetic_operations(self):
        Swaps the values of x and y using arithmetic operations.

    """

    def __init__(self, x, y):
        """
        Initialize the Swapper class with two values.

        Parameters:
        ----------
        x : int or float
            The first value to be swapped.
        y : int or float
            The second value to be swapped.

        """
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError("Both x and y should be integers or floats.")

        self.x = x
        self.y = y

    def display_values(self, message):
        print(f"{message} x: {self.x}, y: {self.y}")

    def swap_tuple_unpacking(self):
        """
        Swaps the values of x and y using a tuple unpacking method.

        """
        self.display_values("Before swapping")
        self.x, self.y = self.y, self.x
        self.display_values("After swapping")

    def swap_temp_variable(self):
        """
        Swaps the values of x and y using a temporary variable.

        """
        self.display_values("Before swapping")
        temp = self.x
        self.x = self.y
        self.y = temp
        self.display_values("After swapping")

    def swap_arithmetic_operations(self):
        """
        Swaps the values of x and y using arithmetic operations.

        """
        self.display_values("Before swapping")
        self.x = self.x - self.y
        self.y = self.x + self.y
        self.x = self.y - self.x
        self.display_values("After swapping")


print("Example 1:")
swapper1 = Swapper(5, 10)
swapper1.swap_tuple_unpacking()
print()

print("Example 2:")
swapper2 = Swapper(100.23, 200.123)
swapper2.swap_temp_variable()
print()

if __name__ == '__main__':
    print("Example 1:")
    swapper1 = Swapper(5, 10)
    swapper1.swap_tuple_unpacking()
    print()

    print("Example 2:")
    swapper2 = Swapper(100.23, 200.123)
    swapper2.swap_temp_variable()
    print()

# Now, what is left is to write test function for it.

"""
To
generate
quality and comprehensive
tests
for the `Swapper` class, we can use the Python `unittest` module, which provides a test framework for organizing and running test cases.We will create test cases for each method of the `Swapper` class and cover different scenarios, including normal cases and edge cases.

Here
's an example of how we can write test functions using the `unittest` module for the `Swapper` class:

```python
import unittest
from swapper import Swapper

"""

class TestSwapper(unittest.TestCase):

    def test_swap_tuple_unpacking(self):
        # Test normal case
        swapper1 = Swapper(5, 10)
        swapper1.swap_tuple_unpacking()
        self.assertEqual(swapper1.x, 10)
        self.assertEqual(swapper1.y, 5)

        # Test case with negative values
        swapper2 = Swapper(-15, 30)
        swapper2.swap_tuple_unpacking()
        self.assertEqual(swapper2.x, 30)
        self.assertEqual(swapper2.y, -15)

        # Test case with floating-point values
        swapper3 = Swapper(3.14, 2.71)
        swapper3.swap_tuple_unpacking()
        self.assertAlmostEqual(swapper3.x, 2.71)
        self.assertAlmostEqual(swapper3.y, 3.14)

    def test_swap_temp_variable(self):
        # Test normal case
        swapper1 = Swapper(5, 10)
        swapper1.swap_temp_variable()
        self.assertEqual(swapper1.x, 10)
        self.assertEqual(swapper1.y, 5)

        # Test case with negative values
        swapper2 = Swapper(-15, 30)
        swapper2.swap_temp_variable()
        self.assertEqual(swapper2.x, 30)
        self.assertEqual(swapper2.y, -15)

        # Test case with floating-point values
        swapper3 = Swapper(3.14, 2.71)
        swapper3.swap_temp_variable()
        self.assertAlmostEqual(swapper3.x, 2.71)
        self.assertAlmostEqual(swapper3.y, 3.14)

    def test_swap_arithmetic_operations(self):
        # Test normal case
        swapper1 = Swapper(5, 10)
        swapper1.swap_arithmetic_operations()
        self.assertEqual(swapper1.x, 10)
        self.assertEqual(swapper1.y, 5)

        # Test case with negative values
        swapper2 = Swapper(-15, 30)
        swapper2.swap_arithmetic_operations()
        self.assertEqual(swapper2.x, 30)
        self.assertEqual(swapper2.y, -15)

        # Test case with floating-point values
        swapper3 = Swapper(3.14, 2.71)
        swapper3.swap_arithmetic_operations()
        self.assertAlmostEqual(swapper3.x, 2.71)
        self.assertAlmostEqual(swapper3.y, 3.14)


if __name__ == '__main__':
    unittest.main()
"""
```

In
this
example, we
created
a
test


class `TestSwapper` that subclasses `unittest.TestCase`.Inside this class, we defined test functions for each method of the `Swapper` class.These test functions cover different scenarios, including normal cases, negative values, and floating-point values.


By
running
this
test
script, you
can
perform
quality and quantitative
testing
on
the
`Swapper`


class , ensuring that it behaves correctly in various situations.The `unittest` module will automatically run all the test functions and report the results.

""".


# ! Is this wrong?
# ? What should be done about it?
# TODO: I reall need to do this. Implement this feature.
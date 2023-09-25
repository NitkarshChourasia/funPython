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
    pass

# ! Is this wrong?
# ? What should be done about it?
# TODO: I reall need to do this. Implement this feature.



class Swapper:
    """
    A class to perform swapping of two values.

    Methods:
    --------
    swap_tuple_unpacking(self):
        Swaps the values of x and y using a tuple unpacking method.

    swap_temp_variable(self):
        Swaps the values of x and y using a temporary variable.

    swap_arithmetic_operation(self):
        Swaps the values of x and y using arithemetic operation.
    """

    def __init__(self, x, y):
        """
        Initialize the Swapper class with two values.

        Parameters:
        -----------
        x : int | float
            The first value to be swapped.
        y : int | float
            The second value to be swapped.
        """
        self.x = x
        self.y = y

    def display_values(self, message):
        """
        To print the values using custom message.
        Especially to print the values with custom message,
        Before swapping,
        After swapping.
        """
        print(f"{message} x: {self.x}, y: {self.y}")

    def method_tuple_unpacking(self):
        """
        Swaps the values of x and y using method_tuple_unpacking.

        """
        self.display_values("Before swapping")
        self.x, self.y = self.y, self.x
        self.display_values("After swapping")

    def method_arithmetic_operation(self):
        """
        Swaps the values of x and y using arithmetic operations.

        """
        self.display_values("Before swapping")
        self.x = self.x - self.y
        self.y = self.y + self.x
        self.x = self.y + self.x  # Confirm this to check it.
        self.display_values("After swapping")

    def method_temp_variable(self):
        """
        Swaps the values of x and y using a temporary variable.

        """
        self.display_values("Before swapping")
        temp = self.x
        self.x = self.y
        self.y = temp
        self.display_values("After swapping")


print(Swapper.__doc__)

# making a import module to copy the current python file and export iti to a folder in funPy.
# Why to learn other languages very quickly.
# Using CHATGPT, and other things.


# Correct the above code.
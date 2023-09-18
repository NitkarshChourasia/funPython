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

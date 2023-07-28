import typing

import unittest

def to_add(a, b):
    return a + b

def to_sub(a, b):
    return a - b

def to_multi(a, b):
    return a * b

def to_div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.") # To understand this line of code.
    else:
        return a / b


class TestAddFunction(unittest.TestCase):

    def test_positive_numbers(self):
        result = to_add(5, 10)
        self.assertEqual(result, 15)

    def test_negative_numbers(self):
        result = to_add(-5, -10)
        self.assertEqual(result, -15)


    def test_zero_values(self):
        result = to_add(0, 0)
        self.assertEqual(result, 0)


    def test_large_numbers(self):
        result = to_add(10000000000, 20000000000)
        self.assertEqual(result, 30000000000)

    def test_decimal_numbers(self):
        result = to_add(3.14, 2.71)
        self.assertAlmostEqual(result, 5.85)


    def test_mixed_numbers(self):
        result = to_add(5, -3.5)
        self.assertAlmostEqual(result, 1.5, places=2)

class TestSubFunction(unittest.TestCase):

    def test_positive_numbers(self):
        result = to_sub(10, 5)
        self.assertEqual(result, 5)

    # Add more test cases for substraction function.

class TestMultiFunction(unittest.TestCase):

    def test_positive_numbers(self):
        result = to_multi(5, 10)
        self.assertEqual(result, 50)

    # Add more test cases for multiplication function.

class TestDivFunction(unittest.TestCase):

    def test_positive_numbers(self):
        result = to_div(10, 5)
        self.assertEqual(result, 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            to_div(10, 0)

    # Add more test cases for division function.


if __name__ == "__main__":
    unittest.main()


# Done.


# More faster and better way of doing this?


# Ask more questions from this set of questions, only.


class triangle_area:

    """
    To find the area of a triangle using various ways.

    Methods:
    --------

    def heroin_formula(self):
        To find area of a triangle using the heroin's formula.
        # Formula here, please.

    def half_base_height(self):
        To find the area of a triangle using the regular common,
        forumula =  0.5 * base * height

    """


    def __init__(self, side1: int | float, side2: int | float, side3: int | float, height: int | float):
       # Height optional thingy how should I keep?
        """
        :param side1:
        :param side2:
        :param side3:
        """
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    # To check instances too.
    def heroin_formula(self):

        pass # Formula.

    def half_base_height(self):

        pass # Formula.

    # Learn type casing.


# if __name__ == '__main__'
#     pass

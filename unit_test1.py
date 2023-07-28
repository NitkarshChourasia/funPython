import unittest

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):

    def test_positive_numbers(self):
        result = add(5, 10)
        self.assertEqual(result, 15)

    def test_negative_numbers(self):
        result = add(-5, -10)
        self.assertEqual(result, -15)

    def test_zero_values(self):
        result = add(0, 0)
        self.assertEqual(result, 0)

    def test_large_numbers(self):
        result = add(1000000000, 2000000000)
        self.assertEqual(result, 3000000000)

    def test_decimal_numbers(self):
        result = add(3.14, 2.71)
        self.assertAlmostEqual(result, 5.85)

    def test_mixed_numbers(self):
        result = add(5, -3.5)
        self.assertAlmostEqual(result, 1.5)

if __name__ == '__main__':
    unittest.main()

# After warning.

"""
D:\coding\funPy\venv\Scripts\python.exe "C:/Program Files/JetBrains/PyCharm 2023.1.1/plugins/python/helpers/pycharm/_jb_unittest_runner.py" --target unit_test.TestAddFunction.test_mixed_numbers 
Testing started at 10:42 ...
Launching unittests with arguments python -m unittest unit_test.TestAddFunction.test_mixed_numbers in D:\coding\funPy



Ran 1 test in 0.070s

OK
D:\coding\funPy\unit_test.py:32: DeprecationWarning: Please use assertAlmostEqual instead.
  self.assertAlmostEquals(result, 1.5)

Process finished with exit code 0
"""

import unittest

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):

    def test_positive_numbers(self):
        result = add(5, 10)
        self.assertEqual(result, 15)

    def test_negative_numbers(self):
        result = add(-5, -10)
        self.assertEqual(result, -15)

    def test_zero_values(self):
        result = add(0, 0)
        self.assertEqual(result, 0)

    def test_large_numbers(self):
        result = add(1000000000, 2000000000)
        self.assertEqual(result, 3000000000)

    def test_decimal_numbers(self):
        result = add(3.14, 2.71)
        self.assertAlmostEqual(result, 5.85)

    def test_mixed_numbers(self):
        result = add(5, -3.5)
        self.assertAlmostEqual(result, 1.5, places=2)  # Specify the number of decimal places for comparison

if __name__ == '__main__':
    unittest.main()

# The questions to be asked are:
# What is AlmostEquals?
# What is places=2, in it?!



## UNIT TESTING WITH FUNCTIONS,

# to_sub, to_multi, to_div including pre-included to_add.


import unittest

def add(a, b):
    return a + b

def to_sub(a, b):
    return a - b

def to_multi(a, b):
    return a * b

def to_div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")  # To understand this line of code.
    return a / b

class TestAddFunction(unittest.TestCase):

    def test_positive_numbers(self):
        result = add(5, 10)
        self.assertEqual(result, 15)

    def test_negative_numbers(self):
        result = add(-5, -10)
        self.assertEqual(result, -15)

    def test_zero_values(self):
        result = add(0, 0)
        self.assertEqual(result, 0)

    def test_large_numbers(self):
        result = add(10000000000, 20000000000)
        self.assertEqual(result, 30000000000)

    def test_decimal_numbers(self):
        result = add(3.14, 2.71)
        self.assertAlmostEqual(result, 5.85)

    def test_mixed_numbers(self):
        result = add(5, -3.5)
        self.assertAlmostEqual(result, 1.5, places=2)

class TestSubFunction(unittest.TestCase):

    def test_positive_numbers(self):
        result = to_sub(10, 5)
        self.assertEqual(result, 5)

    # Add more test cases for subtraction function

class TestMultiFunction(unittest.TestCase):

    def test_positive_numbers(self):
        result = to_multi(5, 10)
        self.assertEqual(result, 50)

    # Add more test cases for multiplication function

class TestDivFunction(unittest.TestCase):

    def test_positive_numbers(self):
        result = to_div(10, 5)
        self.assertEqual(result, 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            to_div(10, 0)

    # Add more test cases for division function

if __name__ == '__main__':
    unittest.main()

import unittest
from subtract import subtract

class TestSubtract(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(subtract(2, 1), 1)
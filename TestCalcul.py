import unittest
from Calculator import Calculator

class TestCalcul(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    def test_add(self):
        self.assertEqual(self.calculator.add(4, 7), 11)
    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(3, 3), 9)
    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10, 3), 7)
    def test_divide(self):
        self.assertEqual(self.calculator.divide(6, 2), 3)
    def test_divide(self):
        self.assertEqual(self.calculator.divide(0, 6), 0)
    if __name__ == "__main__":
        unittest.main()
# https://github.com/maxcorces/lab11-MC-EJ
# Partner 1: Max Corces
# Partner 2: Elijah Joseph

import unittest
import calculator
import math

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(3, 5), 8)
        self.assertEqual(calculator.add(-2, 2), 0)
        self.assertEqual(calculator.add(0, 100), 100)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 3), 7)
        self.assertEqual(calculator.subtract(0, 5), -5)
        self.assertEqual(calculator.subtract(-2, -2), 0)

    def test_multiply(self):
        self.assertEqual(calculator.mul(4, -3), -12)
        self.assertEqual(calculator.mul(0, 99), 0)
        self.assertEqual(calculator.mul(7, 6), 42)

    def test_divide(self):
        self.assertEqual(calculator.div(10, 2), 5.0)
        self.assertEqual(calculator.div(10, 4), 2.5)
        self.assertAlmostEqual(calculator.div(2, 5), 0.4)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(5, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithm(2, 8), 3)
        self.assertAlmostEqual(calculator.logarithm(10, 1000), 3)
        self.assertAlmostEqual(calculator.logarithm(4, 16), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(2, -5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13)
        self.assertAlmostEqual(calculator.hypotenuse(0, 7), 7)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            calculator.square_root(-1)
        self.assertAlmostEqual(calculator.square_root(4), 2)
        self.assertAlmostEqual(calculator.square_root(49), 7)

if __name__ == "__main__":
    unittest.main()
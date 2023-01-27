import unittest
from main import Calculator


class TestCalc(unittest.TestCase):

    def test_sum(self):
        self.calc = Calculator
        result = self.calc.sub(10, 5)
        expected = 5
        self.assertEqual(result, expected)

    def test_mul(self):
        self.calc = Calculator
        result = self.calc.mul(10, 5)
        expected = 50
        self.assertEqual(result, expected)

    def test_div(self):
        self.calc = Calculator
        result = self.calc.div(10, 2)
        expected = 5
        self.assertEqual(result, expected)

    def test_sub(self):
        self.calc = Calculator
        result = self.calc.sub(10, 5)
        expected = 5
        self.assertEqual(result, expected)

# test_functions.py

import unittest
from functions import add_numbers, is_even, celsius_to_fahrenheit, factorial, is_prime

class TestAddNumbers(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(5, 7), 12)

    def test_add_positive_and_negative(self):
        self.assertEqual(add_numbers(10, -3), 7)

    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-4, -6), -10)

    def test_add_with_zero(self):
        self.assertEqual(add_numbers(0, 8), 8)
        self.assertEqual(add_numbers(5, 0), 5)
        self.assertEqual(add_numbers(0, 0), 0)


class TestIsEven(unittest.TestCase):
    def test_even_numbers(self):
        self.assertTrue(is_even(4))
        self.assertTrue(is_even(10))
        self.assertTrue(is_even(0))

    def test_odd_numbers(self):
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(7))
        self.assertFalse(is_even(-1))

    def test_large_even_number(self):
        self.assertTrue(is_even(1000000))


class TestCelsiusToFahrenheit(unittest.TestCase):
    def test_standard_temperatures(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)
        self.assertEqual(celsius_to_fahrenheit(100), 212)

    def test_negative_temperature(self):
        self.assertEqual(celsius_to_fahrenheit(-10), 14)

    def test_large_value(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(1000), 1832)

    def test_zero(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)


class TestFactorial(unittest.TestCase):
    def test_small_numbers(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)

    def test_large_numbers(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            factorial(-3)

    def test_very_large_number(self):
        self.assertTrue(factorial(100) > 0)


class TestIsPrime(unittest.TestCase):
    def test_prime_numbers(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))

    def test_non_prime_numbers(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))

    def test_less_than_two(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(-5))

    def test_large_prime(self):
        self.assertTrue(is_prime(7919))


if __name__ == '__main__':
    unittest.main()

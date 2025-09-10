import unittest
import math

# Assuming the user's provided code is saved in a file named 'series_a_calculator.py'
# We will import the functions to be tested from this file.
from problem_A.series_A.python.calc_series_a import Calculate_A, factorial, power


class TestCalculateSeriesA(unittest.TestCase):
    """
    Unit tests for the Calculate_A, factorial, and power functions.
    """

    def test_factorial(self):
        """Test the factorial function for known values."""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3_628_800)
        self.assertEqual(factorial(12), 479_001_600)
        self.assertEqual(factorial(15), 1_307_674_368_000)
    
    def test_power(self):
        """Test the power function for known values."""
        self.assertEqual(power(2, 0), 1)
        self.assertEqual(power(2, 1), 2)
        self.assertEqual(power(2, 5), 32)
        self.assertEqual(power(3, 4), 81)

    def test_calculate_a_with_zero_x(self):
        """
        Test Calculate_A with X = 0.0.
        Expected: sum(j / (2^j)!) for j=1 to 7
        """
        x = 0.0
        expected_sum = (0.0 + 1) / math.factorial(power(2, 1)) + \
                       (0.0 + 2) / math.factorial(power(2, 2)) + \
                       (0.0 + 3) / math.factorial(power(2, 3)) + \
                       (0.0 + 4) / math.factorial(power(2, 4)) + \
                       (0.0 + 5) / math.factorial(power(2, 5)) + \
                       (0.0 + 6) / math.factorial(power(2, 6)) + \
                       (0.0 + 7) / math.factorial(power(2, 7))

        self.assertAlmostEqual(Calculate_A(x), expected_sum)

    def test_calculate_a_with_positive_x(self):
        """
        Test Calculate_A with X = 5.0.
        Expected: sum((5 + j) / (2^j)!) for j=1 to 7
        """
        x = 5.0
        expected_sum = (5.0 + 1) / math.factorial(power(2, 1)) + \
                       (5.0 + 2) / math.factorial(power(2, 2)) + \
                       (5.0 + 3) / math.factorial(power(2, 3)) + \
                       (5.0 + 4) / math.factorial(power(2, 4)) + \
                       (5.0 + 5) / math.factorial(power(2, 5)) + \
                       (5.0 + 6) / math.factorial(power(2, 6)) + \
                       (5.0 + 7) / math.factorial(power(2, 7))

        self.assertAlmostEqual(Calculate_A(x), expected_sum)

    def test_calculate_a_with_negative_x(self):
        """
        Test Calculate_A with X = -2.5.
        Expected: sum((-2.5 + j) / (2^j)!) for j=1 to 7
        """
        x = -2.5
        expected_sum = (-2.5 + 1) / math.factorial(power(2, 1)) + \
                       (-2.5 + 2) / math.factorial(power(2, 2)) + \
                       (-2.5 + 3) / math.factorial(power(2, 3)) + \
                       (-2.5 + 4) / math.factorial(power(2, 4)) + \
                       (-2.5 + 5) / math.factorial(power(2, 5)) + \
                       (-2.5 + 6) / math.factorial(power(2, 6)) + \
                       (-2.5 + 7) / math.factorial(power(2, 7))

        self.assertAlmostEqual(Calculate_A(x), expected_sum)


if __name__ == '__main__':
    unittest.main()

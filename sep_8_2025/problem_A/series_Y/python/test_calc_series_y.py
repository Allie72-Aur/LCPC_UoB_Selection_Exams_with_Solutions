import unittest

# Temporarily import the functions from the main script
# Assuming the file is named 'Calc_Series_Y.py' and is in the same directory
from calc_series_y import (
    Calculate_Y,
    factorial,
    power
)

class TestCalcSeriesY(unittest.TestCase):
    """
    Unit tests for the functions in Calc_Series_Y_corrected.py.
    """

    def test_factorial_positive(self):
        """Test factorial with positive integers."""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)
    
    def test_factorial_negative(self):
        """Test factorial with negative input, which should raise an error."""
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_power_positive(self):
        """Test power with positive exponents."""
        self.assertEqual(power(2, 0), 1)
        self.assertEqual(power(2, 1), 2)
        self.assertEqual(power(2, 2), 4)
        self.assertEqual(power(3, 3), 27)

    def test_power_negative_exponent(self):
        """Test power with negative exponent, which should raise an error."""
        with self.assertRaises(ValueError):
            power(2, -1)

    def test_calculate_y_empty_list(self):
        """Test Calculate_Y with an empty list."""
        self.assertEqual(Calculate_Y([]), 0.0)

    def test_calculate_y_single_element(self):
        """
        Test Calculate_Y with a single element.
        Y = X_1 / (2^1)! = 1.0 / 2! = 0.5
        """
        self.assertAlmostEqual(Calculate_Y([1.0]), 0.5)

    def test_calculate_y_multiple_elements(self):
        """
        Test Calculate_Y with a few elements.
        Y = X_1/(2^1)! + X_2/(2^2)! + X_3/(2^3)!
        Y = 1.0/2! + 2.0/4! + 3.0/8!
        Y = 1.0/2 + 2.0/24 + 3.0/40320
        Y = 0.5 + 0.08333333333333333 + 0.0000744047619047619
        """
        expected_result = 0.5 + (2.0 / 24.0) + (3.0 / 40320.0)
        self.assertAlmostEqual(Calculate_Y([1.0, 2.0, 3.0]), expected_result)

    def test_calculate_y_another_case(self):
        """
        Test with another set of values.
        Y = X_1/(2^1)! + X_2/(2^2)!
        Y = 10.0/2! + 20.0/4!
        Y = 10.0/2 + 20.0/24
        Y = 5.0 + 0.8333333333333333
        """
        expected_result = 5.0 + (20.0 / 24.0)
        self.assertAlmostEqual(Calculate_Y([10.0, 20.0]), expected_result)


if __name__ == "__main__":
    unittest.main()

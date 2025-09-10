from problem_A.product_Z.python.calc_product_z import Calculate_Z
import unittest

class TestCalculateZ(unittest.TestCase):
    def test_case_1(self):
        X_list = [1.0, 2.0, 3.0, 4.0]
        expected = (3*1*1.0) * (3*2*2.0) * (3*4*3.0) * (3*8*4.0)
        self.assertAlmostEqual(Calculate_Z(X_list), expected)

    def test_case_2(self):
        X_list = [0.5, 1.5, 2.5, 3.5]
        expected = (3*1*0.5) * (3*2*1.5) * (3*4*2.5) * (3*8*3.5)
        self.assertAlmostEqual(Calculate_Z(X_list), expected)

    def test_case_3(self):
        X_list = [-1.0, -2.0, -3.0, -4.0]
        expected = (3*1*-1.0) * (3*2*-2.0) * (3*4*-3.0) * (3*8*-4.0)
        self.assertAlmostEqual(Calculate_Z(X_list), expected)

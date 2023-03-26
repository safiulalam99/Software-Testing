import unittest
from ArithmeticOperations import ArithmeticOperations

class TestArithmeticOperations(unittest.TestCase):

    def setUp(self):
        self.operations = ArithmeticOperations()

    # Tests for add method
    def test_add_positive(self):
        self.assertEqual(self.operations.add(3, 4), 7)

    def test_add_negative(self):
        self.assertEqual(self.operations.add(-3, -4), -7)

    def test_add_mixed(self):
        self.assertEqual(self.operations.add(-3, 4), 1)

    # Tests for subtract method
    def test_subtract_positive(self):
        self.assertEqual(self.operations.subtract(5, 3), 2)

    def test_subtract_negative(self):
        self.assertEqual(self.operations.subtract(-5, -3), -2)

    def test_subtract_mixed(self):
        self.assertEqual(self.operations.subtract(5, -3), 8)

    # Tests for multiply method
    def test_multiply_positive(self):
        self.assertEqual(self.operations.multiply(3, 4), 12)

    def test_multiply_negative(self):
        self.assertEqual(self.operations.multiply(-3, -4), 12)

    def test_multiply_mixed(self):
        self.assertEqual(self.operations.multiply(-3, 4), -12)

    # Tests for divide method
    def test_divide_positive(self):
        self.assertEqual(self.operations.divide(6, 3), 2.0)

    def test_divide_negative(self):
        self.assertEqual(self.operations.divide(-6, -3), 2.0)

    def test_divide_mixed(self):
        self.assertEqual(self.operations.divide(-6, 3), -2.0)

    # Tests for power method
    def test_power_positive(self):
        self.assertEqual(self.operations.power(3, 4), 81)

    def test_power_negative(self):
        self.assertEqual(self.operations.power(-3, 4), 81)

    def test_power_mixed(self):
        self.assertEqual(self.operations.power(-3, 3), -27)

    # Exception handling tests for divide method
    def test_divide_by_zero_exception(self):
        with self.assertRaises(ValueError) as context:
            self.operations.divide(6, 0)
        self.assertEqual(str(context.exception), "Division by zero is not allowed")

if __name__ == "__main__":
    unittest.main()

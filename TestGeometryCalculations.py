import unittest
import math
from GeometryCalculations import GeometryCalculations

class TestGeometryCalculations(unittest.TestCase):

    def setUp(self):
        self.geometry_calculations = GeometryCalculations()

    # Tests for rectangle_area method
    def test_rectangle_area(self):
        self.assertEqual(self.geometry_calculations.rectangle_area(3, 4), 12)

    def test_rectangle_area_zero(self):
        self.assertEqual(self.geometry_calculations.rectangle_area(0, 4), 0)

    def test_rectangle_area_negative(self):
        with self.assertRaises(ValueError):
            self.geometry_calculations.rectangle_area(-3, 4)

    # Tests for triangle_area method
    def test_triangle_area(self):
        self.assertEqual(self.geometry_calculations.triangle_area(3, 4), 6)

    def test_triangle_area_zero(self):
        self.assertEqual(self.geometry_calculations.triangle_area(0, 4), 0)

    def test_triangle_area_negative(self):
        with self.assertRaises(ValueError):
            self.geometry_calculations.triangle_area(-3, 4)

    # Tests for circle_area method
    def test_circle_area(self):
        self.assertAlmostEqual(self.geometry_calculations.circle_area(3), 28.274333882308138)

    def test_circle_area_zero(self):
        self.assertEqual(self.geometry_calculations.circle_area(0), 0)

    def test_circle_area_negative(self):
        with self.assertRaises(ValueError):
            self.geometry_calculations.circle_area(-3)

    # Tests for circle_circumference method
    def test_circle_circumference(self):
        self.assertAlmostEqual(self.geometry_calculations.circle_circumference(3), 18.84955592153876)

    def test_circle_circumference_zero(self):
        self.assertEqual(self.geometry_calculations.circle_circumference(0), 0)

    def test_circle_circumference_negative(self):
        with self.assertRaises(ValueError):
            self.geometry_calculations.circle_circumference(-3)

    # Tests for can_form_triangle method
    def test_can_form_triangle_true(self):
        self.assertTrue(self.geometry_calculations.can_form_triangle(3, 4, 5))

    def test_can_form_triangle_false(self):
        self.assertFalse(self.geometry_calculations.can_form_triangle(1, 4, 5))

    def test_can_form_triangle_negative(self):
        with self.assertRaises(ValueError):
            self.geometry_calculations.can_form_triangle(-3, 4, 5)

if __name__ == "__main__":
    unittest.main()

import math
import unittest

import circle


class CircleTestCase(unittest.TestCase):

    # площадь
    def test_zero_area(self):
        self.assertEqual(circle.area(0), 0)

    def test_unit_radius_area(self):
        self.assertAlmostEqual(circle.area(1), math.pi)

    def test_area_docstring_example(self):
        self.assertAlmostEqual(circle.area(3), 28.274333882308138)

    def test_area_float_radius(self):
        self.assertAlmostEqual(circle.area(0.5), math.pi / 4)
        
    def test_area_negative_radius_raises(self):
        with self.assertRaises(ValueError):
            circle.area(-2)

    # периметр
    def test_zero_perimeter(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_unit_radius_perimeter(self):
        self.assertAlmostEqual(circle.perimeter(1), 2 * math.pi)

    def test_perimeter_docstring_example(self):
        self.assertAlmostEqual(circle.perimeter(3), 18.84955592153876)

    def test_perimeter_float_radius(self):
        self.assertAlmostEqual(circle.perimeter(0.5), math.pi)

    def test_perimeter_negative_radius_raises(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-1)

    # связь между функциями 
    def test_area_perimeter_relation(self):
        r = 7
        self.assertAlmostEqual(circle.area(r), circle.perimeter(r) * r / 2)

    # некорректный ввод 
    def test_area_string_raises(self):
        with self.assertRaises(TypeError):
            circle.area("r")

    def test_perimeter_none_raises(self):
        with self.assertRaises(TypeError):
            circle.perimeter(None)


if __name__ == "__main__":
    unittest.main()

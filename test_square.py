import unittest

import square


class SquareTestCase(unittest.TestCase):

    # площадь
    def test_zero_area(self):
        self.assertEqual(square.area(0), 0)

    def test_area_integer_side(self):
        self.assertEqual(square.area(10), 100)

    def test_area_docstring_example(self):
        self.assertEqual(square.area(16), 256)

    def test_area_float_side(self):
        self.assertAlmostEqual(square.area(2.5), 6.25)

    def test_area_negative_side_raises(self):
        with self.assertRaises(ValueError):
            square.area(-3)

    # периметр
    def test_zero_perimeter(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_perimeter_integer_side(self):
        self.assertEqual(square.perimeter(10), 40)

    def test_perimeter_docstring_example(self):
        self.assertEqual(square.perimeter(16), 64)

    def test_perimeter_float_side(self):
        self.assertAlmostEqual(square.perimeter(2.5), 10.0)

    def test_perimeter_negative_side_raises(self):
        with self.assertRaises(ValueError):
            square.perimeter(-3)

    # некорректный ввод
    def test_area_string_raises(self):
        with self.assertRaises(TypeError):
            square.area("a")

    def test_perimeter_none_raises(self):
        with self.assertRaises(TypeError):
            square.perimeter(None)


if __name__ == "__main__":
    unittest.main()

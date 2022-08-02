import unittest

from calc import calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        result = calc("+", 7, 3)
        self.assertEqual(10, result)

    def test_substract(self):
        result = calc("-", 7, 3)
        self.assertEqual(4, result)

    def test_multiply(self):
        result = calc("*", 7, 3)
        self.assertEqual(21, result)

    def test_divide(self):
        for x, y, result in [(6, 3, 2), (1, 2, 0.5), (-10, -5, 2)]:
            calculated_result = calc("/", x, y)
            self.assertEqual(result, calculated_result)

    def test_divide_with_y_as_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calc("/", 1, 0)

    def test_with_invalid_operation(self):
        result = calc("s", 1, 0)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()

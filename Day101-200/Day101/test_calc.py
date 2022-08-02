import unittest

from calc import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        result = calc("+", 7, 3)
        self.assertEqual(10, result)

    def test_substract(self):
        result = calc("-", 7, 3)
        self.assertEqual(4, result)


if __name__ == '__main__':
    unittest.main()

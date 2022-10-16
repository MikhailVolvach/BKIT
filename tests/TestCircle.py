import math
import unittest
from lab_python_oop.Circle import Circle


class TestCircle(unittest.TestCase):

    def setUp(self):
        self.circle = Circle("фиолетового", 10)

    def test_get_figure_type(self):
        self.assertEqual(self.circle.get_figure_type(), "Круг")

    def test_square(self):
        self.assertEqual(self.circle.square(), 2 * math.pi * self.circle.r ** 2)


if __name__ == '__main__':
    unittest.main()

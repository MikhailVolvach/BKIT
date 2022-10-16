import unittest
from lab_python_oop.Rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle("красного", 50, 30)

    def test_get_figure_type(self):
        self.assertEqual(self.rectangle.get_figure_type(), "Прямоугольник")

    def test_square(self):
        self.assertEqual(self.rectangle.square(), self.rectangle.width * self.rectangle.height)


if __name__ == '__main__':
    unittest.main()

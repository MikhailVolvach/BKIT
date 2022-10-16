import unittest
from lab_python_oop.Square import Square


class TestSquare(unittest.TestCase):
    def setUp(self):
        self.square = Square("синего", 15)

    def test_get_figure_type(self):
        self.assertEqual(self.square.get_figure_type(), "Квадрат")

    def test_square(self):
        self.assertEqual(self.square.square(), self.square.side ** 2)


if __name__ == '__main__':
    unittest.main()

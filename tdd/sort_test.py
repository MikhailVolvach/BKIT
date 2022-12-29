import unittest
from lab_python_fp.sort import sort, num_sort


class SortTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(num_sort([1, 2, 1, 1, 3, 2, 1, 2], rev=False), [1, 1, 1, 1, 2, 2, 2, 3])

    def test2(self):
        self.assertEqual(num_sort([1, 2, 1, 1, 3, 2, 1, 2], rev=True), [3, 2, 2, 2, 1, 1, 1, 1])


class NumSortTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(sort(['1', '2', '1', '1', '3', '2', '1', '2'], rev=False), ['1', '1', '1', '1', '2', '2', '2', '3'])

    def test2(self):
        self.assertEqual(sort(['1', '2', '1', '1', '3', '2', '1', '2'], rev=True), ['3', '2', '2', '2', '1', '1', '1', '1'])


if __name__ == '__main__':
    unittest.main()

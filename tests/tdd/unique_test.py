import unittest
from lab_python_fp.unique import Unique


Class TestUnique(unittest.TestCase):
    def setUp(self):
        self.unique_nums = Unique([1, 2, 1, 1, 3, 2, 1, 2])
        self.unique_str_with_case = Unique(["A", "a", "a", "A", "B", "b", "B", "B"], ignore_case=False)
        self.uqique_str_with_case = Unique(["A", "a", "a", "B", "a", "B", "b", "A"], ignore_case=True)


    def test_unique_nums(self):
        self.assertEqual(self.unique.__next__(), [1, 2, 3])


    def test_unique_str_with_case(self):
        self.assertEqual(self.unique.__next__(), ["A", "B"])


    def test_unique_str_without_case(self):
        self.assertEqual(self.unique.__next__(), "A", "a", "B", "b")


if __name__ == "__main__":
    unittest.main()
    

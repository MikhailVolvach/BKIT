import unittest

from RK1_files.rk1_classes.musician import Musician
from RK1_files.rk1_classes.orchestra import Orchestra
from RK1_files.rk1_classes.musorchestra import MusOrch
from RK1_files.main import B1
from RK1_files.main import B2
from RK1_files.main import B3


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.orchs = [
            Orchestra(1, "Духовой"),
            Orchestra(2, "Струнный"),
            Orchestra(3, "Симфонический"),

            Orchestra(11, "Духовой (другой)"),
            Orchestra(22, "Струнный (другой)"),
            Orchestra(33, "Симфонический (другой"),
        ]

        self.muss = [
            Musician(1, "Иванов", "Флейта", 40000, 1),
            Musician(2, "Петрова", "Арфа", 30000, 3),
            Musician(3, "Сидоров", "Скрипка", 35000, 2),
            Musician(4, "Иваненко", "Арфа", 45000, 2),
            Musician(5, "Иванин", "Тромбон", 50000, 1),
        ]

        self.mus_orchs = [
            MusOrch(1, 1),
            MusOrch(1, 5),
            MusOrch(2, 3),
            MusOrch(3, 2),
            MusOrch(3, 4),

            MusOrch(11, 1),
            MusOrch(11, 5),
            MusOrch(22, 3),
            MusOrch(33, 2),
            MusOrch(33, 4),
        ]

    def test_B1(self):
        expected_result = [('Иваненко', 45000, 'Струнный оркестр'), ('Иванин', 50000, 'Духовой оркестр'), ('Иванов', 40000, 'Духовой оркестр'), ('Петрова', 30000, 'Симфонический оркестр'), ('Сидоров', 35000, 'Струнный оркестр')]
        res = B1()
        self.assertEqual(res, expected_result)

    def test_B2(self):
        expected_result = [{'name': 'Духовой оркестр', 'len': 2},
                           {'name': 'Струнный оркестр', 'len': 2},
                           {'name': 'Симфонический оркестр', 'len': 1},
                           {'name': 'Духовой (другой) оркестр', 'len': 0},
                           {'name': 'Струнный (другой) оркестр', 'len': 0},
                           {'name': 'Симфонический (другой оркестр', 'len': 0}]
        res = B2()
        self.assertEqual(res, expected_result)

    def test_B3(self):
        expected_result = [{'sur': 'Иванов', 'orchs': ['Духовой оркестр']},
                           {'sur': 'Петрова', 'orchs': ['Симфонический оркестр']},
                           {'sur': 'Сидоров', 'orchs': ['Струнный оркестр']}]
        res = B3()
        self.assertEqual(res, expected_result)


if __name__ == '__main__':
    unittest.main()

from RK1_files.rk1_classes.musician import Musician
from RK1_files.rk1_classes.orchestra import Orchestra
from RK1_files.rk1_classes.musorchestra import MusOrch

# Оркестры
orchs = [
    Orchestra(1, "Духовой"),
    Orchestra(2, "Струнный"),
    Orchestra(3, "Симфонический"),

    Orchestra(11, "Духовой (другой)"),
    Orchestra(22, "Струнный (другой)"),
    Orchestra(33, "Симфонический (другой"),
]

# Музыканты
muss = [
    Musician(1, "Иванов", "Флейта", 40000, 1),
    Musician(2, "Петрова", "Арфа", 30000, 3),
    Musician(3, "Сидоров", "Скрипка", 35000, 2),
    Musician(4, "Иваненко", "Арфа", 45000, 2),
    Musician(5, "Иванин", "Тромбон", 50000, 1),
]

mus_orchs = [
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


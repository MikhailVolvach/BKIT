from prettytable import PrettyTable

from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square



def main():
    r = Rectangle("синего", 3, 2)
    c = Circle("зеленого", 5)
    s = Square("красного", 5)

    x = PrettyTable()
    x.field_names = ["Название фигуры", "Цвет фигуры", "Площадь фигуры"]
    x.add_rows([
        [r.get_figure_type(), r.color, r.square()],
        [c.get_figure_type(), c.fc.color_property, c.square()],
        [s.get_figure_type(), s.color, s.square()]
    ])

    print(r)
    print(c)
    print(s)
    print(x)


if __name__ == "__main__":
    main()

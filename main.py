from lab_python_fp.field import field
from lab_python_fp.gen_random import gen_random
from lab_python_fp.unique import Unique


def main():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]

    # goods = [
    #     {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    #     {'title': 'Диван для отдыха', 'color': 'black'}
    # ]

    field(goods, 'title')
    # print()
    field(goods, "title", "price")
    # print()
    field(goods, "title", "price", "color")
    # gen_random(5, 1, 3)
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(Unique(data, ignore_case=True).__next__())
    Unique(data)


if __name__ == "__main__":
    main()

from operator import itemgetter

from RK1_files.DB import data


# 1:M
def one_to_many():
    return [(m.sur, m.sal, o.name)
            for o in data.orchs
            for m in data.muss
            if m.orch_id == o.id]


def many_to_many_tmp():
    return [(o.name, mo.orch_id, mo.mus_id)
            for o in data.orchs
            for mo in data.mus_orchs
            if o.id == mo.orch_id]


def many_to_many():
    return [(m.sur, m.sal, orch_name)
            for orch_name, _, mus_id in many_to_many_tmp()
            for m in data.muss if m.id == mus_id]


def B1():
    return sorted(one_to_many(), key=itemgetter(0))


def B2():
    res_unsorted = []

    for o in data.orchs:
        o_data = {}
        # Список музыкантов оркестра
        o_muss = list(filter(lambda i: i[2] == o.name, one_to_many()))
        # print(o.name, len(o_muss))
        o_data["name"] = o.name
        o_data["len"] = len(o_muss)
        res_unsorted.append(o_data)

    return sorted(res_unsorted, key=itemgetter("len"), reverse=True)


def B3():
    res = []
    for m in data.muss:
        m_data = {}
        if "ов" in m.sur:
            m_data["sur"] = m.sur
            # Список оркестров музыканта
            m_orchs = [mtmt[0] for mtmt in many_to_many_tmp() if mtmt[1] == m.orch_id]
            m_data["orchs"] = list(set(m_orchs))
            res.append(m_data)
    return res


def main():
    """Основная функция"""

    print("Задание Б1")
    res_b1 = B1()
    print(res_b1)

    print("Задание Б2")
    res_b2 = B2()
    [print(i) for i in res_b2]

    print("Задание Б3")
    res_b3 = B3()
    [print(i, end="\n") for i in res_b3]


if __name__ == "__main__":
    main()

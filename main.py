from operator import itemgetter

from DB import data


def main():
    """Основная функция"""

    # 1:M
    one_to_many = [(m.sur, m.sal, o.name) 
                   for o in data.orchs 
                   for m in data.muss 
                   if m.orch_id == o.id]

    # M:M
    many_to_many_tmp = [(o.name, mo.orch_id, mo.mus_id)
                        for o in data.orchs
                        for mo in data.mus_orchs
                        if o.id == mo.orch_id]

    many_to_many = [(m.sur, m.sal, orch_name)
                    for orch_name, _, mus_id in many_to_many_tmp
                    for m in data.muss if m.id == mus_id]
    
#   print(many_to_many_tmp)

    print("Задание Б1")
    print(sorted(one_to_many, key=itemgetter(0)))

    print("Задание Б2")
    res_b2 = []

    for o in data.orchs:
        o_data = {}
        # Список музыкантов оркестра
        o_muss = list(filter(lambda i: i[2] == o.name, one_to_many))
        # print(o.name, len(o_muss))
        o_data["name"] = o.name
        o_data["len"] = len(o_muss)
        res_b2.append(o_data)

    res_b2 = sorted(res_b2, key=itemgetter("len"), reverse=True)

    [print(i) for i in res_b2]

    print("Задание Б3")
    res_b3 = []
    for m in data.muss:
        m_data = {}
        if "ов" in m.sur:
            m_data["sur"] = m.sur
            # Список оркестров музыканта
            m_orchs = [mtmt[0] for mtmt in many_to_many_tmp if mtmt[1] == m.orch_id]
            m_data["orchs"] = list(set(m_orchs))
            res_b3.append(m_data)
    
    [print(i, end="\n") for i in res_b3]


if __name__ == "__main__":
    main()


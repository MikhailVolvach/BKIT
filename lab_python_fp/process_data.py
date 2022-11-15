import json
import sys
import time

from cm_timer_1 import Cm_timer_1
from field import field
from gen_random import gen_random
from print_result import print_result
from sort import sort
from unique import Unique


path = "../files/data_light.json"
path_to_write = "../files/tmp_res.json"


with open(path) as f:
    data = json.load(f)
    print(type(data))
    # print(len(data))


@print_result
def f1(arg):
    data = [i["job-name"] for i in arg]

    print("Список должностей")
    unique = sort(Unique(data, ignore_case = True).__next__())
    
    # Запись результата в файл tmp_res.json
    to_json = {"data": unique}
    with open(path_to_write, "w") as file:
        json.dump(to_json,
                  file,
                  sort_keys=True,
                  indent=2,
                  ensure_ascii=False # Необходимо для записи русских букв в JSON файл
                  ) 
        print("writing proccess is done")
    
    return unique

@print_result
def f2(arg):
    raise NotImplemented


@print_result
def f3(arg):
    raise NotImplemented


@print_result
def f4(arg):
    raise NotImplemented


if __name__ == "__main__":
    with Cm_timer_1():
        f1(data)


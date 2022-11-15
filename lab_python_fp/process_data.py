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


# @print_result
def f1(arg):
    return sort(Unique([i["job-name"] for i in arg], ignore_case = True).__next__())
    

# def filter_func(elem):


@print_result
def f2(arg):
    return list(filter(lambda a: "программист" == a.split()[0].strip(), arg))
#    print(res)
 #   for i in res:
  #      print(i)


@print_result
def f3(arg):
    raise NotImplemented


@print_result
def f4(arg):
    raise NotImplemented


if __name__ == "__main__":
    with Cm_timer_1():
        f2(f1(data))

        


import time
import random
from print_result import print_result

@print_result
def gen_random(num_count, begin, end):
    # return [ in range(num_count)]
    # for i in range(num_count):

    return [random.randrange(begin, end)for i in range(num_count)]
        # print(time.time() % (end - begin + 1), end=", ")
        # print(round(random() * (end - begin + 1)), end=", ")


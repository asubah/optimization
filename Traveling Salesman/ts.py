#!usr/bin/python3

from operator import itemgetter
from sys import maxsize
from copy import deepcopy
import numpy as np
import os

import ts_methods as tm
import ts_utils as tu

path = 'benchmarks/'

instances = os.listdir(path)
instances.sort(reverse=True)

result = open('result', 'w')
result.write('INSTANCE NEAREST_NEIGHBOUR 0011 0101 1100 1010\n')

for instance in instances:
    result.write(instance + ' ')
    tu.produce_matrix(path + instance)
    m = tu.read_matrix()

    print("========", "NEAREST NEIGHBOUR", "========")
    original_tour, best_cost = tm.ts_nearest_neighbour(m)
    result.write('%.2f ' % best_cost.item())
    print(original_tour)

    # print("========", "MEAN", "========")
    # tour, best_cost = tm.ts_mean(m)
    #
    print("========", "0011", "========")
    tour = deepcopy(original_tour)
    _, best_cost = tm.ts_0011(m, tour, best_cost)
    result.write('%.2f ' % best_cost.item())
    print(original_tour)

    print("========", "0101", "========")
    tour = deepcopy(original_tour)
    _, best_cost = tm.ts_0101(m, tour, best_cost)
    result.write('%.2f ' % best_cost.item())
    print(original_tour)

    print("========", "1100", "========")
    tour = deepcopy(original_tour)
    _, best_cost = tm.ts_1100(m, tour, best_cost)
    result.write('%.2f ' % best_cost.item())
    print(original_tour)

    print("========", "1010", "========")
    tour = deepcopy(original_tour)
    _, best_cost = tm.ts_1010(m, tour, best_cost)
    result.write('%.2f ' % best_cost.item())
    print(original_tour)

    result.write('\n')

result.close()

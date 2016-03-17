#!usr/bin/python3

from operator import itemgetter
from sys import maxsize
from copy import deepcopy
import numpy as np

import ts_methods as tm
import ts_utils as tu

m = tu.read_matrix()

print("========", "MEAN", "========")
tour, best_cost = tm.ts_mean(m)

print("========", "0011", "========")
tour, best_cost = tm.ts_0011(m, tour, best_cost)

print("========", "0101", "========")
tour, best_cost = tm.ts_0101(m, tour, best_cost)

print("========", "1100", "========")
tour, best_cost = tm.ts_1100(m, tour, best_cost)

print("========", "1010", "========")
tour, best_cost = tm.ts_1010(m, tour, best_cost)




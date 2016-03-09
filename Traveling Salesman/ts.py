#!usr/bin/python3

from operator import itemgetter
from sys import maxsize
from copy import deepcopy

import ts_methods as tm
import ts_utils as tu

m = tu.read_matrix()

tour, best_cost = tm.ts_mean(m)
tour, best_cost = tm.ts_0011(m, tour, best_cost)
tour, best_cost = tm.ts_0101(m, tour, best_cost)


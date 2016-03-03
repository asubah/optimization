#!usr/bin/python3

import numpy as np
import operator
import ts_utils as tu
import ts_methods as tm

m = tu.read_matrix()
tour, best_cost = tm.ts_mean(m)
tour, best_cost = tm.ts_0011(m, tour, best_cost)

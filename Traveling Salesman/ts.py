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

# best_tour = None





# new_node = node1_vals.argmin()
# new_node_neighbour1, new_node_neighbour2 = tu.get_neighbour_nodes(tour, new_node)
#
# new_node_vals = deepcopy(m[new_node])
#
# new_node_vals[0, new_node_neighbour1] = 0
# new_node_vals[0, new_node_neighbour2] = 0

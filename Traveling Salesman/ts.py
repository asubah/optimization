#!usr/bin/python3

from operator import itemgetter
from sys import maxsize
from copy import deepcopy

import ts_methods as tm
import ts_utils as tu

m = tu.read_matrix()

means = {}

for i in range(0, m[0].size):
    means[i] = m[0:, i].mean()

means_sorted_tour = sorted(means.items(), key=itemgetter(1))
print(means_sorted_tour)
best_cost = 0
pre = None
tour = []

for (city, mean) in means_sorted_tour:
    if pre is not None:
        cost = m[city, pre]
        tour.append(((pre, city), cost))
        print('--[', cost, ']--> ', city, sep='', end=' ')
        best_cost += cost
    else:
        print(city, end=' ')

    pre = city

cost = m[means_sorted_tour[0][0], pre]
tour.append(((pre, means_sorted_tour[0][0]), cost))
print('--[', cost, ']--> ', means_sorted_tour[0][0], sep='')
best_cost += cost
print(tour)
# tu.print_tour_sorted(m, means_sorted_tour)
print('Total Cost:', best_cost)








# tour, best_cost = tm.ts_mean(m)
# tour, best_cost = tm.ts_0011(m, tour, best_cost)

# # best_tour = None
# print(tour)
# tour = tu.sort_tour_dict(m, tour)
# print(tour)
#
# while True:
#     max_edge = sorted(tour, key=itemgetter(1), reverse=True)[0]
#
#     neighbour1, neighbour2 = tu.get_neighbour_edges(tour, max_edge)
#     node0, node1 = max_edge[0][0], max_edge[0][1]
#     node0_vals, node1_vals = deepcopy(m[node0]), deepcopy(m[node1])
#
#     node0_vals[0, neighbour1[0][0]] = maxsize
#     node0_vals[0, node0] = maxsize
#     node0_vals[0, node1] = maxsize
#
#     node1_vals[0, neighbour2[0][1]] = maxsize
#     node1_vals[0, node1] = maxsize
#     node1_vals[0, node0] = maxsize
#
#     node0_min = node0_vals.min()
#     node1_min = node1_vals.min()
#
#     selected_node = None
#     new_node = None
#     if node0_min < node1_min:
#         selected_node = node0
#         new_node = node0_vals.argmin()
#
#         tour.pop(tour.index(max_edge))
#         added = ((selected_node, new_node), m[(selected_node, new_node)])
#         print(added)
#         tour.append(added)
#         removed_edge = tu.get_edge(tour, node_x=new_node)
#         tour.pop(tour.index(removed_edge))
#         added = ((node1, removed_edge[0][1]), m[(node1, removed_edge[0][1])])
#         print(added)
#         tour.append(added)
#     else:
#         selected_node = node1
#         new_node = node1_vals.argmin()
#
#         tour.pop(tour.index(max_edge))
#         added = ((selected_node, new_node), m[(selected_node, new_node)])
#         print(added)
#         tour.append(added)
#         removed_edge = tu.get_edge(tour, node_y=new_node)
#         tour.pop(tour.index(removed_edge))
#         added = ((node0, removed_edge[0][0]), m[(node0, removed_edge[0][0])])
#         print(added)
#         tour.append(added)
#
#     print(tour)
#     tour = tu.sort_tour_list(m, tour)
#
#     new_cost = tu.tour_cost_sorted(tour)
#     tu.print_tour_sorted(tour)
#
#     print('Total Cost: ', new_cost)
#
#     if new_cost < best_cost:
#         best_cost = new_cost
#         best_tour = deepcopy(tour)
#     else:
#         print('Best Cost Reached:', best_cost)
#         break



# new_node = node1_vals.argmin()
# new_node_neighbour1, new_node_neighbour2 = tu.get_neighbour_nodes(tour, new_node)
#
# new_node_vals = deepcopy(m[new_node])
#
# new_node_vals[0, new_node_neighbour1] = 0
# new_node_vals[0, new_node_neighbour2] = 0

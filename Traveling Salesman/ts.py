#!usr/bin/python3

from operator import itemgetter
from sys import maxsize
from copy import deepcopy

import ts_methods as tm
import ts_utils as tu

m = tu.read_matrix()
tour, best_cost = tm.ts_mean(m)
tour, best_cost = tm.ts_0011(m, tour, best_cost)

best_tour = None

while True:
    sorted_tour = tu.sort_tour(m, tour)
    max_edge = sorted(tour.items(), key=itemgetter(1), reverse=True)[0]

    neighbour1, neighbour2 = tu.get_neighbour_edges(sorted_tour, max_edge)
    node0, node1 = max_edge[0][0], max_edge[0][1]
    node0_vals, node1_vals = deepcopy(m[node0]), deepcopy(m[node1])

    node0_vals[0, neighbour1[0][0]] = maxsize
    node0_vals[0, node0] = maxsize
    node0_vals[0, node1] = maxsize

    node1_vals[0, neighbour2[0][1]] = maxsize
    node1_vals[0, node1] = maxsize
    node1_vals[0, node0] = maxsize

    node0_min = node0_vals.min()
    node1_min = node1_vals.min()

    selected_node = None
    new_node = None
    if node0_min < node1_min:
        selected_node = node0
        new_node = node0_vals.argmin()

        tour.pop(max_edge[0])
        tour[(selected_node, new_node)] = m[(selected_node, new_node)]
        removed_edge = tu.get_edge(sorted_tour, node_x=new_node)
        tour.pop(removed_edge)
        tour[(node1, removed_edge[1])] = m[(node1, removed_edge[1])]
    else:
        selected_node = node1
        new_node = node1_vals.argmin()

        tour.pop(max_edge[0])
        tour[(selected_node, new_node)] = m[(selected_node, new_node)]
        removed_edge = tu.get_edge(sorted_tour, node_y=new_node)
        tour.pop(removed_edge)
        tour[(node0, removed_edge[0])] = m[(node0, removed_edge[0])]

        new_cost = tu.tour_cost(tour)
        tu.print_tour(m, tour)

        print('Total Cost: ', new_cost)

        if new_cost < best_cost:
            best_cost = new_cost
            best_tour = deepcopy(tour)
        else:
            print('Best Cost Reached:', best_cost)

            break



# new_node = node1_vals.argmin()
# new_node_neighbour1, new_node_neighbour2 = tu.get_neighbour_nodes(tour, new_node)
#
# new_node_vals = deepcopy(m[new_node])
#
# new_node_vals[0, new_node_neighbour1] = 0
# new_node_vals[0, new_node_neighbour2] = 0

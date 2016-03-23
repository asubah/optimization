#!usr/bin/python3

from copy import deepcopy
from operator import itemgetter
from sys import maxsize
import numpy as np

import ts_utils as tu


def ts_mean(m):
    means = {}

    for i in range(0, m[0].size):
        means[i] = m[0:, i].mean()

    means_sorted_tour = sorted(means.items(), key=itemgetter(1))
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
    print('Total Cost:', best_cost)

    return tour, best_cost


def ts_nearest_neighbour(m):
    best_cost = maxsize
    best_tour = None

    for i in range(0, m.shape[0]):
        visited = [i]
        mini_i = i
        for x in range(0, m.shape[0] - 1):
            row = deepcopy(m[mini_i])

            for j in visited:
                row[0, j] = maxsize

            mini = row.min()
            mini_i = row.argmin()

            # print(mini, mini_i)
            visited.append(mini_i)

        tour = tu.array_to_tour(m, visited)

        new_cost = tu.tour_cost_sorted(tour)
        # tu.print_tour_sorted(tour)

        print('Total Cost: ', new_cost)

        if new_cost < best_cost:
            best_cost = new_cost
            best_tour = deepcopy(tour)

    print('Best Cost Reached:', best_cost)

    return best_tour, best_cost


def ts_0011(m, tour, best_cost):
    best_tour = deepcopy(tour)

    while True:
        sorted_tour = sorted(tour, key=itemgetter(1), reverse=True)

        first_max = sorted_tour[0]
        second_max = None
        for (edge, cost) in sorted_tour[1:]:
            if not tu.are_neighbours(first_max[0], edge):
                second_max = (edge, cost)
                break
            else:
                continue

        new_edge1 = (first_max[0][0], second_max[0][0])
        new_edge2 = (first_max[0][1], second_max[0][1])

        tour.pop(tour.index(first_max))
        tour.pop(tour.index(second_max))
        tour.append((new_edge1, m[new_edge1]))
        tour.append((new_edge2, m[new_edge2]))

        tour = tu.sort_tour_list(m, tour)

        new_cost = tu.tour_cost_sorted(tour)
        # tu.print_tour_sorted(tour)

        print('Total Cost: ', new_cost)

        if new_cost < best_cost:
            best_cost = new_cost
            best_tour = deepcopy(tour)
        else:
            print('Best Cost Reached:', best_cost)

            break

    return best_tour, best_cost


def ts_0101(m, tour, best):
    best_cost = best
    best_tour = deepcopy(tour)

    while True:
        max_edge = sorted(tour, key=itemgetter(1), reverse=True)[0]

        neighbour1, neighbour2 = tu.get_neighbour_edges(tour, max_edge)
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

            tour.pop(tour.index(max_edge))
            added = ((selected_node, new_node), m[(selected_node, new_node)])
            tour.append(added)
            removed_edge = tu.get_edge(tour, node_x=new_node)
            tour.pop(tour.index(removed_edge))
            added = ((node1, removed_edge[0][1]), m[(node1, removed_edge[0][1])])
            tour.append(added)
        else:
            selected_node = node1
            new_node = node1_vals.argmin()

            tour.pop(tour.index(max_edge))
            added = ((selected_node, new_node), m[(selected_node, new_node)])
            tour.append(added)
            removed_edge = tu.get_edge(tour, node_y=new_node)
            tour.pop(tour.index(removed_edge))
            added = ((node0, removed_edge[0][0]), m[(node0, removed_edge[0][0])])
            tour.append(added)

        tour = tu.sort_tour_list(m, tour)

        new_cost = tu.tour_cost_sorted(tour)
        # tu.print_tour_sorted(tour)

        print('Total Cost: ', new_cost)

        if new_cost < best_cost:
            best_cost = new_cost
            best_tour = deepcopy(tour)
        else:
            print('Best Cost Reached:', best_cost)
            break

    return best_tour, best_cost


def ts_1100(m, tour, best):
    best_cost = best
    best_tour = deepcopy(tour)

    while True:
        m_copy = deepcopy(m)

        for edge in tour:
            m_copy[edge[0]] = maxsize
            m_copy[edge[0][1], edge[0][0]] = maxsize
            m_copy[edge[0][0], edge[0][0]] = maxsize

        min_cost = m_copy.min()
        min_index = np.where(m_copy == min_cost)[0]
        min_edge = ((min_index[0], min_index[1]), min_cost)

        neighbours1 = tu.get_neighbour_nodes(tour, min_index[0])
        neighbours2 = tu.get_neighbour_nodes(tour, min_index[1])
        # print(neighbours1)
        # print(neighbours2)
        # print(neighbours1[0][0], neighbours2[0][0])
        # print(neighbours1[1][1], neighbours2[1][1])

        cost1 = m[neighbours1[0][0], neighbours2[0][0]]
        cost2 = m[neighbours1[1][1], neighbours2[1][1]]

        min_edge2 = None
        if cost1 < cost2:
            min_edge2 = ((neighbours1[0][0], neighbours2[0][0]), cost1)
        else:
            min_edge2 = ((neighbours1[1][1], neighbours2[1][1]), cost2)

        # print(min_edge)
        # print(min_edge2)

        tour.append(min_edge)
        tour.append(min_edge2)

        to_be_removed = ((min_edge[0][0], min_edge2[0][0]), m[(min_edge[0][0], min_edge2[0][0])])
        if to_be_removed in tour:
            tour.pop(tour.index(to_be_removed))
        else:
            to_be_removed = ((min_edge2[0][0], min_edge[0][0]), m[(min_edge[0][0], min_edge2[0][0])])
            if to_be_removed in tour:
                tour.pop(tour.index(to_be_removed))
            else:
                to_be_removed = ((min_edge[0][0], min_edge2[0][1]), m[(min_edge[0][0], min_edge2[0][1])])
                if to_be_removed in tour:
                    tour.pop(tour.index(to_be_removed))
                else:
                    to_be_removed = ((min_edge2[0][1], min_edge[0][0]), m[(min_edge[0][0], min_edge2[0][1])])
                    if to_be_removed in tour:
                        tour.pop(tour.index(to_be_removed))

        # print(to_be_removed)
        to_be_removed = ((min_edge[0][1], min_edge2[0][1]), m[(min_edge[0][1], min_edge2[0][1])])
        if to_be_removed in tour:
            tour.pop(tour.index(to_be_removed))
        else:
            to_be_removed = ((min_edge2[0][1], min_edge[0][1]), m[(min_edge[0][1], min_edge2[0][1])])
            if to_be_removed in tour:
                tour.pop(tour.index(to_be_removed))
            else:
                to_be_removed = ((min_edge[0][1], min_edge2[0][0]), m[(min_edge[0][1], min_edge2[0][0])])
                if to_be_removed in tour:
                    tour.pop(tour.index(to_be_removed))
                else:
                    to_be_removed = ((min_edge2[0][0], min_edge[0][1]), m[(min_edge[0][1], min_edge2[0][0])])
                    if to_be_removed in tour:
                        tour.pop(tour.index(to_be_removed))
        # print(to_be_removed)

        tour = tu.sort_tour_list(m, tour)

        new_cost = tu.tour_cost_sorted(tour)
        # tu.print_tour_sorted(tour)

        print('Total Cost: ', new_cost)

        if new_cost < best_cost:
            best_cost = new_cost
            best_tour = deepcopy(tour)
        else:
            print('Best Cost Reached:', best_cost)
            break

    return best_tour, best_cost


def ts_1010(m, tour, best):
    best_cost = best
    best_tour = deepcopy(tour)

    while True:
        m_copy = deepcopy(m)

        for edge in tour:
            m_copy[edge[0]] = maxsize
            m_copy[edge[0][1], edge[0][0]] = maxsize
            m_copy[edge[0][0], edge[0][0]] = maxsize

        min_cost = m_copy.min()
        min_index = np.where(m_copy == min_cost)[0]
        min_edge1 = ((min_index[0], min_index[1]), min_cost)

        neighbours = tu.get_neighbour_nodes(tour, min_index[0])
        neighbours += tu.get_neighbour_nodes(tour, min_index[1])

        # print(min_edge1)
        # print(neighbours)

        max_edge1 = (None, -1)
        for edge in neighbours:
            if m[edge] > max_edge1[1]:
                max_edge1 = (edge, m[edge])

        max_edge2 = neighbours[(neighbours.index(max_edge1[0]) + 2) % 4]
        min_edge2 = max_edge1[0][0], max_edge2[0]

        max_edge2 = (max_edge2, m[max_edge2])
        min_edge2 = (min_edge2, m[min_edge2])

        # print()
        # print('add', min_edge1)
        # print('remove', max_edge1)
        # print('add', min_edge2)
        # print('remove', max_edge2)

        tour.append(min_edge1)
        tour.pop(tour.index(max_edge1))
        tour.append(min_edge2)
        tour.pop(tour.index(max_edge2))

        tour = tu.sort_tour_list(m, tour)

        new_cost = tu.tour_cost_sorted(tour)
        # tu.print_tour_sorted(tour)

        print('Total Cost: ', new_cost)

        if new_cost < best_cost:
            best_cost = new_cost
            best_tour = deepcopy(tour)
        else:
            print('Best Cost Reached:', best_cost)
            break

    return best_tour, best_cost
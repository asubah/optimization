#!usr/bin/python3

import numpy as np
from math import sqrt


def read_matrix():
    m = np.matrix(
        np.loadtxt(
            'm.txt'
        )
    )
    # m += np.transpose(m)
    return m


def produce_matrix(path):
    data = np.genfromtxt(path, skip_header=6, skip_footer=1)  # , dtype=np.int)
    m = np.zeros(shape=(len(data), len(data)))

    for i in range(0, m.shape[0]):
        for j in range(0, m.shape[0]):
            m[i, j] = e_distance(data[i][1], data[i][2], data[j][1], data[j][2])

    np.savetxt('m.txt', m)


def print_tour(m, tour):
    n = [(x, y) for x, y in tour.keys() if x == 0 or y == 0][0]
    print('{0} --[{1}]-->'.format(n[0], m[n]), end=' ')
    reverse = False
    for i in range(0, m[0].size - 2):
        pre = n
        if not reverse:
            n = [(x, y) for x, y in tour.keys()
                 if x == n[1] or y == n[1] and x != n[0] and y != n[0]][0]
            if n[0] != pre[1]:
                reverse = True
            else:
                reverse = False
        else:
            n = [(x, y) for x, y in tour.keys()
                 if (x == n[0] or y == n[0]) and (x, y) != n and (y, x) != n][0]
            if n[0] != pre[0]:
                reverse = True
            else:
                reverse = False

        if not reverse:
            print('{0} --[{1}]-->'.format(n[0], m[n]), end=' ')
        else:
            print('{0} --[{1}]-->'.format(n[1], m[n]), end=' ')

    if not reverse:
        print('{0} --[{1}]--> {2}'.format(n[1], m[0, n[1]], 0), end=' ')
    else:
        print('{0} --[{1}]--> {2}'.format(n[0], m[0, n[0]], 0), end=' ')

    print()


def print_tour_sorted(tour):
    for ((n0, n1), cost) in tour:
        print(n0, ' --[', cost, ']-->', sep='', end=' ')

    print(tour[-1][0][1])


def tour_cost(tour):
    return np.sum([value for (key, value) in tour.items()])


def tour_cost_sorted(tour):
    return np.sum([cost for ((n0, n1), cost) in tour])


def sort_tour_dict(m, tour):
    n = [(x, y) for x, y in tour.keys() if x == 0 or y == 0][0]
    sorted_tour = [(n, m[n])]
    reverse = False
    for i in range(0, m[0].size - 2):
        pre = n
        if not reverse:
            n = [(x, y) for x, y in tour.keys()
                 if x == n[1] or y == n[1] and x != n[0] and y != n[0]][0]
            if n[0] != pre[1]:
                reverse = True
            else:
                reverse = False
        else:
            n = [(x, y) for x, y in tour.keys()
                 if (x == n[0] or y == n[0]) and (x, y) != n and (y, x) != n][0]
            if n[0] != pre[0]:
                reverse = True
            else:
                reverse = False

        if not reverse:
            sorted_tour.append((n, m[n]))
        else:
            sorted_tour.append(((n[1], n[0]), m[n]))

    if not reverse:
        sorted_tour.append(((n[1], 0), m[n[1], 0]))
    else:
        sorted_tour.append(((n[0], 0), m[n[0], 0]))

    return sorted_tour


def sort_tour_list(m, tour):
    n = tour[0][0]  # [(x, y) for ((x, y), z) in tour if x == 0 or y == 0][0]
    sorted_tour = [(n, m[n])]
    reverse = False
    for i in range(0, m[0].size - 2):
        pre = n
        if not reverse:
            n = [(x, y) for ((x, y), z) in tour
                 if x == n[1] or y == n[1] and x != n[0] and y != n[0]][0]
            if n[0] != pre[1]:
                reverse = True
            else:
                reverse = False
        else:
            n = [(x, y) for ((x, y), z) in tour
                 if (x == n[0] or y == n[0]) and (x, y) != n and (y, x) != n][0]
            if n[0] != pre[0]:
                reverse = True
            else:
                reverse = False

        if not reverse:
            sorted_tour.append((n, m[n]))
        else:
            sorted_tour.append(((n[1], n[0]), m[n]))

    if not reverse:
        sorted_tour.append(((n[1], tour[0][0][0]), m[n[1], tour[0][0][0]]))
    else:
        sorted_tour.append(((n[0], tour[0][0][0]), m[n[0], tour[0][0][0]]))

    return sorted_tour


def get_neighbour_edges(tour, edge):
    if edge not in tour:
        edge = ((edge[0][1], edge[0][0]), edge[1])

    node_index = tour.index(edge)

    if node_index == 0:
        return tour[len(tour) - 1], tour[node_index + 1]
    elif node_index == len(tour) - 1:
        return tour[node_index - 1], tour[0]
    else:
        return tour[node_index - 1], tour[node_index + 1]


def get_neighbour_nodes(tour, node):
    n = [(x, y) for (x, y), z in tour if x == node or y == node]
    # x = y = None

    if n[0][0] == node:
        n = [n[1], n[0]]
    # else:
    #     x = n[0][0]
    #
    # if n[1][0] == node:
    #     y = n[1][1]
    # else:
    #     y = n[1][0]

    return n


def get_edge(tour, node_x=None, node_y=None):
        if node_x is not None:
            return [((x, y), z) for ((x, y), z) in tour if x == node_x][0]
        elif node_y is not None:
            return [((x, y), z) for ((x, y), z) in tour if y == node_y][0]
        else:
            return None


def are_neighbours(edge0, edge1):
    if edge0[0] == edge1[0] \
            or edge0[0] == edge1[1] \
            or edge0[1] == edge1[0] \
            or edge0[1] == edge1[1]:
        return True
    else:
        return False


def array_to_tour(m, arr):
    tour = []
    for i in range(len(arr) - 1):
        edge = (arr[i], arr[i+1])
        tour.append((edge, m[edge]))

    edge = (arr[-1], arr[0])
    tour.append((edge, m[edge]))

    return tour


def e_distance(x, y, a, b):
    return round(sqrt(((x - a) ** 2) + ((y - b) ** 2)))

#!usr/bin/python3

import numpy as np


def read_matrix():
    m = np.matrix(
        np.loadtxt(
            'm.txt',
            dtype=np.dtype(int)
        )
    )
    m += np.transpose(m)
    return m


def print_tour(m, tour):
    n = [(x, y) for x, y in tour.keys() if x == 0 or y == 0][0]
    print('{0} --[{1}]-->'.format(n[0], m[n]), end=' ')
    reverse = False
    for i in range(0, m[0].size - 3):
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


def print_tour_sorted(m, tour):
    pre = None
    for (city, mean) in tour:
        if pre is not None:
            print('--[', m[city, pre], ']--> ', city, sep='', end=' ')
        else:
            print(city, end=' ')
    
    print('--[', m[tour[0][0], pre], ']--> ', tour[0][0], sep='')


def tour_cost(tour):
    return np.sum([value for (key, value) in tour.items()])


def tour_cost_sorted(tour):
    return np.sum([value for (key, value) in tour])


def sort_tour(m, tour):
    n = [(x, y) for x, y in tour.keys() if x == 0 or y == 0][0]
    sorted_tour = [(n, m[n])]
    reverse = False
    for i in range(0, m[0].size - 3):
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
    n = [(x, y) for x, y in tour.keys() if x == node or y == node]
    x = y = None

    if n[0][0] == node:
        x = n[0][1]
    else:
        x = n[0][0]

    if n[1][0] == node:
        y = n[1][1]
    else:
        y = n[1][0]

    return x, y


def get_edge(tour, node_x=None, node_y=None):
        if node_x is not None:
            return [(x, y) for (x, y), z in tour if x == node_x][0]
        elif node_y is not None:
            return [(x, y) for (x, y), z in tour if y == node_y][0]
        elif node_x is None and node_y is None:
            return None
        else:
            return tour[(node_x, node_y)][0]

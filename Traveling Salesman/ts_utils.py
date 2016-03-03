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

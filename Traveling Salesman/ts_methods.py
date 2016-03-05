#!usr/bin/python3

import operator
import ts_utils as tu
from copy import deepcopy


def ts_mean(m):
    means = {}

    for i in range(0, m[0].size - 1):
        means[i] = m[0:, i].mean()

    means_sorted_tour = sorted(means.items(), key=operator.itemgetter(1))

    best_cost = 0
    pre = None
    tour = {}
    for (city, mean) in means_sorted_tour:
        if pre is not None:
            cost = m[city, pre]
            tour[(pre, city)] = cost
            print('--[', cost, ']--> ', city, sep='', end=' ')
            best_cost += cost
        else:
            print(city, end=' ')

        pre = city

    cost = m[means_sorted_tour[0][0], pre]
    tour[pre, means_sorted_tour[0][0]] = cost
    print('--[', cost, ']--> ', means_sorted_tour[0][0], sep='')
    best_cost += cost

    # tu.print_tour_sorted(m, means_sorted_tour)
    print('Total Cost:', best_cost)

    return tour, best_cost


def ts_0011(m, tour, best_cost):
    best_tour = None

    while True:
        sorted_tour = sorted(tour.items(), key=operator.itemgetter(1), reverse=True)

        first_max = sorted_tour[0]
        second_max = None
        for (edge, cost) in sorted_tour[1:]:
            if first_max[0][0] == edge[0] \
                    or first_max[0][0] == edge[1] \
                    or first_max[0][1] == edge[0] \
                    or first_max[0][1] == edge[1]:
                continue
            else:
                second_max = (edge, cost)
                break

        new_edge1 = (first_max[0][0], second_max[0][0])
        new_edge2 = (first_max[0][1], second_max[0][1])

        # print(first_max[0], second_max[0])
        # print(new_edge1, new_edge2)

        tour.pop(first_max[0])
        tour.pop(second_max[0])
        tour[new_edge1] = m[new_edge1]
        tour[new_edge2] = m[new_edge2]

        new_cost = tu.tour_cost(tour)
        tu.print_tour(m, tour)

        print('Total Cost: ', new_cost)

        if new_cost < best_cost:
            best_cost = new_cost
            best_tour = deepcopy(tour)
        else:
            print('Best Cost Reached:', best_cost)

            break

    return best_tour, best_cost


def ts_0101(m, tour, best):
    sorted_tour = sorted(tour.items(), key=operator.itemgetter(1), reverse=True)
    max_edge = sorted_tour[0]




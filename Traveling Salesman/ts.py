#!usr/bin/python3

from operator import itemgetter
from sys import maxsize
from copy import deepcopy
import numpy as np
import os
import re

import ts_methods as tm
import ts_utils as tu


def method_0():
    path = 'benchmarks/'

    instances = os.listdir(path)
    # instances.sort()

    result = open('results_0.csv', 'w')
    result.write('INSTANCE N NEAREST_NEIGHBOUR 0011 0101 1100 1010\n')

    for instance in instances:
        result.write(instance + ' ' + re.search('(\d+)', instance).group(0) + ' ')
        tu.produce_matrix(path + instance)
        m = tu.read_matrix()

        print('INSTANCE:', instance)

        print("========", "NEAREST NEIGHBOUR", "========")
        original_tour, original_cost = tm.ts_nearest_neighbour(m)
        result.write('%d ' % best_cost.item())

        # print("========", "MEAN", "========")
        # tour, best_cost = tm.ts_mean(m)

        print("========", "0101", "========")
        tour = deepcopy(original_tour)
        _, best_cost = tm.ts_0101(m, tour, original_cost)
        result.write('%d ' % best_cost.item())

        print("========", "1010", "========")
        tour = deepcopy(original_tour)
        _, best_cost = tm.ts_1010(m, tour, original_cost)
        result.write('%d ' % best_cost.item())

        print("========", "0011", "========")
        tour = deepcopy(original_tour)
        _, best_cost = tm.ts_0011(m, tour, original_cost)
        result.write('%d ' % best_cost.item())

        print("========", "1100", "========")
        tour = deepcopy(original_tour)
        _, best_cost = tm.ts_1100(m, tour, original_cost)
        result.write('%d ' % best_cost.item())

        result.write('\n')

    result.close()


def method_1():
    path = 'benchmarks/'

    instances = os.listdir(path)
    # instances.sort()

    result = open('results_1.csv', 'w')
    result.write('INSTANCE N NEAREST_NEIGHBOUR Result Trace\n')

    for instance in instances:
        trace = ''
        result.write(instance + ' ' + re.search('(\d+)', instance).group(0) + ' ')
        tu.produce_matrix(path + instance)
        m = tu.read_matrix()

        print('INSTANCE:', instance)

        print("========", "NEAREST NEIGHBOUR", "========")
        initial_tour, initial_cost = tm.ts_nearest_neighbour(m)
        result.write('%d ' % initial_cost.item())

        # print("========", "MEAN", "========")
        # tour, best_cost = tm.ts_mean(m)

        best_tour = initial_tour
        best_cost = initial_cost

        while True:
            t = ''
            print("========", "0101", "========")
            tour = deepcopy(initial_tour)
            tour_0101, cost_0101 = tm.ts_0101(m, tour, initial_cost)
            # result.write('%d ' % cost_0101.item())

            if cost_0101 < best_cost:
                best_cost = cost_0101
                best_tour = deepcopy(tour_0101)
                t = '0101,'

            print("========", "1010", "========")
            tour = deepcopy(initial_tour)
            tour_1010, cost_1010 = tm.ts_1010(m, tour, initial_cost)
            # result.write('%d ' % cost_1010.item())

            if cost_1010 < best_cost:
                best_cost = cost_1010
                best_tour = deepcopy(tour_1010)
                t = '1010,'

            print("========", "0011", "========")
            tour = deepcopy(initial_tour)
            tour_0011, cost_0011 = tm.ts_0011(m, tour, initial_cost)
            # result.write('%d ' % cost_0011.item())

            if cost_0011 < best_cost:
                best_cost = cost_0011
                best_tour = deepcopy(tour_0011)
                t = '0011,'

            print("========", "1100", "========")
            tour = deepcopy(initial_tour)
            tour_1100, cost_1100 = tm.ts_1100(m, tour, initial_cost)
            # result.write('%d ' % cost_1100.item())

            if cost_1100 < best_cost:
                best_cost = cost_1100
                best_tour = deepcopy(tour_1100)
                t = '1100,'

            if best_cost < initial_cost:
                initial_cost = best_cost
                initial_tour = deepcopy(best_tour)
                trace += t
            else:
                result.write('%d %s' % (best_cost.item(), trace))
                break

        result.write('\n')

    result.close()


def method_2():
    path = 'benchmarks/'

    instances = os.listdir(path)
    # instances.sort()

    result = open('results_2.csv', 'w')
    result.write('INSTANCE N NEAREST_NEIGHBOUR Result\n')

    for instance in instances:
        result.write(instance + ' ' + re.search('(\d+)', instance).group(0) + ' ')
        tu.produce_matrix(path + instance)
        m = tu.read_matrix()

        print('INSTANCE:', instance)

        print("========", "NEAREST NEIGHBOUR", "========")
        initial_tour, initial_cost = tm.ts_nearest_neighbour(m)
        result.write('%d ' % initial_cost.item())

        # print("========", "MEAN", "========")
        # tour, best_cost = tm.ts_mean(m)

        best_tour = initial_tour
        best_cost = initial_cost

        while True:
            t = ''
            print("========", "0101", "========")
            best_tour, best_cost = tm.ts_0101(m, best_tour, best_cost)
            # result.write('%d ' % cost_0101.item())

            print("========", "1010", "========")
            best_tour, best_cost = tm.ts_1010(m, best_tour, best_cost)
            # result.write('%d ' % cost_1010.item())

            print("========", "0011", "========")
            best_tour, best_cost = tm.ts_0011(m, best_tour, best_cost)
            # result.write('%d ' % cost_0011.item())

            print("========", "1100", "========")
            best_tour, best_cost = tm.ts_1100(m, best_tour, best_cost)
            # result.write('%d ' % cost_1100.item())

            if best_cost < initial_cost:
                initial_cost = best_cost
            else:
                result.write('%d' % best_cost.item())
                break

        result.write('\n')

    result.close()


def main():
    method_1()

if __name__ == "__main__":
    main()

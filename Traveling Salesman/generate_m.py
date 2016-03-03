#!usr/bin/python3

import random
import numpy as np


def generate(n, mini=1, maxi=20, seed=None):
    if not seed:
        random.seed(seed)

    m = []
    for i in range(0, n):
        r = []

        for j in range(0, n):
            if j < i:
                r.append(random.randint(mini, maxi))
            else:
                r.append(0)

        m.append(r)

    matrix = np.matrix(m, dtype=np.dtype(int))
    matrix += matrix.transpose()

    np.savetxt('m.txt', matrix, fmt='%i')
    return matrix

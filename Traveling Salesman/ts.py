#!usr/bin/python3

import numpy as np
import operator
import print_ts as pts

m = np.matrix(
        np.loadtxt(
            'm.txt',
            dtype=np.dtype(int)
            )
        )

m += m.transpose()

means = {}
for i in range(0, m[0].size - 1):
    means[i] = m[0:,i].mean()

meansSortedTour = sorted(means.items(), key=operator.itemgetter(1))

bestCost = 0
pre = None
tour = {}
for (city, mean) in meansSortedTour:
    if not pre == None:
        cost = m[city, pre]
        tour[(pre, city)] = cost
        print('--[', cost, ']--> ', city, sep='', end=' ')
        bestCost += cost
    else:
        print(city, end=' ')
    
    pre = city

cost = m[meansSortedTour[0][0], pre]
tour[pre, meansSortedTour[0][0]] = cost
print('--[', cost, ']--> ', meansSortedTour[0][0], sep='')
bestCost += cost

print('Total Cost:', bestCost)

while True:
    sortedTour = sorted(tour.items(), key=operator.itemgetter(1), reverse=True)

    firstMax = sortedTour[0]
    secondMax = None
    for (edge, cost) in sortedTour[1:]:
        if firstMax[0][0] == edge[0] or firstMax[0][0] == edge[1] or firstMax[0][1] == edge[0] or firstMax[0][1] == edge[1]:
            continue
        else:
            secondMax = (edge, cost)
            break
    
    newEdge1 = (firstMax[0][0], secondMax[0][0])
    newEdge2 = (firstMax[0][1], secondMax[0][1])
   
    #print(firstMax[0], secondMax[0]) 
    #print(newEdge1, newEdge2)

    tour[newEdge1] = m[newEdge1]
    tour[newEdge2] = m[newEdge2]
    
    tour.pop(firstMax[0])
    tour.pop(secondMax[0])
    
    newCost = np.sum([value for (key, value) in tour.items()])

    pts.print_tour(m, tour)    

    print('Total Cost: ', newCost)

    if newCost < bestCost:
        bestCost = newCost
    else:
        print('Best Cost Reached:', bestCost)
        break

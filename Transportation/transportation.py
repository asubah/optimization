#!usr/bin/python3
from pulp import *
import os.path

def solver(file_name):
    if not os.path.exists(file_name):
        return 'Fatal Error: file does not exist!'

    f = open(file_name)
    ls = f.readlines()
    
    mn = ls[0]
    mn = mn.replace('\n', '')
    mn = mn.split(' ')
    mn[0] = int(mn[0])
    mn[1] = int(mn[1])
    
    supply = []
    demand = []
    costs = []
    
    for l in ls[1:-1]:
        l = l.replace('\n', '')
        l = l.split(' ')
        supply.append(l[-1])
        costs.append(l[:-1])
    
    demand = ls[-1].split(' ')
    
    costs = [[int(j) for j in i] for i in costs]
    
    supplyNames = []
    supplyDict = {}
    for i in range(mn[0]):
        supplyNames.append(str(i))
        supplyDict[str(i)] = int(supply[i])
    
    
    demandNames = []
    demandDict = {}
    for i in range(mn[1]):
        demandNames.append(str(i))
        demandDict[str(i)] = int(demand[i])
    
    
    prob = LpProblem("p1",LpMinimize)
    
    Routes = [(s,d) for s in supplyNames for d in demandNames]
    route_vars = LpVariable.dicts("x",(supplyNames,demandNames),0,None,LpInteger)
    
    prob += lpSum([route_vars[s][d]*costs[int(s)][int(d)] for (s,d) in Routes]), "Sum of Transporting Costs"
    
    for s in supplyNames:
        prob += lpSum([route_vars[s][d] for d in demandNames]) <= supplyDict[s], "Sum of Supply %s"%s
    
    
    for d in demandNames:
        prob += lpSum([route_vars[s][d] for s in supplyNames]) >= demandDict[d], "Sum of Demand %s"%d
    
    prob.solve(GLPK(msg=0))
    
    return  (LpStatus[prob.status], value(prob.objective))

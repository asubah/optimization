#!usr/bin/python3
import transportation as t
import os

path = 'Instances/2/'

result = open('result', 'w')
result.write('instance status optimum\n')

instances = os.listdir(path)
instances.sort()

for instance in instances:
    r = t.solver(path + instance)
    print(instance, r[0], r[1])
    result.write(instance + ' ' + r[0] + ' ' + str(r[1]) + '\n')

result.close()

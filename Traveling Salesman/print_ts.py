#!usr/bin/python3

def print_tour(m, tour):
    n = [(x,y) for x,y in tour.keys() if x == 0 or y == 0][0]
    print('{0} --[{1}]-->'.format(n[0], m[n]), end=' ')
    reverse = False
    for i in range(0, m[0].size - 3):
        pre = n
        if not reverse:
            n = [(x,y) for x,y in tour.keys()
                if x == n[1] or y == n[1] and x != n[0] and y != n[0]][0]
            if n[0] != pre[1]:
                reverse = True
            else:
                reverse = False
        else:
            n = [(x,y) for x,y in tour.keys()
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
        print('{0} --[{1}]--> {2}'.format(n[1], m[0, n[1]], 0))
    else:
        print('{0} --[{1}]--> {2}'.format(n[0], m[0, n[0]], 0))

import os
import sys
import copy

paths = []
def combination(number, count):
    path = []
    backtrack(number, count, 1, path)
    return paths

def backtrack(number, count, start_idx, path):
    if len(path) == count:
        paths.append(copy.deepcopy(path))
        return

    for i in range(start_idx, number+1, 1):
        path.append(i)

        backtrack(number, count, i+1, path)

        path.pop()

if __name__ == '__main__':
    number = 4
    count = 2
    outs = combination(number, count)
    print('number=%s count=%s'%(number, count))
    print('outs=%s'%outs)

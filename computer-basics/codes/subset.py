import os
import sys
import copy

paths = []
def subset(lst):
    options = lst
    path = []
    start_idx = 0
    backtrack(path, start_idx, options)
    return paths

def backtrack(path, start_idx, options):
    paths.append(copy.deepcopy(path))
    #print('add path: %s'%(path))

    for i in range(start_idx, len(options), 1):
        option = options[i]
        #print('path=%s option=%s i=%s start_idx= %s'%(path, option, i, start_idx))
        path.append(option)

        backtrack(path, i + 1, options)

        path.pop()

if __name__ == '__main__':
    inputs = [1,2,3]
    outs = subset(inputs)
    print('inputs=%s'%inputs)
    print('outs=%s'%outs)

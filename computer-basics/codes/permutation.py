import os
import sys
import copy

paths = []
def permutation(lst):
    options = lst
    path = []
    backtrack(path, options)
    return paths

def backtrack(path, options):
    if len(path) == len(options):
        paths.append(copy.deepcopy(path))
        #print('add path: %s'%(path))
        return

    for option in options:
        #print('path=%s option=%s'%(path, option))
        #do_option
        if option in path:
            continue
        path.append(option)

        backtrack(path, options)

        #undo_option
        path.pop()

if __name__ == '__main__':
    inputs = [1,2,3]
    outs = permutation(inputs)
    print('inputs=%s'%inputs)
    print('outs=%s'%outs)

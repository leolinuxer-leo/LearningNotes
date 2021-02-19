import os
import sys

steps = []
def pancake_sort(lst):
    sort(lst, len(lst))
    return steps
    

def sort(lst, count):
    if count == 1:
        return

    max_id = find_max_id(lst, count)
    reverse(lst, 0, max_id)
    steps.append(max_id + 1)
    print('step a id=%s lst=%s'%(max_id+1, lst))
    reverse(lst, 0, count - 1)
    steps.append(count)
    print('step a id=%s lst=%s'%(count, lst))
    
    sort(lst, count-1)

def find_max_id(lst, cnt):
    max_v = -1
    max_id = -1
    for i in range(cnt):
        if lst[i] > max_v:
            max_v = lst[i]
            max_id = i
    return max_id
    
def reverse(lst, start_id, end_id):
    while start_id < end_id:
        lst[start_id], lst[end_id] = lst[end_id], lst[start_id]
        start_id += 1
        end_id -= 1

if __name__ == '__main__':
    inputs = [3, 2, 4, 1]
    print('inputs=%s'%inputs)
    outs = pancake_sort(inputs)
    print('outs=%s'%outs)

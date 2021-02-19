import os
import sys

from basics.sstack import SStack

def force(lst):
    cnt = len(lst)
    outs = []
    for i in range(cnt):
        current = lst[i]
        mmax = -1
        for j in range(i+1, cnt, 1):
            if lst[j] > current:
                mmax = lst[j]
                break
        outs.append(mmax)
    return outs

def monotonic_stack(lst):
    cnt = len(lst)
    stack = SStack()
    ans = [0]*cnt
    for i in range(cnt-1, -1, -1):
        current = lst[i]
        while(not stack.is_empty() and stack.top() <= current):
            stack.pop()
        if stack.is_empty():
            ans[i] = -1
        else:
            ans[i] = stack.top()
        stack.push(current)
    return ans

def next_greater_num(lst):
    #return force(lst)
    return monotonic_stack(lst)

if __name__ == '__main__':
    inputs = [2,1,2,4,3]
    outputs = [4,2,4,-1,-1]
    outs = next_greater_num(inputs)
    print('inputs=%s'%inputs)
    print('outputs=%s'%outputs)
    print('outputs=%s'%outs)

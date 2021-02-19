import os
import sys

class SStack:

    def __init__(self):
        self.data = []
        self.size = 0

    def push(self, val):
        self.data.append(val)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        val = self.data.pop()
        self.size -= 1
        return val

    def top(self):
        if self.size == 0:
            return None
        else:
            return self.data[-1]

    def is_empty(self):
        return self.size == 0

if __name__ == '__main__':
    inputs = [2,1,2,4,3]
    stack = SStack()
    for v in inputs:
        stack.push(v)

    print('inputs=%s'%inputs)
    print('outs')
    while not stack.is_empty():
        v = stack.pop()
        print(v)

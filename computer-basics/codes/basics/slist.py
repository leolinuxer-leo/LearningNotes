import os
import sys
import copy

class SNode:

    def __init__(self, val = None):
        self.val = val
        self.next = None

class SOneWayList:

    def __init__(self):
        self.head = None
        self.tail = self.head
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_back(self, val):
        node = SNode(val)
        if self.is_empty():
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def pop_front(self):
        if self.is_empty():
            return None
        node = self.head
        self.head = self.head.next
        self.size -= 1
        return node.val

    def get_front(self):
        if self.is_empty():
            return None
        return self.head.val

    def get_back(self):
        if self.is_empty():
            return None
        return self.tail.val

    def get_all(self):
        lst = []
        head = self.head
        while head != None:
            lst.append(head.val)
            head = head.next
        return lst

if __name__ == '__main__':
    inputs = [2,1,2,4,3]
    slist = SOneWayList()

    for v in inputs:
        slist.push_back(v)

    print('inputs=%s'%inputs)
    lst = slist.get_all()
    print('outs=%s'%lst)

    while not slist.is_empty():
        val = slist.pop_front()
        print('pop', val)
        print('front', slist.get_front(), ' back', slist.get_back())
    lst = slist.get_all()
    print('outs=%s'%lst)

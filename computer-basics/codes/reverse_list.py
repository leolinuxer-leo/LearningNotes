import os
import sys

from basics.slist import SOneWayList

def reverse_list(head):
    if head.next == None:
        return head
    last = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return last

def reverse(slist):
    old_head = slist.head
    new_head = reverse_list(slist.head) 
    slist.head = new_head
    slist.tail = old_head
    print('new head', slist.head.val, slist.head.next)
    print('new tail', slist.tail.val, slist.tail.next)

if __name__ == '__main__':
    inputs = [2,1,2,4,3]
    slist = SOneWayList()

    for v in inputs:
        slist.push_back(v)

    print('inputs=%s'%inputs)
    lst = slist.get_all()
    print('outs=%s'%lst)

    head = reverse(slist)
    lst = slist.get_all()
    print('outs=%s'%lst)


import os
import sys

class STreeNode:

    def __init__(self, nid, val = None):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class STreeBST:

    def __init__(self):
        self.root = None
        self.map_nid2node = {}

    def is_empty(self):
        return len(self.root == None)

    def add_node(self, pid, nid, val):
        node = STreeNode(nid, val)
        self.map_nid2node[nid] = node
        if pid == -1: # add root
            self.root = node
            return True

        if pid not in self.map_nid2node:
            print('Error no such pid=%d'%(pid))
            return False

        root = self.map_nid2node[pid]
        if root.left == None:
            root.left = node
            return True
        elif root.right == None:
            root.right = node
            return True
        else:
            print('Error parent(nid=%d) node is full'%(pid))
            return False
        
    
    def print_self(self):
        self.print_node(self.root, 0)

    def print_node(self, node, depth):
        if node == None:
            return
        blanks = ['---']*depth
        print(''.join(blanks)+'|<%s>'%(node.val))
        self.print_node(node.left, depth + 1)
        self.print_node(node.right, depth + 1)

if __name__ == '__main__':
    inputs = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
    print('inputs=%s'%inputs)

    stree = STreeBST()
    cnt = len(inputs)
    for idx in range(cnt):
        val = inputs[idx]
        if val == None:
            continue
        if idx == 0:
            pid = -1
        else:
            pid = int((idx-1)/2)
        nid = idx
        print('add node: pid=%d nid=%d val=%s'%(pid, nid, val))
        stree.add_node(pid, nid, val)

    stree.print_self()

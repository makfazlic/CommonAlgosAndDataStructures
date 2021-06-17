#!/usr/bin/python3
# Binary search tree 

from math import tan
from print_bst_ascii import *
import random
import sys

class Node:
    def __init__(self,value):
        self.key = value
        self.left = None
        self.right = None
        self.parent = None

# \Theta(n)
# In-Order Tree Walk
# Pre - t.key before t.left recursive call
# Post - t.key after t.left recursive call
# Print reverse - switch t.left and t.right recursive calls
def print_in_order(t):
    if t != None:
        print_in_order(t.left)
        print(t.key)
        print_in_order(t.right)

# \Theta(n)
def bst_size(t):
    if t == None:
        return 0
    else:
        return bst_size(t.left) + 1 + bst_size(t.right)

# \Theta(n)
# Average case height = O(log n) 
def bst_height(t):
    if t == None:
        return 0
    else:
        return 1 + max(bst_height(t.left), bst_height(t.right))

# \Theta(n)
def bst_min(t):                 # minimum key in t
    if t == None:
        return None
    while t.left != None:
        t = t.left
    return t.key

# \Theta(n)
def bst_min_node(t):                 # node holding the minimum key in t
    if t == None:
        return None
    while t.left != None:
        t = t.left
    return t

# \Theta(n)
def bst_max(t):                 # maximum key in t
    if t == None:
        return None
    while t.right != None:
        t = t.right
    return t.key

# \Theta(n)
def bst_next(t):
    # next node in the natural order of keys
    if t.right != None:
        return bst_min_node(t.right)
    #
    # go up at most until we reach the root (parent == None)
    # or a parent node
    p = t.parent
    while p != None and p.left != t:
        t = p
        p = p.parent
    return p

# \Theta(n)
def bst_previous(t):
    # next node in the natural order of keys
    if t.left != None:
        return bst_max_node(t.left)
    #
    # go up at most until we reach the root (parent == None)
    # or a parent node
    p = t.parent
    while p != None and p.right != t:
        t = p
        p = p.parent
    return p

# \Theta(n)
def bst_search(t, k):
    while t != None and t.key != k:
        if k > t.key:
            t = t.right
        else:
            t = t.left
    return t != None
    
# \Theta(n)
def bst_insert(t,k):
    # insert k in t (with repetitions, i.e., in a multiset).  Return
    # the root of the tree, which is t if t != None, or a new root
    # node if t == None
    if t == None:
        return Node(k)
    r = t
    while True:
        if k <= t.key:
            if t.left == None:
                t.left = Node(k)
                return r
            else:
                t = t.left
        else:
            if t.right == None:
                t.right = Node(k)
                return r
            else:
                t = t.right

# \Theta(n)
def bst_from_array(A):
    t = None
    for a in A:
        t = bst_insert(t, a)
    return t

# \Theta(n)
def bst_delete(t, k):
    if k.left == None or k.right == None:
        y = k
    else:
        y = bst_next(k)
    if y.left != None:
        x = y.left
    else:
        x = y.right
    if x != None:
        x.parent = y.parent
    if y.parent == None:
        t = x
    else:
        if y == y.parent.left:
            y.parent.left = x
        else: 
            y.parent.right = x
    if y == k:
        k.key = y.key
        k.left = y.left
        k.right = y.right
    
def rotate_right(t):
    assert t != None and t.left != None
    r = t.left
    t.left = r.right
    r.right = t
    return r

def rotate_left(t):
    assert t != None and t.right != None
    r = t.right
    t.right = r.left
    r.left = t
    return r

def tree_root_insert(t, k):
    if t == None:
        return Node(k)
    if k <= t.key:
        t.left = tree_root_insert(t.left, k)
        return rotate_right(t)
    else:
        t.right = tree_root_insert(t.right, k)
        return rotate_left(t)

# Usage
#t = Node(5)
#t.left = Node(4)
#t.right = Node(18)
#t.right.left = Node(7)
#t.right.right = Node(19)
#t.right.right.right = Node(19)

A = [x for  x in range(20)]
t = bst_from_array(A)
print_tree(t)
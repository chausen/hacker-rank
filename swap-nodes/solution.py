#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

depths = defaultdict(list)

# Storing the depth makes it easier to keep track of
# which depth a node is at when we add it to the depths dict
class Node:
    left = None
    right = None
    depth = 1

    def __init__(self, val):
        self.value = val

# Also populates the global depth dictionary:
# depth: { key = depth, value = list of nodes at that depth }
# This is used to make it trivial to find the nodes whose subtrees
# must be swapped
def create_tree(indexes):
    nodes = [-1] * (len(indexes) + 1)
    root = Node(1)
    nodes[1] = root
    for parent_index, children in enumerate(indexes, start=1):
        parent_node = nodes[parent_index]
        depths[parent_node.depth].append(parent_node)
        left, right = children[0], children[1]
        if left != -1:
            left_node = Node(left)
            left_node.depth = parent_node.depth + 1
            parent_node.left = left_node
            nodes[left] = left_node
        if right != -1:
            right_node = Node(right)
            right_node.depth = parent_node.depth + 1
            parent_node.right = right_node
            nodes[right] = right_node
    return root
    
def in_order(root):
    stack = []
    in_order_nodes = []
    current_node = root

    while True:        
        if current_node is not None:
            stack.append(current_node)
            current_node = current_node.left            
        elif(stack):
            current_node = stack.pop()
            in_order_nodes.append(current_node.value)
            current_node = current_node.right
        else:
            break;
    return in_order_nodes

# We want to swap at each depth that is a multiple of k,
# c is used to keep track of the current multiple
def swap_nodes(k):
    c = 1
    while c*k in depths:
        for node in depths[c*k]:
            temp = node.left
            node.left = node.right
            node.right = temp
        c += 1

def swapNodes(indexes, queries):
    results = []
    root = create_tree(indexes)
    for k in queries:
        swap_nodes(k)
        nodes = in_order(root)
        results.append(nodes)
    return results

if __name__ == '__main__':

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    print([' '.join(map(str, x)) for x in result])

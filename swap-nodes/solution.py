#!/bin/python3

import math
import os
import random
import re
import sys

class Node:
    left = None
    right = None

    def __init__(self, val):
        self.value = val

def create_tree(indexes):
    nodes = [-1] * (len(indexes) + 1)
    root = Node(1)
    nodes[1] = root
    for parent_index, children in enumerate(indexes, start=1):
        parent_node = nodes[parent_index]
        left, right = children[0], children[1]
        if left != -1:
            left_node = Node(left)
            parent_node.left = left_node
            nodes[left] = left_node
        if right != -1:
            right_node = Node(right)
            parent_node.right = right_node
            nodes[right] = right_node
    return root
    
def in_order(node, nodes):
    if node.left:
        in_order(node.left, nodes)
    nodes.append(node.value)
    if node.right:
        in_order(node.right, nodes)

def swap_nodes(node, k, depth):
    if depth % k == 0:
        temp = node.left
        node.left = node.right
        node.right = temp
    if node.left:
        swap_nodes(node.left, k, depth+1)
    if node.right:
        swap_nodes(node.right, k, depth+1)

def swapNodes(indexes, queries):
    results = []
    root = create_tree(indexes)
    for k in queries:
        swap_nodes(root, k, 1)
        nodes = []
        in_order(root, nodes)
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

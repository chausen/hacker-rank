#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
from collections import deque

def build_graph(n, edges):
    graph = defaultdict(set)
    
    for edge in edges:
        to, frm = edge[0], edge[1]
        graph[to].add(frm)
        graph[frm].add(to)
    return graph

# Complete the bfs function below.
def bfs(n, m, edges, s):
    graph = build_graph(n, edges)
    visited = set()
    # make room to store node n in index n and initialize to unreachable
    distances = [-1] * (n + 1)

    queue = deque([s])
    visited.add(s)
    distances[s] = 0
    while queue:
        vertex = queue.pop()
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.appendleft(neighbor)
                distances[neighbor] = distances[vertex] + 6        

    del distances[s] # don't include starting node
    return distances[1:] # nodes are from 1 to n
    
if __name__ == '__main__':
    fptr = open('output.txt', 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

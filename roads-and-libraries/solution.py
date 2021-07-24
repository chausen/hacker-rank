#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict

def build_graph(n, cities):
    isolated_cities = set()
    for i in range(1, n + 1):
        isolated_cities.add(i)
        
    graph = defaultdict(set)
    for edge in cities:
        frm, to = edge[0], edge[1]
        graph[frm].add(to)
        graph[to].add(frm)
        isolated_cities.discard(frm)
        isolated_cities.discard(to)

    for city in isolated_cities:
        graph[city] = None

    return graph

def dfs(graph):
    components = []
    visited = set()

    def traverse(vertex):
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                components[-1] += 1
                traverse(neighbor)
    
    for vertex in graph:
        if vertex not in visited:
            visited.add(vertex)
            components.append(1)
            traverse(vertex)
                
    return components

# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    # There are two cases:
    # 1. c_lib <= c_road
    # 2. c_lib  > c_road
    # For case 1., the the easiest thing to do is build a library for every
    # city, and it will result in the minimum cost
    # For case 2., we want to:
    #   find all of the components
    #   find the number of edges per component
    #   build a library in any city in each component
    # So, the min cost will be:
    # sum(for each comp: comp.num_edges*c_road + c_lib)

    if c_lib <= c_road:
        return n * c_lib

    graph = build_graph(n, cities)
    components = dfs(graph)    

    total = 0
    for component_count in components:
        total += (component_count - 1) * c_road + c_lib

    return total
        

if __name__ == '__main__':
    fptr = open('output.txt', 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()



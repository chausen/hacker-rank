#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

def whatFlavorsMine(cost, money):
    costs = defaultdict(list)
    for i in range(len(cost)):
        costs[cost[i]].append(i+1)

    for c in costs:        
        if money - c in costs:
            if money - c == c and len(costs[c]) < 2:
                continue
            chosen_flavors = sorted((costs[c].pop(), costs[money-c].pop()))
            print('{} {}'.format(chosen_flavors[0], chosen_flavors[1]))
            return

def whatFlavors(cost, money):
    saved = {}
    for i,n in enumerate(cost):
        if money-n in saved:
            print('{} {}'.format(saved[money-n], i+1))
            return
        saved[n] = i+1        

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)

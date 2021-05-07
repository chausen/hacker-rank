#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

# Complete the isBalanced function below.
def isBalanced(s):
    d = deque()
    LEFT = ['(', '[', '{']
    RIGHT = [')', ']', '}']
    for c in s:
        if c in LEFT:
            d.append(c)
        if c in RIGHT:
            if len(d) == 0 or LEFT.index(d.pop()) != RIGHT.index(c):
                return 'NO'                

    if len(d) == 0:
        return 'YES'
    else:
        return 'NO'
        

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        print(result)

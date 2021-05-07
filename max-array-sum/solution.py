#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):

    def bigmax(arr, i):
        if i >= len(arr):
            return 0
        # take
        t = bigmax(arr, i + 2) + arr[i]
        # don't take
        d = bigmax(arr, i + 1)

        return max(t,d)

    return bigmax(arr, 0)

# recurrence relation
# max(i + max(i-2), max(i-1))
def maxSubsetSumDynamic(arr):
    m = []
    m.append(arr[0])
    m.append(max(m[0], arr[1]))
    for i in range(2, len(arr)):
        m.append(max(arr[i] + m[i-2], m[i-1]))
    return m[-1]

def maxSubsetSumDynamicOptimized(arr):
    pen = arr[0] if arr[0] > 0 else 0 # solution should be 0 if all elements are negative
    ult = max(pen, arr[1])
    for i in range(2, len(arr)):
        temp = max(arr[i] + pen, ult)
        pen = ult
        ult = temp
    return ult         

if __name__ == '__main__':
    n = int(input())
    
    arr = list(map(int, input().rstrip().split()))
    res = maxSubsetSumDynamicOptimized(arr)

    print(res)

    

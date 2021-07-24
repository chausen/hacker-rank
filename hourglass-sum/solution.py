#!/bin/python3

import math
import os
import random
import re
import sys

def hourglass(arr, center_x, center_y):
    sum = arr[center_x][center_y]
    for j in range(center_y - 1, center_y + 2):
        sum += arr[center_x - 1][j]
        sum += arr[center_x + 1][j]
    return sum

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sums = []
    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr[0]) - 1):
            sums.append(hourglass(arr, i, j))
    
    return max(sums)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

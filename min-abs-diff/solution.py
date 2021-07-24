# For sorted all-positive or all-negative integers, the two with the smallest difference will always be adjacent to each other. Every step, compare the current difference with the current min, and update it if smaller.

# UPDATE: this is wrong...75 - (-75) = 150...not 0...derp
# If the smallest absolute difference is between a positive and a negative number, it will be the pair closest to equidistant from 0. We can have a pointer going left of 0 (-) and a pointer going right (+). For a sorted list, at each step we:
#  move the pointer that is closest to 0
#  compute the current difference and compare it to the current min
#  update the current min if > current diff

#!/bin/python3

import math
import os
import random
import re
import sys

def minimumAbsoluteDifference(arr):
    arr = sorted(arr)
    
    sign_change_index = -1
    minimum = math.inf
    for i in range(len(arr) - 1):
        curr_diff = abs(arr[i] - arr[i+1])
        if curr_diff < minimum:
            minimum = curr_diff
        if arr[i] <= 0 and arr[i+1] > 0:
            sign_change_index = arr[i]
    # don't need this...see note on the top...derp
    if sign_change_index > -1:
        i, j = sign_change_index, sign_change_index + 1
        while i >= 0 or j < len(arr):
            curr_diff = abs(arr[i] - arr[j])
            if curr_diff < minimum:
                minimum = curr_diff           
            
            if i >= 0 and abs(arr[i]) < abs(arr[j]):
                i -= 1
            else:
                j += 1
   
    return minimum
            
if __name__ == '__main__':
    fptr = open('output.txt', 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

# using a min heap
def luckBalance(k, contests):
    max_luck = 0
    h = [] # min heap for important luck ratings
    
    for contest in contests:
        max_luck += contest[0]
        if contest[1] == 1:
            heapq.heappush(h, contest[0])                        

    for _ in range(len(h) - k):
        # *2 to account for already adding the luck values
        max_luck -= 2 * heapq.heappop(h) 

    return max_luck

# another approach I saw; didn't write this one, but I liked it
# sort the overall list in decreasing order
# add luck for important contests until you run out of ones you can lose
def luckBalanceSortApproach(k, contests):
    total_luck = 0
    for luck,important in sorted(contests, reverse=True):
        if not important:
            total_luck += luck
        elif k:
            total_luck += luck
            k -= 1
        else:
            total_luck -= luck
    return total_luck

if __name__ == '__main__':    

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    print(result)



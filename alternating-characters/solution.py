#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternatingCharacters(s):
    deletions = 0
    
    prev = s[0]
    for i, c in enumerate(s[1:], start=1):
        if prev == c:
            deletions += 1
        else:
            prev = c
            
    return deletions

if __name__ == '__main__':
    
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        print(result)

    

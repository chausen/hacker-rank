#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def twoStrings(s1, s2):
    m = {}
    for i in range(len(s1)):
        m[s1[i]] = True
    for i in range(len(s2)):
        if s2[i] in m:
            return 'YES'
    return 'NO'

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        print(result)

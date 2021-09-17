#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#
    
def abbreviation_recursive(a, b):
    is_abbrev = False
    def abbrev(s, i):    
        if i >= len(a):
            if b == s:
                nonlocal is_abbrev
                is_abbrev = True
            return
        if a[i].islower():
            abbrev(s, i+1)  
            abbrev(s + a[i].upper(), i+1)
        else:        
            abbrev(s + a[i], i+1)

    abbrev('', 0)
    if is_abbrev:
        return 'YES'
    else:
        return 'NO'

def abbreviation(a, b): 
    if len(a) < len(b):
        return 'NO'

    combos = [a.upper()]
    if combos[0] == a:
        return 'YES'
    for i in range(len(a)):        
        for j in range(i**2-1):
            if a[i].isupper():
                next
            c = combos[j]
            c = c[:i-1] + '_' + c[i:]
            if c.replace('_', '') == b:
                return 'YES'
            combos.append(c)
    print(combos)
    return 'NO'
            
if __name__ == '__main__':    

    q = int(input().strip())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        print(result)    

import sys

MATCH = 0
INSERT = 1
DELETE = 2

def match(a, b):
    if a == b:
        return 0
    else:
        return 1

def indel(a):
    return 1

def string_compare_r(s, t, i, j):    
    opt = [0]*3 
    lowest_cost = sys.maxsize

    if (i == 0):
        return (j * indel(' '))

    if (j == 0):
        return (i * indel(' '))

    opt[MATCH] = string_compare_r(s, t, i-1, j-1) + match(s[i], t[j])
    opt[INSERT] = string_compare_r(s, t, i, j-1) + indel(t[j])
    opt[DELETE] = string_compare_r(s, t, i-1, j) + indel(s[i])

    lowest_cost = opt[MATCH]    
    for k in range(INSERT, DELETE+1):
        if (opt[k] < lowest_cost):
            lowest_cost = opt[k]
    
    return lowest_cost

s = 'zoo'
t = 'bird'
print(string_compare_r(s, t, len(s)-1, len(t)-1))
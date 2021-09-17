from collections import namedtuple
import pprint

MATCH = 0
INSERT = 1
DELETE = 2

pp = pprint.PrettyPrinter(indent=4)
cell = namedtuple('cell', 'cost parent')

def string_compare(s, t):        
    MAXLEN = max(len(s), len(t))
    m = [ [cell(0,0)] * (MAXLEN+1) for _ in range(MAXLEN+1)]
    opt = [0] * 3

    t = t.rjust(len(t) + 1)
    s = s.rjust(len(s) + 1)
    if len(s) > len(t):
        t = t.ljust(len(t) + (len(s) - len(t)))
    elif len(s) < len(t):
        s = s.ljust(len(s) + (len(t) - len(s)))    

    m[0][0] = cell(0, -1)
    for i in range(1, MAXLEN+1):
        m[0][i] = cell(i, INSERT)
        m[i][0] = cell(i, DELETE)    

    for i in range(1, len(s)):
        for j in range(1, len(t)):    
            opt[MATCH] = m[i-1][j-1].cost + match(s[i], t[j])
            opt[INSERT] = m[i][j-1].cost + 1
            opt[DELETE] = m[i-1][j].cost + 1            

            m[i][j] = cell( min(opt), opt.index(min(opt)) )

    reconstruct_path(s, t, i, j, m)
    
    goal = goal_cell(s, t, i, j, m)

    return m[goal[0]][goal[1]].cost

def match(a, b):
    v = 0 if a == b else 1
    return v

def reconstruct_path(s, t, i, j, m):
    if (m[i][j].parent == -1):
        return;
    if (m[i][j].parent == MATCH):
        reconstruct_path(s, t, i-1, j-1, m)
        match_out(s, t, i, j)
        return
    if (m[i][j].parent == INSERT):
        reconstruct_path(s, t, i, j-1, m)
        insert_out(t, j)
        return
    if (m[i][j].parent == DELETE):
        reconstruct_path(s, t, i-1, j, m)
        delete_out(s, i)
        return

def match_out(s, t, i, j):
    if s[i] == t[j]:
        print('M')
    else:
        print('S')

def insert_out(t, j):
    print("I")

def delete_out(s, i):
    print("D")        

def goal_cell(s, t, i, j, m):
    return (len(s)-1, len(t)-1)    

# print(string_compare('hei', 'be'))
# print(string_compare('hello', 'world'))
print(string_compare('thou shalt', 'you should'))
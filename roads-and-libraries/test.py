from collections import defaultdict

d = defaultdict(set)
d[1].add(2)
d[2] = None

print(d)
for s in d:
    print(d)
    print(f'Size: {len(d)}')
    

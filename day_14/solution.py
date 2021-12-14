from collections import defaultdict, Counter
f = [x for x in open("input.txt").read().strip().split("\n")]

start = f[0]
parts = f[2:]
d = defaultdict(str)

for part in parts:
    left, right = part.split(" -> ")
    d[left] = right

d1 = defaultdict(int)
for a,b in zip(start[:-1], start[1:]):
    q = a+b
    d1[q] += 1

for i in range(40):
    d2 = defaultdict(int)
    for k,v in d1.items():
        d2[k[0] + d[k]] += v
        d2[d[k] + k[1]] += v
    d1 = d2
    if i in [9, 39]:
        q = Counter()
        for k,v in d1.items():
            q[k[0]] += v
        q[start[-1]] += 1 # Need to add the last character
        print(max(q.values()) - min(q.values()))






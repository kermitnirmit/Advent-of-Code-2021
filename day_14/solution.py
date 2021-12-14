from collections import defaultdict, Counter
f = [x for x in open("input.txt").read().strip().split("\n")]

start = f[0]  # first line is the start str
parts = f[2:] # everything after the 2nd line is a mapping
d = defaultdict(str) # instantiate a dictionary that maps something to a string (kinda not necessary)

for part in parts:
    left, right = part.split(" -> ")
    d[left] = right # left double maps to right single

d1 = defaultdict(int) #instantiate dictionary that maps something to an int
for a,b in zip(start[:-1], start[1:]): # this iterates over the letter pairs in the initial string
    q = a+b
    d1[q] += 1 # counts how many of each pair

for i in range(40):
    d2 = defaultdict(int) #because the changes are instantaneous - need to keep a new and old dictionary
    for k,v in d1.items(): # k is a letter pair thats in the last generation string, v is how many times that pair occurred
        d2[k[0] + d[k]] += v  # if k = AB and AB maps to R, then that generates an AR and RB. How many of those? v of them. this line takes care of AR
        d2[d[k] + k[1]] += v # and this line takes care of RB
    d1 = d2 # generation done, so store these new numbers for the next iteration
    if i in [9, 39]:
        q = Counter() #same as defaultdict(int)
        for k,v in d1.items(): # same as line 19, but each letter pair overlaps, so i need to only count the first one
            q[k[0]] += v # k[0] is the first letter in the pair, count how many times that character appeared
        q[start[-1]] += 1 # Need to add the last character because it's never the first character in a pair.
        print(max(q.values()) - min(q.values())) # most common - least common.

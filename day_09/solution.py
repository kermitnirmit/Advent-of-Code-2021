f = [x for x in open("input.txt").read().strip().split("\n")]
dirs = [(0,1), (0, -1), (1,0), (-1, 0)]
c = 0
lows = []
low_locs = []
for i, line in enumerate(f):
    for j, letter in enumerate(line):
        lowerNeighbor = False
        for a, b in dirs:
            if -1 < i + a < len(f) and -1 < j + b < len(line):
                if int(f[i+a][j+b]) <= int(letter):
                    lowerNeighbor = True
                    break
        if not lowerNeighbor:
            lows.append(int(letter))
            low_locs.append((i,j))


seen = set()
def findIslands(i,j, currSize):
    for a, b in dirs:
        if -1 < i + a < len(f) and -1 < j + b < len(line):
            if "9" > f[i + a][j+b] > f[i][j] and (i+a, j+b) not in seen and (i + a, j + b) not in low_locs:
                seen.add((i+a,j+b))
                currSize = findIslands(i+a, j+b, currSize + 1)
    return currSize

islands = []
for i in range(len(f)):
    for j in range(len(f[0])):
        if (i,j) in low_locs:
            seen.add((i, j))
            islands.append(findIslands(i,j, 1))

p = 1
for a in  sorted(islands, reverse=True)[:3]:
    p *= a
print(sum(lows) + len(lows))
print(p)


import numpy as np
a = [list(x) for x in open("input.txt").read().strip().split("\n")]
asdf = []
for q in a:
    w = []
    for e in q:
        w.append(int(e))
    asdf.append(w)
f = np.asarray(asdf)
dirs = [(x, y) for x in range(-1, 2) for y in range(-1, 2)]
step = 1
flashes = 0
while step < 1000:
    f += 1
    if f.sum() ==  (len(f) ** 2):
        print("p2", step - 1)
        break
    flashers = set()
    over9s = (f > 9).sum()
    while over9s > 0:
        for i in range(len(f)):
            for j in range(len(f)):
                if f[i][j] > 9:
                    flashers.add((i,j))
                    for x,y in dirs:
                        if -1 < x + i < len(f) and -1 < y + j < len(f[0]) and not (x == 0 and y == 0):
                            f[x+i][y+j] += 1
        for x, y in flashers:
            f[x][y] = 0
        over9s = (f > 9).sum()
    flashes += len(flashers)
    f = np.where(f > 9, 0, f)
    step += 1
    if step == 101:
        print("p1", flashes)
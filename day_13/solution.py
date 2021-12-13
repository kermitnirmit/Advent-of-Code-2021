from statistics import median, mean, geometric_mean
from itertools import combinations, permutations
from collections import defaultdict
import parse
import numpy as np

points, folds = [x for x in open("input.txt").read().strip().split("\n\n")]

points = [x for x in points.splitlines()]
p = []

for point in points:
    p.append(tuple(map(int, point.split(","))))
points = p
folds = [x for x in folds.splitlines()]
max_x = max(x[0] for x in points) + 1
max_y = max(x[1] for x in points) + 1
f = []
for fold in folds:
    axis, idx = fold[11:].split("=")
    f.append((axis, int(idx)))
folds = f



a = np.zeros((max_y, max_x))

def fold_it(a, d):
    arr = a[d:]
    arr = np.flip(arr, axis=0)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            a[i][j] = max(arr[i][j], a[i][j])
    return a[:d]


for x,y in points:
    a[y][x] = 1
for i, (q, d) in enumerate(folds):
    d = int(d)
    if q == "x":
        a = a.T
        a = fold_it(a, d)
        a = a.T
    else:
        a = fold_it(a, d)
    if i == 0:
        print(int(a.sum()))

for i in range(len(a)):
    builder = ""
    for j in range(len(a[i])):
        if a[i][j] == 1:
            builder += "#"
        else:
            builder += " "
    print(builder)


for i, f in enumerate(folds):
    axis, idx = f
    if axis == "x":
        points = set((x, y) if x < idx else (idx + idx - x, y) for x,y in points)
    else:
        points = set((x, y) if y < idx else (x, idx + idx - y) for x, y in points)
    if i == 0:
        print(len(points))

still_there = list(points)
max_x = max(x[1] for x in still_there)
max_y = max(x[0] for x in still_there)

for i in range(max_x + 1):
    builder = ""
    for j in range(max_y + 1):
        if (j,i) in still_there:
            builder += "#"
        else:
            builder += " "
    print(builder)

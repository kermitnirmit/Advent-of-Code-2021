import numpy as np
from parse import parse
from collections import defaultdict
from itertools import product
from tqdm import tqdm, trange
a = np.zeros((101,101,101))

# f = open("input.txt").read().strip().split("\n")
f = open("test.txt").read().strip().split("\n")

steps = []
maxx = 0
maxy = 0
maxz = 0

minx = 0
miny = 0
minz = 0

for line in f:
    toggle, xmin, xmax, ymin, ymax, zmin, zmax = parse("{} x={:d}..{:d},y={:d}..{:d},z={:d}..{:d}", line).fixed
    toggle = 1 if toggle == "on" else 0
    # maxx = max(maxx, xmax)
    # minx = min(minx, xmin)
    # maxy = max(maxy, ymax)
    # miny = min(miny, ymin)
    # maxz = max(maxz, zmax)
    # minz = min(minz, zmin)
    steps.append((toggle, xmin, xmax, ymin, ymax, zmin, zmax))

for toggle, xmin, xmax, ymin, ymax, zmin, zmax in steps:
    if xmax < -50 or xmin > 50 or ymax < -50 or ymin > 50 or zmax < -50 or zmin > 50:
        pass
    else:
        a[xmin+50:xmax+50+1, ymin+50:ymax+50+1, zmin+50:zmax+50+1] = toggle
    # print(a.sum())
    # input("continue")
print("part 1", int(a.sum()))

xranges = np.zeros(maxx + 1 + (-1 * minx))
yranges = np.zeros(maxy + 1 + (-1 * miny))
zranges = np.zeros(maxz + 1 + (-1 * minz))

# print(minx, maxx)
print(len(xranges))

vol = 0
xdict = defaultdict(set)
for toggle, xmin, xmax, ymin, ymax, zmin, zmax in steps[:2]:
    vol = 0
    for x in range(xmin, xmax + 1):
        if toggle:
            xdict[x] = xdict[x] | set(product(range(ymin, ymax + 1), range(zmin, zmax + 1)))
    for v in xdict.values():
        vol += len(v)
    print(vol)
print(xdict)


print(xranges)
print(yranges)
print(zranges)
vol = 0

print(xranges.sum() * yranges.sum() * zranges.sum())



# for toggle, xmin, xmax, ymin, ymax, zmin, zmax in tqdm(steps):
#     for i in trange(xmin, xmax + 1):
#         for j in range(ymin, ymax + 1):
#             for k in range(zmin, zmax + 1):
#                 if toggle == 1:
#                     ons.add((i, j, k))
#                 if toggle == 0:
#                     if (i,j,k) in ons:
#                         ons.remove((i,j,k))
#
# print(len(ons))
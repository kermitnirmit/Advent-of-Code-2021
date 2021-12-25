import numpy as np
from parse import parse

a = np.zeros((101, 101, 101))

f = open("input.txt").read().strip().split("\n")
# f = open("test.txt").read().strip().split("\n")

steps = []
stepsandbounds = []
for line in f:
    toggle, xmin, xmax, ymin, ymax, zmin, zmax = parse("{} x={:d}..{:d},y={:d}..{:d},z={:d}..{:d}", line).fixed
    toggle = 1 if toggle == "on" else 0
    steps.append((toggle, xmin, xmax, ymin, ymax, zmin, zmax))
    bounds = ((xmin, xmax + 1), (ymin, ymax + 1), (zmin, zmax + 1))
    stepsandbounds.append((toggle, bounds))

for toggle, xmin, xmax, ymin, ymax, zmin, zmax in steps:
    if xmax < -50 or xmin > 50 or ymax < -50 or ymin > 50 or zmax < -50 or zmin > 50:
        pass
    else:
        a[xmin + 50:xmax + 50 + 1, ymin + 50:ymax + 50 + 1, zmin + 50:zmax + 50 + 1] = toggle
print("part 1", int(a.sum()))

# p2
# shamelessly stolen from adi

def intersect(a, b):
    if a[0] > b[1] or b[0] > a[1]:
        return None
    nums = sorted([a[0], a[1], b[0], b[1]])
    return [nums[1], nums[2]]

def intersect3d(a,b):
    ret = []
    for q,w in zip(a,b):
        res = intersect(q,w)
        if res is None:  # if there's any 1d part that doesn't overlap, the whole cube is separate
            return None
        ret.append(res)
    return ret

def volume(cube):
    bounds = cube[0]
    v = 1
    for low, hi in bounds:
        v *= (hi - low)
    for c in cube[1]:
        v -= volume(c)
    return v

def make_hole(c, b):
    doesintersect = intersect3d(c[0], b)
    if doesintersect:
        for i, sub_cube in enumerate(c[1]):
            c[1][i] = make_hole(sub_cube, b)
        c[1].append((doesintersect, []))
    return c

cubes = []
for toggle, bounds in stepsandbounds:
    for i, cube in enumerate(cubes):
        cubes[i] = make_hole(cube, bounds)
        # basically prevents double counting -
        # if a cube partially overlaps with another cube with ON,
        # this creates a negative space so the double count becomes one. 1+1 - 1 = 1
    if toggle:
        cubes.append((bounds, []))  # this is an on inst so have to add this area

# rvol = 0
print("part 2", sum(volume(c) for c in cubes))
